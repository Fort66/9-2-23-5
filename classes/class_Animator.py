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
        self.original_frames = [[scale(load(f'{self.dir_path}/{value}').convert_alpha(), self.obj_rect[2:]), self.speed_frame] for value in file_list]
        self.frames = self.original_frames.copy()
        self.rect = self.frames[0][0].get_rect(center=self.obj_rect.center)


    def animate(self, obj):
        if self.frame_time == 0:
            self.frame_time = time()

        if time() - self.frame_time >= self.frames[self.frame][1] and not self.paused:
            self.frame = self.frame + 1 if self.frame < len(self.frames) - 1 else 0
            scale(self.frames[self.frame][0], self.obj_rect[2:])
            self.frame_time = time()
            if self.frame >= len(self.frames) - 1:
                self.loops[0] += 1







