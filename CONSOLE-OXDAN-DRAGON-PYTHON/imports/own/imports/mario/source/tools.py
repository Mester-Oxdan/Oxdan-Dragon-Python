__author__ = 'marble_xu'

import os
import pygame as pg
from abc import ABC, abstractmethod
import pygame
import imports.own.will_go_to_start

keybinding = {
    'action':pg.K_SPACE,
    'jump':pg.K_UP,
    'jump_1':pg.K_w,
    'left':pg.K_LEFT,
    'left_1':pg.K_a,
    'right':pg.K_RIGHT,
    'right_1':pg.K_d,
    'down':pg.K_DOWN,
    'down_1':pg.K_s,
    'escape': pg.K_ESCAPE
}

class State():
    def __init__(self):
        self.start_time = 0.0
        self.current_time = 0.0
        self.done = False
        self.next = None
        self.persist = {}
    
    @abstractmethod
    def startup(self, current_time, persist):
        '''abstract method'''

    def cleanup(self):
        self.done = False
        return self.persist
    
    @abstractmethod
    def update(sefl, surface, keys, current_time):
        '''abstract method'''

class Control():
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode((800, 600))  # Set the screen size as needed
        self.done = False
        self.clock = pg.time.Clock()
        self.fps = 60
        self.current_time = 0.0
        self.keys = pg.key.get_pressed()
        self.state_dict = {}
        self.state_name = None
        self.state = None
    
    def setup_states(self, state_dict, start_state):
        self.state_dict = state_dict
        self.state_name = start_state
        self.state = self.state_dict[self.state_name]
    
    def update(self):
        self.current_time = pg.time.get_ticks()
        if self.state.done:
            self.flip_state()
        self.state.update(self.screen, self.keys, self.current_time)
    
    def flip_state(self):
        previous, self.state_name = self.state_name, self.state.next
        persist = self.state.cleanup()
        self.state = self.state_dict[self.state_name]
        self.state.startup(self.current_time, persist)

    def event_loop(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.done = True
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    self.done = True
            self.keys = pg.key.get_pressed()
    
    def main(self):
        while not self.done:
            self.event_loop()
            self.update()
            pg.display.update()
            self.clock.tick(self.fps)
        pg.quit()

def get_image(sheet, x, y, width, height, colorkey, scale):
        image = pg.Surface([width, height])
        rect = image.get_rect()

        image.blit(sheet, (0, 0), (x, y, width, height))
        image.set_colorkey(colorkey)
        image = pg.transform.scale(image,
                                   (int(rect.width*scale),
                                    int(rect.height*scale)))
        return image

def load_all_gfx(directory, colorkey=(255,0,255), accept=('.png', '.jpg', '.bmp', '.gif')):
    graphics = {}
    for pic in os.listdir(directory):
        name, ext = os.path.splitext(pic)
        if ext.lower() in accept:
            img = pg.image.load(os.path.join(directory, pic))
            if img.get_alpha():
                img = img.convert_alpha()
            else:
                img = img.convert()
                img.set_colorkey(colorkey)
            graphics[name] = img
    return graphics
