from pygame.sprite import Sprite
from classes.class_Animator import Animator
from functions.function_guards_collision import player_guard_collision, enemies_guard_collision, guards_collision

from time import time


class Guardian(Animator, Sprite):
    def __init__(
        self,
        dir_path=None,
        speed_frame=None,
        obj_rect=None,
        guard_level=None,
        obj=None
    ):
        super().__init__(
            dir_path=dir_path,
            speed_frame=speed_frame,
            obj_rect=obj_rect,
            obj=obj
            )

        self.guard_level = guard_level
        self.destruction_time = 0
        # self.obj_rect = obj_rect

    def decrease_level(self, value):
        if self.guard_level > 0:
            self.guard_level -= value


    def update(self):
        player_guard_collision()
        enemies_guard_collision()
        guards_collision()
            # if self.destruction_time <= 0:
            #     self.destruction_time = time()
        super().update()
