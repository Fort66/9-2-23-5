import pygame as pg
from pygame.display import set_mode, set_caption, set_icon, get_desktop_sizes
from pygame.image import load
from pygame.locals import RESIZABLE, FULLSCREEN

from dataclasses import dataclass

pg.init()

@dataclass
class ScreenGame:
    size: tuple = (1280, 720)
    color: str | tuple = 'SteelBlue'
    caption: str = 'Game'
    icon: str = ''
    is_resizable: bool = False
    is_full_screen: bool = False

    def __post_init__(self):
        if self.is_resizable:
            self.window = set_mode(self.size, RESIZABLE)
        elif self.is_full_screen:
            self.window = set_mode(get_desktop_sizes()[0], FULLSCREEN)
        else:
            self.window = set_mode(self.size)
        set_caption(self.caption)
        if self.icon:
            set_icon(load(self.icon))

        self.rect = self.window.get_rect()
        
    
    def update_caption(self, caption):
       self.caption = set_caption(caption)


