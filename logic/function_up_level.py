from logic.class_LevelsGame import LevelsGame

levels_game = LevelsGame()

def up_level(self):
    if len(self.sprite_groups.enemies_group) == 0:
        self.sprite_groups.camera_group.empty()
        self.clear_player_groups()
        self.clear_enemies_groups()
        levels_game.attack_min += 1
        levels_game.current_level += 1
        levels_game.update_levels()
        self.sprite_groups.camera_group.set_background()
        self.setup()