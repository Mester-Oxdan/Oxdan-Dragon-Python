/*
 * This software is
 * Copyright (c) 2011 - 2013 Lukas Odzioba
 * Copyright (c) 2012 - 2013 magnum
 * and it is hereby released to the general public under the following terms:
 * Redistribution and use in source and binary forms, with or without
 * modification, are permitted.
 */

#include "opencl_misc.h"

#if nvidia_sm_3x(DEVICE_INFO)
#define USE_BITSELECT 1
#endif

#if gpu_nvidia(DEVICE_INFO)
#define BITALIGN_AGGRESSIVE
#else
#define BUF_UPDATE_SWITCH
#endif

#undef MD5_LUT3 /* No good for this format, just here for reference */

#define ROTATE_LEFT(x, s) rotate(x, (uint)s)

/* The basic MD5 functions */
#if MD5_LUT3
#define F(x, y, z)	lut3(x, y, z, 0xca)
#define G(x, y, z)	lut3(x, y, z, 0xe4)
#elif USE_BITSELECT
#define F(x, y, z)	bitselect(z, y, x)
#define G(x, y, z)	bitselect(y, x, z)
#else
#if HAVE_ANDNOT
#define F(x, y, z) ((x & y) ^ ((~x) & z))
#else
#define F(x, y, z)	(z ^ (x & (y ^ z)))
#endif
#define G(x, y, z)	(y ^ (z & (x ^ y)))
#endif

#if MD5_LUT3
#define H(x, y, z)	lut3(x, y, z, 0x96)
#define H2 H
#else
#define H(x, y, z)	((x ^ y) ^ z)
#define H2(x, y, z)	(x ^ (y ^ z))
#endif

#if MD5_LUT3
#define I(x, y, z)	lut3(x, y, z, 0x39)
#elif USE_BITSELECT
#define I(x, y, z)	(y ^ bitselect(0xffffffffU, x, z))
#else
#define I(x, y, z)	(y ^ (x | ~z))
#endif

#define FF(v, w, x, y, z, s, ac) {        \
                v += F(w, x, y) + z + ac; \
                v = ROTATE_LEFT(v, s) + w; \
        }

#define GG(v, w, x, y, z, s, ac) {        \
                v += G(w, x, y) + z + ac; \
                v = ROTATE_LEFT(v, s) + w; \
        }

#define HH(v, w, x, y, z, s, ac) {        \
                v += H(w, x, y) + z + ac; \
                v = ROTATE_LEFT(v, s) + w; \
        }

#define HH2(v, w, x, y, z, s, ac) {        \
                v += H2(w, x, y) + z + ac; \
                v = ROTATE_LEFT(v, s) + w; \
        }

#define II(v, w, x, y, z, s, ac) {        \
                v += I(w, x, y) + z + ac; \
                v = ROTATE_LEFT(v, s) + w; \
        }

#define S11	7
#define S12	12
#define S13	17
#define S14	22
#define S21	5
#define S22	9
#define S23	14
#define S24	20
#define S31	4
#define S32	11
#define S33	16
#define S34	23
#define S41	6
#define S42	10
#define S43	15
#define S44	21

#define AC1	0xd76aa477
#define AC2pCd	0xf8fa0bcc
#define AC3pCc	0xbcdb4dd9
#define AC4pCb	0xb18b7a77
#define MASK1	0x77777777


typedef struct {
	uint saltlen;
	uchar salt[8];
	uchar prefix;	/* 'a' = $apr1$, '1' = $1$, '\0' = {smd5} (no prefix). */
} crypt_md5_salt;

typedef struct {
	uchar v[PLAINTEXT_LENGTH];
	uchar length;
} crypt_md5_password;

typedef struct {
	uint v[4];		/** 128 bits **/
} crypt_md5_hash;

typedef struct {
	uint buffer[16];
} md5_ctx;

