import pygame as pg
from icecream import ic

from config.create_Objects import screen, levels_game
from classes.class_CheckEvents import CheckEvents
from classes.class_CameraGroup import CameraGroup
from units.class_Player import Player
from units.class_Enemies import Enemies

from classes.class_SpriteGroups import SpriteGroups
from UI.screens.class_MiniMap import MiniMap


class Game:
    def __init__(self):
        self.run = True
        self.fps = 100
        self.screen = screen
        self.check_events = CheckEvents(self)
        self.clock = pg.time.Clock()
        self.sprite_groups = SpriteGroups()
        self.sprite_groups.camera_group = CameraGroup(self)
        self.mini_map = MiniMap(scale_value=.15, color_map=(0, 100, 0, 170))
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

    def run_game(self):
        while self.run:
            screen.window.fill(screen.color)

            self.check_events.check_events()

            if len(self.sprite_groups.player_group) == 0:
                self.sprite_groups.camera_group.empty()
                self.clear_player_groups()
                self.clear_enemies_groups()
                levels_game.attack_min += 1
                levels_game.current_level += 1
                levels_game.update_levels()
                self.sprite_groups.camera_group.set_background()
                self.setup()

            if len(self.sprite_groups.enemies_group) == 0:
                self.sprite_groups.camera_group.empty()
                self.clear_player_groups()
                self.clear_enemies_groups()
                levels_game.attack_min = 0
                levels_game.current_level = 1
                levels_game.update_levels()
                self.sprite_groups.camera_group.set_background()
                self.setup()

            self.sprite_groups.camera_group.update()
            self.sprite_groups.camera_group.custom_draw(self.player)

            self.screen.update_caption(f"{str(round(self.clock.get_fps(), 2))}")
            pg.display.update()
            self.clock.tick(self.fps)
