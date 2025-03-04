from classes.class_Animator import Animator

class BackgroundScreen(Animator):
    def __init__(
        self,
        dir_path=None,
        speed_frame=None,
        owner=None,
        loops=None,
        size=None,
        scale_value=None,
        no_group=None
        ):
        super().__init__(
            dir_path=dir_path,
            speed_frame=speed_frame,
            loops=loops,
            size=size,
            scale_value=scale_value,
            no_group=no_group
        )

        self.owner = owner
        self.rect = self.image_rotation.get_rect(center=self.owner.rect.center)

    def update(self):
        self.image_rotation = self.frames[self.frame][0]
        self.rect = self.image_rotation.get_rect(center=self.owner.rect.center)
        self.animate()
        self.owner.window.blit(self.image_rotation, self.rect)