__constant uchar cl_md5_salt_prefix[] = "$1$";
__constant uchar cl_apr1_salt_prefix[] = "$apr1$";
__const_a8 uchar g[] =
    { 0, 7, 3, 5, 3, 7, 1, 6, 3, 5, 3, 7, 1, 7, 2, 5, 3, 7, 1, 7, 3, 4, 3, 7,
	    1, 7, 3, 5, 2, 7, 1, 7, 3, 5, 3, 6, 1, 7, 3, 5, 3, 7 };

#ifdef BUF_UPDATE_SWITCH
inline void buf_update(uint *buf, uint a, uint b, uint c, uint d, uint offset)
{
	uint i = offset >> 2;
	switch (offset & 3) {
	case 0:
		buf[i] = a;
		buf[i + 1] = b;
		buf[i + 2] = c;
		buf[i + 3] = d;
		break;
	case 1:
#ifdef BITALIGN_AGGRESSIVE
		buf[i] = BITALIGN_IMM(a, buf[i] << 24, 24);
#else
		buf[i] = (buf[i] & 0x000000ff) | (a << 8);
#endif
		buf[i + 1] = BITALIGN_IMM(b, a, 24);
		buf[i + 2] = BITALIGN_IMM(c, b, 24);
		buf[i + 3] = BITALIGN_IMM(d, c, 24);
#ifdef BITALIGN_AGGRESSIVE
		buf[i + 4] = BITALIGN_IMM(buf[i + 4] >> 8, d, 24);
#else
		buf[i + 4] = (buf[i + 4] & 0xffffff00) | (d >> 24);
#endif
		break;
	case 2:
#ifdef BITALIGN_AGGRESSIVE
		buf[i] = BITALIGN_IMM(a, buf[i] << 16, 16);
#else
		buf[i] = (buf[i] & 0x0000ffff) | (a << 16);
#endif
		buf[i + 1] = BITALIGN_IMM(b, a, 16);
		buf[i + 2] = BITALIGN_IMM(c, b, 16);
		buf[i + 3] = BITALIGN_IMM(d, c, 16);
#ifdef BITALIGN_AGGRESSIVE
		buf[i + 4] = BITALIGN_IMM(buf[i + 4] >> 16, d, 16);
#else
		buf[i + 4] = (buf[i + 4] & 0xffff0000) | (d >> 16);
#endif
		break;
	case 3:
#ifdef BITALIGN_AGGRESSIVE
		buf[i] = BITALIGN_IMM(a, buf[i] << 8, 8);
#else
		buf[i] = (buf[i] & 0x00ffffff) | (a << 24);
#endif
		buf[i + 1] = BITALIGN_IMM(b, a, 8);
		buf[i + 2] = BITALIGN_IMM(c, b, 8);
		buf[i + 3] = BITALIGN_IMM(d, c, 8);
#ifdef BITALIGN_AGGRESSIVE
		buf[i + 4] = BITALIGN_IMM(buf[i + 4] >> 24, d, 8);
#else
		buf[i + 4] = (buf[i + 4] & 0xff000000) | (d >> 8);
#endif
		break;
	}
}
#else
inline void buf_update(uint *buf, uint a, uint b, uint c, uint d, uint offset)
{
	uint i = offset >> 2;
	uint j = offset & 3;
	if (!j) {
		buf[i] = a;
		buf[i + 1] = b;
		buf[i + 2] = c;
		buf[i + 3] = d;
		return;
	}

	j <<= 3;
	uint k = 32 - j;
#ifdef BITALIGN_AGGRESSIVE
	buf[i] = BITALIGN(a, buf[i] << k, k);
#else
	buf[i] = (buf[i] & (0xffffffffU >> k)) | (a << j);
#endif
	buf[i + 1] = BITALIGN(b, a, k);
	buf[i + 2] = BITALIGN(c, b, k);
	buf[i + 3] = BITALIGN(d, c, k);
#ifdef BITALIGN_AGGRESSIVE
	buf[i + 4] = BITALIGN(buf[i + 4] >> j, d, k);
#else
	buf[i + 4] = (buf[i + 4] & (0xffffffffU << j)) | (d >> k);
#endif
}
#endif

