from classes.class_Animator import Animator

class Guardian(Animator):
    def __init__(
                self,
                dir_path=None,
                speed_frame=None,
                obj_rect=None
                ):
        super().__init__(
                        dir_path,
                        speed_frame,
                        obj_rect
                        )