import pygame as pg
from pygame.sprite import Sprite
from pygame.math import Vector2
from pygame.transform import rotozoom, scale_by
from pygame.image import load

from icecream import ic

from classes.class_SpriteGroups import SpriteGroups
from functions.function_shots_collision import (
    player_guard_collision,
    enemies_shot_collision,
    shots_collision,
    distance_collision
    )
from functions.function_load_source import load_json_source


class Shots(Sprite):
    def __init__(
        self,
        types=None,
        pos=(0, 0),
        size=(20, 3),
        color="white",
        speed=0, #
        angle=0,
        kill_shot_distance=None, #
        scale_value=None, #
        damage=None, #
        owner=None
    ):
        if types:
            self.source = load_json_source(
                dir_path='config/sources/rockets',
                level=types
            )
            self.image = self.source['image']
            self.speed = self.source['speed']
            self.damage = self.source['damage']
            self.scale_value = self.source['scale_value']
            self.kill_shot_distance = self.source['kill_shot_distance']
        else:
            self.scale_value = scale_value
            self.kill_shot_distance = kill_shot_distance
            self.damage = damage
            self.speed = speed

        self.sprite_groups = SpriteGroups()
        super().__init__(self.sprite_groups.camera_group)

        self.angle = angle
        self.owner = owner
        self.size = size
        self.old_shot_coordinate = Vector2(self.owner.rect.center)

        if self.image:
            self.image = scale_by(load(self.image).convert_alpha(), self.scale_value)
        else:
            self.image = pg.Surface(size, pg.SRCALPHA)
            self.image.fill(color)

        self.image_rotation = rotozoom(self.image, self.angle, 1)
        self.rect = self.image_rotation.get_rect(center=pos)
        self.offset = Vector2().rotate(self.angle)
        self.pos = Vector2(pos) + self.offset
        self.direction = Vector2(1, 0).rotate(-self.angle)

    def check_position(self):
        if (
            Vector2(self.rect.center).distance_to(self.old_shot_coordinate)
            > self.kill_shot_distance
        ):
            distance_collision(self)
            self.kill()

    def move(self):
        self.pos += self.direction * self.speed
        self.rect.center = self.pos

    def update(self):
        self.check_position()
        self.move()
        player_guard_collision(self)
        enemies_shot_collision(self)
        shots_collision()
