import pygame as pg
from pygame.image import load
from pygame.transform import scale

from os import listdir
from time import time

from icecream import ic


class Animator:
    def __init__(
                self,
                dir_path=None,
                speed_frame=None,
                obj_rect=None
                ):
        
        self.dir_path = dir_path
        self.speed_frame = speed_frame
        self.obj_rect = obj_rect
        
        self.frames = None
        self.frame = 0
        self.frame_time = 0
        self.pause_time = 0
        self.paused = False
        self.loops = [0, -1]
        self.ended = False
        self.__post_init__()

    def __post_init__(self):
        file_list = listdir(self.dir_path)
        