inline void ctx_update(md5_ctx *ctx, uchar *string, uint len,
    uint *ctx_buflen)
{
	uint i;

	for (i = 0; i < len; i++)
		PUTCHAR(ctx->buffer, *ctx_buflen + i, string[i]);

	*ctx_buflen += len;
}

inline void ctx_update_prefix(md5_ctx *ctx, uchar prefix, uint *ctx_buflen)
{
	uint i;

	if (prefix == '1') {
		for (i = 0; i < 3; i++)
			PUTCHAR(ctx->buffer, *ctx_buflen + i,
			    cl_md5_salt_prefix[i]);
		*ctx_buflen += 3;
	} else if (prefix == 'a') {
		for (i = 0; i < 6; i++)
			PUTCHAR(ctx->buffer, *ctx_buflen + i,
			    cl_apr1_salt_prefix[i]);
		*ctx_buflen += 6;
	}
	// else if (prefix == '\0') do nothing. for {smd5}
}

inline void init_ctx(md5_ctx *ctx, uint *ctx_buflen)
{
	uint i;
	uint *buf = (uint *) ctx->buffer;

#if gpu_nvidia(DEVICE_INFO)
#pragma unroll 4
#endif
	for (i = 0; i < sizeof(ctx->buffer) / 4; i++)
		*buf++ = 0;
	*ctx_buflen = 0;
}

