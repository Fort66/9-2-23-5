import pygame as pg
from pygame.transform import scale, flip
from pygame.image import load
from pygame.sprite import GroupSingle, Group

from icecream import ic

from config.create_Objects import screen
from classes.class_CheckEvents import CheckEvents
from classes.class_CameraGroup import CameraGroup
from units.class_Player import Player
from units.class_Enemies import Enemies


class Game:
    def __init__(self):
        self.run = True
        self.fps = 100
        self.screen = screen
        self.check_events = CheckEvents(self)
        self.clock = pg.time.Clock()
        self.create_groups()
        self.setup()


    def create_groups(self):
        self.camera_group = CameraGroup(self)
        self.player_group = GroupSingle()
        self.enemies_group = Group()
        self.enemies_shot = Group()
        self.player_shot = Group()

    def setup(self):
        self.player = Player(
                            pos=screen.rect.center,
                            group=self.camera_group,
                            )


        for _ in range(30):
            self.camera_group.add(
                                Enemies(
                                        group=self.camera_group,
                                        game=self,
                                        player=self.player,
                                        )
                                )


    def run_game(self):
        while self.run:
            screen.window.fill(screen.color)

            self.check_events.check_events()

            self.camera_group.update()
            self.camera_group.custom_draw(self.player)

            self.screen.update_caption(f'{str(round(self.clock.get_fps(), 2))}')
            pg.display.update()
            self.clock.tick(self.fps)