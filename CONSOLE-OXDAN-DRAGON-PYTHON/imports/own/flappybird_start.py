import os
import pygame
import time
import random
import imports.own.will_go_to_start

clockflappybird = pygame.time.Clock()

def replay_or_quit():

            for event in pygame.event.get([pygame.KEYDOWN, pygame.KEYUP, pygame.QUIT]):
                if event.type == pygame.QUIT:
                    pygame.quit()
                    imports.own.will_go_to_start.main()

                elif event.type == pygame.KEYDOWN:
                    continue

                return event.key
            return None

def flappybird_start():

        black = (0, 0, 0)
        white = (255, 255, 255)
        green = (34, 139, 34)
        blue = (64, 224, 208)
        pygame.init()

        # resolution - width,height
        surfaceWidth = 800
        surfaceHeight = 500
        surface = pygame.display.set_mode((surfaceWidth, surfaceHeight))
        pygame.display.set_caption('Flappy Bird')
        ico = pygame.image.load(os.path.join(os.environ["OXDAN-DRAGON-PYTHON"], 'imports/own/my_dragon_ico.jpg')).convert()
        pygame.display.set_icon (ico)

        img = pygame.image.load(os.path.join(os.environ["OXDAN-DRAGON-PYTHON"],'imports/own/resources/images/flap.png'))
        img_width = img.get_size()[0]
        img_height = img.get_size()[1]


        def show_score(current_score):
            font = pygame.font.Font('freesansbold.ttf', 20)
            text = font.render('Score: ' + str(current_score), True, white)
            surface.blit(text, [3, 3])


        def blocks(x_block, y_block, block_width, block_height, gap):
            pygame.draw.rect(surface, green, [x_block, y_block, block_width, block_height])
            pygame.draw.rect(surface, green, [x_block, y_block + block_height + gap, block_width, surfaceHeight])


        def makeTextObjs(text, font):
            textSurface = font.render(text, True, white)
            return textSurface, textSurface.get_rect()

        def msg_surface(text):
            smallText = pygame.font.Font('freesansbold.ttf', 20)
            largeText = pygame.font.Font('freesansbold.ttf', 130)

            titletextSurf, titleTextRect = makeTextObjs(text, largeText)
            titleTextRect.center = surfaceWidth / 2, surfaceHeight / 2
            surface.blit(titletextSurf, titleTextRect)

            typtextSurf, typTextRect = makeTextObjs('Press any key to continue', smallText)
            typTextRect.center = surfaceWidth / 2, ((surfaceHeight / 2) + 100)
            surface.blit(typtextSurf, typTextRect)

            pygame.display.update()
            time.sleep(1)

            while replay_or_quit() is None:
                clockflappybird.tick()

            flappybird()


        def gameOver():
            msg_surface('Game over')


        def bird(x, y, image):
            surface.blit(image, (x, y))

        def flappybird():
            
            x = 150
            y = 200
            y_move = 0

            x_block = surfaceWidth
            y_block = 0

            block_width = 50
            block_height = random.randint(0, surfaceHeight / 2)
            gap = img_height * 5

            # speed of blocks
            block_move = 5

            score = 0
            game_over = False

            # Game Loop/ Game State
            while not game_over:

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        game_over = True
                        pygame.quit()
                        imports.own.will_go_to_start.main()

                    # keydown - when button is pressed keyup - when it's released
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_UP or pygame.K_SPACE:
                            y_move = -5
                        if event.key == pygame.K_ESCAPE:
                            game_over = True
                            pygame.quit()
                            imports.own.will_go_to_start.main()

                    if event.type == pygame.KEYUP:
                        if event.key == pygame.K_UP or pygame.K_SPACE:
                            y_move = 5
                        if event.key == pygame.K_ESCAPE:
                            game_over = True
                            pygame.quit()
                            imports.own.will_go_to_start.main()

                y = y + y_move

                surface.fill(blue)
                bird(x, y, img)
                show_score(score)

                # Adding difficulty relative to score
                # Increasing the speed and decreasing the gap of blocks

                if 3 <= score < 5:
                    block_move = 6
                    gap = img_height * 3.3

                if 5 <= score < 8:
                    block_move = 7
                    gap = img_height * 3.1

                if 8 <= score < 14:
                    block_move = 8
                    gap = img_height * 3

                if score >= 14:
                    block_move = 8
                    gap = img_height * 2.5

                blocks(x_block, y_block, block_width, block_height, gap)
                x_block -= block_move

                # boundaries
                if y > surfaceHeight - img_height or y < 0:
                    gameOver()

                # blocks on screen or not
                if x_block < (-1 * block_width):
                    x_block = surfaceWidth
                    block_height = random.randint(0, surfaceHeight / 2)

                # Collision Detection

                # detecting whether we are past the block or not in X
                if x + img_width > x_block and x < x_block + block_width:
                    if y < block_height or y + img_height > block_height + gap:
                        gameOver()

                if x > x_block + block_width and x < x_block + block_width + img_width / 5:
                    score += 1

                pygame.display.update()
                clockflappybird.tick(80)


        flappybird()
        pygame.quit()
        imports.own.will_go_to_start.main()