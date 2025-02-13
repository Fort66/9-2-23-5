from pygame.sprite import Sprite
from pygame.transform import rotozoom, scale_by, flip
from pygame.image import load
from pygame.locals import MOUSEWHEEL, MOUSEBUTTONDOWN, K_a, K_w, K_d, K_s
from pygame.math import Vector2
from pygame.key import get_pressed
from units.class_Shots import Shots
from config.create_Objects import screen
from logic.class_FirstShot import FirstShot

from icecream import ic

import math
from random import randint, choice, uniform

from config.sources.enemies.source import ENEMIES

class Enemies(Sprite):
    def __init__(
                self,
                group=None,
                game=None,
                player=None
                ):
        super().__init__(group)

        self.game = game
        self.group = group
        self.player = player
        self.angle = 0
        self.speed = randint(0, 10)
        self.move_count = randint(0, 600)
        self.direction_list = [0, 1, -1]
        self.moveX = choice(self.direction_list)
        self.moveY = choice(self.direction_list)
        self.shots = False
        self.min_distance = 300
        self.shot_distance = 1500
        self.is_min_distance = False
        self.first_shot = FirstShot()
        self.__post_init__()
        self.group.add(self)

    def __post_init__(self):
        self.image_rotation = ENEMIES[1]['angle'][0]['sprite']

        self.pos = (uniform(
                            self.group.background_rect.left + 200,
                            self.group.background_rect.right - 200
                            ),
                    uniform(
                            self.group.background_rect.top + 200,
                            self.group.background_rect.bottom - 200
                            )
                    )

        self.rect = self.image_rotation.get_rect(center=self.pos)
        self.direction = Vector2(self.pos)


    def rotation(self):
        rotateX = self.player.rect.centerx - self.rect.centerx
        rotateY = self.player.rect.centery - self.rect.centery
        angle_vector = -math.atan2(rotateY, rotateX) * 180 / math.pi

        if angle_vector > 0:
            self.angle = angle_vector
        else:
            self.angle = 360 + angle_vector

        for value in ENEMIES[1]['angle']:
            if self.angle <= value:
                self.image = ENEMIES[1]['angle'][value]['sprite']
                break

        self.image_rotation = rotozoom(self.image, self.angle, 1)
        self.rect = self.image_rotation.get_rect(center=self.rect.center)


    def check_move_count(self):
        if self.move_count <= 0:
            self.move_count = randint(0, 600)
            self.speed = randint(0, 10)
            self.change_direction()
        else:
            self.move_count -= 1


    def change_direction(self):
        self.moveX = choice(self.direction_list)
        self.moveY = choice(self.direction_list)


    def ckeck_position(self):
        if self.rect.left < self.group.background_rect.left:
            self.rect.left = self.group.background_rect.left
            self.change_direction()
        if self.rect.right > self.group.background_rect.right:
            self.rect.right = self.group.background_rect.right
            self.change_direction()
        if self.rect.top < self.group.background_rect.top:
            self.rect.top = self.group.background_rect.top
            self.change_direction()
        if self.rect.bottom > self.group.background_rect.bottom:
            self.rect.bottom = self.group.background_rect.bottom
            self.change_direction()

        if not self.is_min_distance:
            if Vector2(self.rect.center).distance_to(self.player.rect.center) < self.min_distance:
                self.is_min_distance = True
                self.change_direction()
        if Vector2(self.rect.center).distance_to(self.player.rect.center) > self.min_distance:
            self.is_min_distance = False

    def move(self):
        self.rect.move_ip(self.moveX * self.speed, self.moveY * self.speed)


    def shot(self):
        if Vector2(self.rect.center).distance_to(self.player.rect.center) <= self.shot_distance:
            if self.shots and randint(0, 100) == 50:
                self.group.add(
                                Shots(
                                    pos=self.rect.center,
                                    screen=screen,
                                    group=self.group,
                                    speed=10,
                                    angle=self.angle,
                                    shoter=self,
                                    kill_shot_distance=2000,
                                    color='yellow'
                                    )
                                )


    def validate_first_shot(self):
        if self.player.first_shot:
            self.shots = True


    def update(self):
        self.ckeck_position()
        self.rotation()
        self.check_move_count()
        self.move()
        self.validate_first_shot()
        self.shot()

