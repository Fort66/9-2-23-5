from pygame.sprite import Sprite
from pygame.transform import rotozoom
from pygame.math import Vector2
from units.class_Shots import Shots
from classes.class_Animator import Animator

from icecream import ic

import math
from random import randint, choice, uniform

from config.sources.enemies.source import ENEMIES

from classes.class_SpriteGroups import SpriteGroups
from config.create_Objects import checks


class Enemies(Sprite):
    def __init__(self, player=None):
        self.sprite_groups = SpriteGroups()
        super().__init__(self.sprite_groups.camera_group)
        self.sprite_groups.enemies_group.add(self)

        self.player = player
        self.angle = 0
        self.min_distance = 300
        self.shot_distance = 1500
        self.is_min_distance = False
        self.__post_init__()
        self.random_value()
        self.change_direction()

    def __post_init__(self):
        self.image = ENEMIES[1]["angle"][0]["sprite"]
        self.image_rotation = self.image.copy()
        self.rect = self.image_rotation.get_rect()

        self.pos = (
            uniform(
                self.sprite_groups.camera_group.background_rect.left
                + self.image.get_width(),
                self.sprite_groups.camera_group.background_rect.right
                - self.image.get_width(),
            ),
            uniform(
                self.sprite_groups.camera_group.background_rect.top
                + self.image.get_height(),
                self.sprite_groups.camera_group.background_rect.bottom
                - self.image.get_height(),
            ),
        )

        self.rect.center = self.pos
        self.direction = Vector2(self.pos)

        self.shield = Animator(
            dir_path="images/Guards/guard2",
            speed_frame=0.09,
            obj_rect=self.rect,
        )

    def rotation(self):
        rotateX = self.player.rect.centerx - self.rect.centerx
        rotateY = self.player.rect.centery - self.rect.centery
        angle_vector = -math.atan2(rotateY, rotateX) * 180 / math.pi

        if angle_vector > 0:
            self.angle = angle_vector
        else:
            self.angle = 360 + angle_vector

        for value in ENEMIES[1]["angle"]:
            if self.angle <= value:
                self.image = ENEMIES[1]["angle"][value]["sprite"]
                break

        self.image_rotation = rotozoom(self.image, self.angle, 1)
        self.rect = self.image_rotation.get_rect(center=self.rect.center)

    def random_value(self):
        self.move_count = randint(0, 600)
        self.speed = randint(0, 10)
        self.direction_list = [0, 1, -1]

    def check_move_count(self):
        if self.move_count <= 0:
            self.random_value()
        else:
            self.move_count -= 1

    def change_direction(self):
        self.moveX = choice(self.direction_list)
        self.moveY = choice(self.direction_list)

    def ckeck_position(self):
        if checks.position(self, self.sprite_groups.camera_group.background_rect):
            self.change_direction()

        if not self.is_min_distance:
            if (
                Vector2(self.rect.center).distance_to(self.player.rect.center)
                < self.min_distance
            ):
                self.is_min_distance = True
                self.change_direction()
        if (
            Vector2(self.rect.center).distance_to(self.player.rect.center)
            > self.min_distance
        ):
            self.is_min_distance = False

    def move(self):
        self.rect.move_ip(self.moveX * self.speed, self.moveY * self.speed)

    def shot(self):
        if (
            Vector2(self.rect.center).distance_to(self.player.rect.center)
            <= self.shot_distance
        ):
            if self.player.first_shot and randint(0, 100) == 50:
                self.sprite_groups.camera_group.add(
                    shot := Shots(
                        pos=self.rect.center,
                        speed=10,
                        angle=self.angle,
                        shoter=self,
                        kill_shot_distance=2000,
                        color="yellow",
                        image="images/Rockets/shot1.png",
                        scale_value=0.09,
                    )
                )
                self.sprite_groups.enemies_shot_group.add(shot)

    def update(self):
        self.ckeck_position()
        self.rotation()
        self.check_move_count()
        self.move()
        self.shield.animate(self.rect)
        self.shot()
