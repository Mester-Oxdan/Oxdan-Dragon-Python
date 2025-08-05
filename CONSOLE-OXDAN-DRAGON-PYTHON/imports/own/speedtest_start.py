import speedtest
from time import sleep
import threading
import sys
import imports.own.start_start

spinner_running = True

def spinner_task(label):
    frames = ['|', '/', '-', '\\']
    i = 0
    while spinner_running:
        sys.stdout.write(f'\r{label} {frames[i % len(frames)]}')
        sys.stdout.flush()
        sleep(0.1)
        i += 1

def speedtest_start():
                    global spinner_running
                    st = speedtest.Speedtest()

                    print("🔍 Retrieving and selecting best server...")
                    st.get_servers()
                    best = st.get_best_server()

                    print(f"✅ Selected server: {best['sponsor']} in {best['name']}, {best['country']}")

                    # Spinner for download
                    spinner_running = True
                    spinner = threading.Thread(target=spinner_task, args=("⬇️ Testing download speed...",))
                    spinner.start()
                    download_speed = st.download()
                    spinner_running = False
                    spinner.join()

                    # Spinner for upload with retry
                    upload_speed = None
                    for attempt in range(3):
                        try:
                            spinner_running = True
                            spinner = threading.Thread(target=spinner_task, args=("⬆️ Testing upload speed...",))
                            spinner.start()
                            upload_speed = st.upload()
                            spinner_running = False
                            spinner.join()
                            break
                        except speedtest.SpeedtestUploadTimeout:
                            spinner_running = False
                            spinner.join()
                            print(f"⚠️ Upload timed out. Retrying ({attempt + 1}/3)...")
                            sleep(1)

                    ping = st.results.ping

                    print("\n📡 Results:")
                    print(f"Ping: {ping:.2f} ms")
                    print(f"Download: {download_speed / 1_000_000:.2f} Mbps")
                    if upload_speed:
                        print(f"Upload: {upload_speed / 1_000_000:.2f} Mbps")
                    else:
                        print("Upload: ❌ Failed (timeout)")

                    sleep(0.01)
                    imports.own.will_go_to_start.main()