import pygame as pg
from imports.doom.settings import *
from imports.doom.map import *
from imports.doom.player import *
from imports.doom.raycasting import *
from imports.doom.object_renderer import *
from imports.doom.sprite_object import *
from imports.doom.object_handler import *
from imports.doom.weapon import *
from imports.doom.sound import *
from imports.doom.pathfinding import *
import imports.own.will_go_to_start
import pygame

def doom_start():

    class Game:
        def __init__(self):
            pg.init()
            pg.mouse.set_visible(False)
            self.screen = pg.display.set_mode(RES)
            self.clock = pg.time.Clock()
            self.delta_time = 1
            self.global_trigger = False
            self.global_event = pg.USEREVENT + 0
            pg.time.set_timer(self.global_event, 40)
            self.new_game()
            ico = pygame.image.load(os.path.join(os.environ["OXDAN-DRAGON-PYTHON"],'my_dragon_ico.jpg')).convert()
            pygame.display.set_icon (ico)

        def new_game(self):
            self.map = Map(self)
            self.player = Player(self)
            self.object_renderer = ObjectRenderer(self)
            self.raycasting = RayCasting(self)
            self.object_handler = ObjectHandler(self)
            self.weapon = Weapon(self)
            self.sound = Sound(self)
            self.pathfinding = PathFinding(self)
            pg.mixer.music.play(-1)

        def update(self):
            self.player.update()
            self.raycasting.update()
            self.object_handler.update()
            self.weapon.update()
            pg.display.flip()
            self.delta_time = self.clock.tick(FPS)
            pg.display.set_caption(f'{self.clock.get_fps() :.1f}')

        def draw(self):
            # self.screen.fill('black')
            self.object_renderer.draw()
            self.weapon.draw()
            # self.map.draw()
            # self.player.draw()

        def check_events(self):
            self.global_trigger = False
            for event in pg.event.get():
                if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                    pg.quit()
                    imports.own.will_go_to_start.main()
                elif event.type == self.global_event:
                    self.global_trigger = True
                self.player.single_fire_event(event)

        def run(self):
            while True:
                self.check_events()
                self.update()
                self.draw()

    game = Game()
    game.run()
