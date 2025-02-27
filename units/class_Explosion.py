from pygame.sprite import Sprite
from pygame.transform import rotozoom
from classes.class_Animator import Animator


class Explosion(Animator, Sprite):
    def __init__(
        self,
        dir_path=None,
        speed_frame=None,
        obj=None,
        loops=None,
        size=None,
        angle=None,
        scale_value=None,
    ):
        super().__init__(
            dir_path=dir_path,
            speed_frame=speed_frame,
            loops=loops,
            size=size,
            scale_value=scale_value,
            )

        self.angle = angle
        self.obj=obj
        self.rect = self.image_rotation.get_rect(center=self.obj.rect.center)

    def update(self):
        if self.loops > 0:
            self.angle = self.obj.angle
            self.image_rotation = self.frames[self.frame][0]
            self.image_rotation = rotozoom(self.image_rotation, self.angle, 1)
            self.rect = self.image_rotation.get_rect(center=self.obj.rect.center)
            super().animate()
        else:
            self.kill()

