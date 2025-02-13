from pygame.sprite import Sprite
from pygame.transform import rotozoom, scale_by, flip
from pygame.image import load
from pygame.locals import MOUSEWHEEL, MOUSEBUTTONDOWN, K_a, K_w, K_d, K_s
from pygame.math import Vector2
from pygame.key import get_pressed

import math

from units.class_Shots import Shots
from config.create_Objects import screen
from logic.class_FirstShot import FirstShot

from icecream import ic

from config.sources.heroes.source import HEROES


class Player(Sprite):
    def __init__(
                self,
                pos=(0, 0),
                group=None,
                ):
        super().__init__(group)

        self.pos = pos
        self.group = group
        self.direction = Vector2(pos)
        self.angle = 0
        self.first_shot = FirstShot()
        self.speed = HEROES[1]['speed']
        self.rotation_speed = HEROES[1]['rotation_speed']
        self.__post_init__()
        self.prepare_weapons(0)
        self.group.add(self)


    def __post_init__(self):
        self.image_rotation = HEROES[1]['angle'][0]['sprite']
        self.rect = self.image_rotation.get_rect(center=self.pos)


    def prepare_weapons(self, coord):
        self.pos_weapons = []
        for value in HEROES[1]['angle'][coord]['weapons']:
            self.pos_weapons.append(value)

    @property
    def pos_weapons_rotation(self):
        result = []
        for weapon in self.pos_weapons:
            newX, newY = self.vector_rotation(weapon, -self.angle / 180 * math.pi)
            result.append([self.rect.centerx + newX, self.rect.centery + newY])
        return result


    def vector_rotation(self, vector, angle):
        vector = Vector2(vector)
        return vector.rotate_rad(angle)


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
                self.shot()


    def shot(self):
        for value in self.pos_weapons_rotation:
            self.group.add(
                            Shots(
                                pos=(value),
                                screen=screen,
                                group=self.group,
                                speed=10,
                                angle=self.angle,
                                shoter=self,
                                kill_shot_distance=2000
                                )
                            )


    def rotation(self):
        for value in HEROES[1]['angle']:
            if self.angle <= value:
                self.image = HEROES[1]['angle'][value]['sprite']
                self.prepare_weapons(value)
                break

        self.image_rotation = rotozoom(self.image, self.angle, 1)
        self.rect = self.image_rotation.get_rect(center=self.rect.center)


    def ckeck_position(self):
        if self.rect.left < self.group.background_rect.left:
            self.rect.left = self.group.background_rect.left
        if self.rect.right > self.group.background_rect.right:
            self.rect.right = self.group.background_rect.right
        if self.rect.top < self.group.background_rect.top:
            self.rect.top = self.group.background_rect.top
        if self.rect.bottom > self.group.background_rect.bottom:
            self.rect.bottom = self.group.background_rect.bottom


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

    def update(self):
        self.ckeck_position()
        self.move()

        for value in self.pos_weapons_rotation:
            value[0] += self.direction.x
            value[1] += self.direction.y