inline void md5_digest(md5_ctx *ctx, uint *result, uint len,
    uint res_offset)
{
	uint *x = ctx->buffer;
	uint a;
	uint b = 0xefcdab89;
	uint c = 0x98badcfe;
	uint d = 0x10325476;

	a = ROTATE_LEFT(AC1 + x[0], S11);
	a += b;			/* 1 */
	d = ROTATE_LEFT((c ^ (a & MASK1)) + x[1] + AC2pCd, S12);
	d += a;			/* 2 */
	c = ROTATE_LEFT(F(d, a, b) + x[2] + AC3pCc, S13);
	c += d;			/* 3 */
	b = ROTATE_LEFT(F(c, d, a) + x[3] + AC4pCb, S14);
	b += c;			/* 4 */
	FF(a, b, c, d, x[4], S11, 0xf57c0faf);	/* 5 */
	FF(d, a, b, c, x[5], S12, 0x4787c62a);	/* 6 */
	FF(c, d, a, b, x[6], S13, 0xa8304613);	/* 7 */
	FF(b, c, d, a, x[7], S14, 0xfd469501);	/* 8 */
	FF(a, b, c, d, x[8], S11, 0x698098d8);	/* 9 */
	FF(d, a, b, c, x[9], S12, 0x8b44f7af);	/* 10 */
	FF(c, d, a, b, x[10], S13, 0xffff5bb1);	/* 11 */
	FF(b, c, d, a, x[11], S14, 0x895cd7be);	/* 12 */
	FF(a, b, c, d, x[12], S11, 0x6b901122);	/* 13 */
	FF(d, a, b, c, x[13], S12, 0xfd987193);	/* 14 */
	FF(c, d, a, b, len, S13, 0xa679438e);	/* 15 */
	FF(b, c, d, a, 0, S14, 0x49b40821);	/* 16 */

	GG(a, b, c, d, x[1], S21, 0xf61e2562);	/* 17 */
	GG(d, a, b, c, x[6], S22, 0xc040b340);	/* 18 */
	GG(c, d, a, b, x[11], S23, 0x265e5a51);	/* 19 */
	GG(b, c, d, a, x[0], S24, 0xe9b6c7aa);	/* 20 */
	GG(a, b, c, d, x[5], S21, 0xd62f105d);	/* 21 */
	GG(d, a, b, c, x[10], S22, 0x2441453);	/* 22 */
	GG(c, d, a, b, 0, S23, 0xd8a1e681);	/* 23 */
	GG(b, c, d, a, x[4], S24, 0xe7d3fbc8);	/* 24 */
	GG(a, b, c, d, x[9], S21, 0x21e1cde6);	/* 25 */
	GG(d, a, b, c, len, S22, 0xc33707d6);	/* 26 */
	GG(c, d, a, b, x[3], S23, 0xf4d50d87);	/* 27 */
	GG(b, c, d, a, x[8], S24, 0x455a14ed);	/* 28 */
	GG(a, b, c, d, x[13], S21, 0xa9e3e905);	/* 29 */
	GG(d, a, b, c, x[2], S22, 0xfcefa3f8);	/* 30 */
	GG(c, d, a, b, x[7], S23, 0x676f02d9);	/* 31 */
	GG(b, c, d, a, x[12], S24, 0x8d2a4c8a);	/* 32 */

	HH(a, b, c, d, x[5], S31, 0xfffa3942);	/* 33 */
	HH2(d, a, b, c, x[8], S32, 0x8771f681);	/* 34 */
	HH(c, d, a, b, x[11], S33, 0x6d9d6122);	/* 35 */
	HH2(b, c, d, a, len, S34, 0xfde5380c);	/* 36 */
	HH(a, b, c, d, x[1], S31, 0xa4beea44);	/* 37 */
	HH2(d, a, b, c, x[4], S32, 0x4bdecfa9);	/* 38 */
	HH(c, d, a, b, x[7], S33, 0xf6bb4b60);	/* 39 */
	HH2(b, c, d, a, x[10], S34, 0xbebfbc70);/* 40 */
	HH(a, b, c, d, x[13], S31, 0x289b7ec6);	/* 41 */
	HH2(d, a, b, c, x[0], S32, 0xeaa127fa);	/* 42 */
	HH(c, d, a, b, x[3], S33, 0xd4ef3085);	/* 43 */
	HH2(b, c, d, a, x[6], S34, 0x4881d05);	/* 44 */
	HH(a, b, c, d, x[9], S31, 0xd9d4d039);	/* 45 */
	HH2(d, a, b, c, x[12], S32, 0xe6db99e5);/* 46 */
	HH(c, d, a, b, 0, S33, 0x1fa27cf8);	/* 47 */
	HH2(b, c, d, a, x[2], S34, 0xc4ac5665);	/* 48 */

	II(a, b, c, d, x[0], S41, 0xf4292244);	/* 49 */
	II(d, a, b, c, x[7], S42, 0x432aff97);	/* 50 */
	II(c, d, a, b, len, S43, 0xab9423a7);	/* 51 */
	II(b, c, d, a, x[5], S44, 0xfc93a039);	/* 52 */
	II(a, b, c, d, x[12], S41, 0x655b59c3);	/* 53 */
	II(d, a, b, c, x[3], S42, 0x8f0ccc92);	/* 54 */
	II(c, d, a, b, x[10], S43, 0xffeff47d);	/* 55 */
	II(b, c, d, a, x[1], S44, 0x85845dd1);	/* 56 */
	II(a, b, c, d, x[8], S41, 0x6fa87e4f);	/* 57 */
	II(d, a, b, c, 0, S42, 0xfe2ce6e0);	/* 58 */
	II(c, d, a, b, x[6], S43, 0xa3014314);	/* 59 */
	II(b, c, d, a, x[13], S44, 0x4e0811a1);	/* 60 */
	II(a, b, c, d, x[4], S41, 0xf7537e82);	/* 61 */
	II(d, a, b, c, x[11], S42, 0xbd3af235);	/* 62 */
	II(c, d, a, b, x[2], S43, 0x2ad7d2bb);	/* 63 */
	II(b, c, d, a, x[9], S44, 0xeb86d391);	/* 64 */

	a += 0x67452301;
	b += 0xefcdab89;
	c += 0x98badcfe;
	d += 0x10325476;

	if (!res_offset) {
		result[0] = a;
		result[1] = b;
		result[2] = c;
		result[3] = d;
		return;
	}

	buf_update(result, a, b, c, d, res_offset);
}

