from pygame.sprite import Sprite
from pygame.transform import rotozoom
from pygame.locals import MOUSEWHEEL, MOUSEBUTTONDOWN, K_a, K_w, K_d, K_s
from pygame.math import Vector2
from pygame.key import get_pressed

import math
from time import time

from units.class_Shots import Shots
from units.class_Guardian import Guardian

from icecream import ic

from config.sources.heroes.source import HEROES

from classes.class_SpriteGroups import SpriteGroups
from config.create_Objects import checks, weapons

from functions.function_player_collision import player_collision


class Player(Sprite):
    def __init__(
        self,
        pos=(0, 0),
    ):
        self.sprite_groups = SpriteGroups()
        super().__init__(self.sprite_groups.camera_group)
        self.sprite_groups.camera_group.add(self)
        self.sprite_groups.player_group.add(self)

        self.pos = pos
        self.direction = Vector2(pos)
        self.angle = 0
        self.first_shot = False
        self.hp = 5
        self.shot_time = 1
        self.permission_shot = .25
        self.__post_init__()

    def __post_init__(self):
        self.image_rotation = HEROES[1]["angle"][0]["sprite"]
        self.rect = self.image_rotation.get_rect(center=self.pos)
        self.speed = HEROES[1]["speed"]
        self.rotation_speed = HEROES[1]["rotation_speed"]

        self.sprite_groups.camera_group.add(
            shield := Guardian(
                dir_path="images/Guards/guard1",
                speed_frame=0.09,
                obj=self,
                guard_level=10,
                loops=-1,
                angle=self.angle,
                scale_value=(1, 1),
                size=self.rect.size,
                owner=self,
            )
        )
        self.sprite_groups.player_guard_group.add(shield)

        self.prepare_weapons(0)

    def prepare_weapons(self, angle):
        weapons.load_weapons(
            obj=self, source=HEROES[1]["angle"][angle]["weapons"], angle=angle
        )

    def pos_weapons_rotation(self):
        return weapons.pos_rotation(obj=self, angle=self.angle)

    def handle_event(self, event):
        if event.type == MOUSEWHEEL:
            if event.y == -1:
                self.angle = (self.angle - self.rotation_speed) % 360
                self.rotation()
            elif event.y == 1:
                self.angle = (self.angle + self.rotation_speed) % 360
                self.rotation()

        if event.type == MOUSEBUTTONDOWN:
            if event.button == 1:
                if not self.first_shot:
                    self.first_shot = not self.first_shot
                if self.shot_time == 0:
                    self.shot_time = time()
                if time() - self.shot_time >= self.permission_shot:
                    self.shot()
                    self.shot_time = time()

    def shot(self):
        value = self.pos_weapons_rotation()
        for pos in value:
            self.sprite_groups.camera_group.add(
                shot := Shots(
                    pos=(pos),
                    speed=8,
                    angle=self.angle,
                    shoter=self,
                    kill_shot_distance=2000,
                    image="images/Rockets/shot3.png",
                    scale_value=0.2,
                    owner=self,
                )
            )
            self.sprite_groups.player_shot_group.add(shot)

    def rotation(self):
        for value in HEROES[1]["angle"]:
            if self.angle <= value:
                self.image = HEROES[1]["angle"][value]["sprite"]
                self.prepare_weapons(value)
                break

        self.image_rotation = rotozoom(self.image, self.angle, 1)
        self.rect = self.image_rotation.get_rect(center=self.rect.center)

    def check_position(self):
        checks.position(self, self.sprite_groups.camera_group.background_rect)

    def move(self):
        keys = get_pressed()
        if keys[K_a]:
            self.rect.move_ip(-self.speed, 0)
        if keys[K_d]:
            self.rect.move_ip(self.speed, 0)
        if keys[K_w]:
            self.rect.move_ip(0, -self.speed)
        if keys[K_s]:
            self.rect.move_ip(0, self.speed)

    def decrease_hp(self, value):
        if self.hp > 0:
            self.hp -= value
        if self.hp <= 0:
            self.kill()

    def update(self):
        self.check_position()
        self.move()

        player_collision()

        weapons.update_weapons(self, self.angle)
