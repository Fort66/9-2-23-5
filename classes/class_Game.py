import pygame as pg
from icecream import ic

from config.create_Objects import screen, levels_game

from classes.class_CheckEvents import CheckEvents
from classes.class_CameraGroup import CameraGroup
from classes.class_SpriteGroups import SpriteGroups
from classes.class_BackgroundScreen import BackgroundScreen

from units.class_Player import Player
from units.class_Enemies import Enemies

from UI.screens.class_MiniMap import MiniMap

from logic.function_reset_game import reset_game
from logic.function_up_level import up_level


class Game:
    def __init__(self):
        self.run = True
        self.fps = 100
        self.screen = screen
        self.check_events = CheckEvents(self)
        self.clock = pg.time.Clock()
        self.sprite_groups = SpriteGroups()
        self.sprite_groups.camera_group = CameraGroup(self)
        self.mini_map = MiniMap(scale_value=.07, color_map=(0, 100, 0, 170))
        self.old_screen_size = self.screen.window.get_size()
        self.background_animate()
        self.setup()

    def setup(self):
        self.player = Player(pos=screen.rect.center)

        for _ in range(levels_game.enemies_attack):
            self.sprite_groups.camera_group.add(Enemies(player=self.player))

    def clear_player_groups(self):
        self.sprite_groups.player_group.empty()
        self.sprite_groups.player_shot_group.empty()
        self.sprite_groups.player_guard_group.empty()

    def clear_enemies_groups(self):
        self.sprite_groups.enemies_group.empty()
        self.sprite_groups.enemies_shot_group.empty()
        self.sprite_groups.enemies_guard_group.empty()

    def background_animate(self):
        self.back_animate = BackgroundScreen(
            dir_path='images/back_animate/1',
            speed_frame=.1,
            loops=-1,
            size=(
                self.screen.rect[2],
                self.screen.rect[3]
            ),
            no_group=True,
            owner=self.screen
        )

    def check_screen_size(self):
        if self.old_screen_size != self.screen.window.get_size():
            self.background_animate()
            self.old_screen_size = self.screen.window.get_size()

    def run_game(self):
        while self.run:
            screen.window.fill(screen.color)

            self.check_events.check_events()

            reset_game(self)
            up_level(self)

            self.check_screen_size()
            self.back_animate.update()
            self.sprite_groups.camera_group.update()
            # self.sprite_groups.camera_group.custom_draw(self.player)

            self.screen.update_caption(f"{str(round(self.clock.get_fps(), 2))}")
            pg.display.update()
            self.clock.tick(self.fps)