__kernel void cryptmd5(__global const crypt_md5_password *inbuffer,
    __global crypt_md5_hash *outbuffer, __constant crypt_md5_salt *hsalt)
{
	uint idx = get_global_id(0);
	uint pass_len = inbuffer[idx].length;
	uint salt_len = hsalt->saltlen;
	uint alt_result[4];
	md5_ctx ctx[8];
	uint ctx_buflen[8];
	union {
		uint w[(PLAINTEXT_LENGTH + 3) / 4];
		uchar c[PLAINTEXT_LENGTH];
	} pass;
	union {
		uint w[2];
		uchar c[8];
	} salt;
	uint i;

#if gpu_nvidia(DEVICE_INFO)
#pragma unroll 4
#endif
	for (i = 0; i < (PLAINTEXT_LENGTH + 3) / 4; i++)
		pass.w[i] = ((__global uint *) &inbuffer[idx].v)[i];

	salt.w[0] = ((__constant uint *) &hsalt->salt)[0];
	salt.w[1] = ((__constant uint *) &hsalt->salt)[1];

	init_ctx(&ctx[1], &ctx_buflen[1]);
	ctx_update(&ctx[1], pass.c, pass_len, &ctx_buflen[1]);
	ctx_update(&ctx[1], salt.c, salt_len, &ctx_buflen[1]);
	ctx_update(&ctx[1], pass.c, pass_len, &ctx_buflen[1]);
	PUTCHAR(ctx[1].buffer, ctx_buflen[1], 0x80);
	md5_digest(&ctx[1], alt_result, ctx_buflen[1] << 3, 0);

	init_ctx(&ctx[1], &ctx_buflen[1]);
	ctx_update(&ctx[1], pass.c, pass_len, &ctx_buflen[1]);
	ctx_update_prefix(&ctx[1], hsalt->prefix, &ctx_buflen[1]);
	ctx_update(&ctx[1], salt.c, salt_len, &ctx_buflen[1]);
#if PLAINTEXT_LENGTH >= 16
	for (i = pass_len; i > 16; i -= 16)
		ctx_update(&ctx[1], (uchar *) alt_result, 16, &ctx_buflen[1]);
	ctx_update(&ctx[1], (uchar *) alt_result, i, &ctx_buflen[1]);
#else
	ctx_update(&ctx[1], (uchar *) alt_result, pass_len, &ctx_buflen[1]);
#endif
	for (i = pass_len; i > 0; i >>= 1) {
		uchar c = (i & 1) ? 0 : pass.c[0];
		PUTCHAR(ctx[1].buffer, ctx_buflen[1], c);
		ctx_buflen[1]++;
	}

	//pattern[0]=alt pass
	//pattern[1]=alt pass pass
	//pattern[2]=alt salt pass
	//pattern[3]=alt salt pass pass
	//pattern[4]=pass alt
	//pattern[5]=pass pass alt
	//pattern[6]=pass salt alt
	//pattern[7]=pass salt pass alt

	uchar altpos[4];
	altpos[0] = pass_len;
	altpos[1] = pass_len * 2;
	altpos[2] = pass_len + salt_len;
	altpos[3] = altpos[1] + salt_len;

	//prepare pattern buffers
	init_ctx(&ctx[0], &ctx_buflen[0]);
	PUTCHAR(ctx[1].buffer, ctx_buflen[1], 0x80);
	//alt pass
	md5_digest(&ctx[1], ctx[0].buffer, ctx_buflen[1] << 3, 0);	//add results from init
	ctx_buflen[0] = 16;
	for (i = 1; i < 8; i++)	//1 not 0
		init_ctx(&ctx[i], &ctx_buflen[i]);

	ctx_update(&ctx[0], pass.c, pass_len, &ctx_buflen[0]);
	PUTCHAR(ctx[0].buffer, ctx_buflen[0], 0x80);

	//alt pass pass
	ctx_buflen[1] = 16;
	ctx_update(&ctx[1], pass.c, pass_len, &ctx_buflen[1]);
	ctx_update(&ctx[1], pass.c, pass_len, &ctx_buflen[1]);
	PUTCHAR(ctx[1].buffer, ctx_buflen[1], 0x80);
	//alt salt pass
	ctx_buflen[2] = 16;
	ctx_update(&ctx[2], salt.c, salt_len, &ctx_buflen[2]);
	ctx_update(&ctx[2], pass.c, pass_len, &ctx_buflen[2]);
	PUTCHAR(ctx[2].buffer, ctx_buflen[2], 0x80);
	//alt salt pass pass
	ctx_buflen[3] = 16;
	ctx_update(&ctx[3], salt.c, salt_len, &ctx_buflen[3]);
	ctx_update(&ctx[3], pass.c, pass_len, &ctx_buflen[3]);
	ctx_update(&ctx[3], pass.c, pass_len, &ctx_buflen[3]);
	PUTCHAR(ctx[3].buffer, ctx_buflen[3], 0x80);
	//pass alt
	ctx_update(&ctx[4], pass.c, pass_len, &ctx_buflen[4]);
	ctx_buflen[4] += 16;
	PUTCHAR(ctx[4].buffer, ctx_buflen[4], 0x80);
	//pass pass alt
	ctx_update(&ctx[5], pass.c, pass_len, &ctx_buflen[5]);
	ctx_update(&ctx[5], pass.c, pass_len, &ctx_buflen[5]);
	ctx_buflen[5] += 16;
	PUTCHAR(ctx[5].buffer, ctx_buflen[5], 0x80);
	//pass salt alt
	ctx_update(&ctx[6], pass.c, pass_len, &ctx_buflen[6]);
	ctx_update(&ctx[6], salt.c, salt_len, &ctx_buflen[6]);
	ctx_buflen[6] += 16;
	PUTCHAR(ctx[6].buffer, ctx_buflen[6], 0x80);
	//pass salt pass alt
	ctx_update(&ctx[7], pass.c, pass_len, &ctx_buflen[7]);
	ctx_update(&ctx[7], salt.c, salt_len, &ctx_buflen[7]);
	ctx_update(&ctx[7], pass.c, pass_len, &ctx_buflen[7]);
	ctx_buflen[7] += 16;
	PUTCHAR(ctx[7].buffer, ctx_buflen[7], 0x80);

#if gpu_nvidia(DEVICE_INFO)
#pragma unroll 8
#endif
	for (i = 0; i < 8; i++)
		ctx_buflen[i] <<= 3;

	uint id1 = g[0], id2;

	int j = 1;
#if gpu_nvidia(DEVICE_INFO)
	for (i = 0; i < 250; i++) {
#else
	for (i = 0; i < 500; i++) {
#endif
		id2 = g[j];
		md5_digest(&ctx[id1], ctx[id2].buffer, ctx_buflen[id1],
		    altpos[id2 - 4]);
		if (j == 41)
			j = -1;
		id1 = g[j + 1];
		md5_digest(&ctx[id2], ctx[id1].buffer, ctx_buflen[id2], 0);

#if gpu_nvidia(DEVICE_INFO)
		id2 = g[j + 2];
		md5_digest(&ctx[id1], ctx[id2].buffer, ctx_buflen[id1],
		    altpos[id2 - 4]);
		if (j == 39)
			j = -3;
		id1 = g[j + 3];
		j += 4;
		md5_digest(&ctx[id2], ctx[id1].buffer, ctx_buflen[id2], 0);
#else
		j += 2;
#endif
	}

#if gpu_nvidia(DEVICE_INFO)
#pragma unroll 4
#endif
	for (i = 0; i < 4; i++)
		outbuffer[idx].v[i] = ctx[3].buffer[i];
}
