from pygame.sprite import Sprite
from classes.class_Animator import Animator
from functions.function_guards_collision import player_guard_collision, enemies_guard_collision, guards_collision



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
        # self.obj_rect = obj_rect

    @property
    def decrease_level(self):
        if self.guard_level > 0:
            self.guard_level -= 1


    def update(self):
        player_guard_collision(self)
        enemies_guard_collision(self)
        guards_collision(self)
        super().update()
