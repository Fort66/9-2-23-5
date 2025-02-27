from pygame.sprite import groupcollide, spritecollideany
from classes.class_SpriteGroups import SpriteGroups
from units.class_Explosion import Explosion

sprite_groups = SpriteGroups()

def player_guard_collision(self):
    if (spritecollideany(self, sprite_groups.player_guard_group) and self.owner not in sprite_groups.player_group) or (spritecollideany(self, sprite_groups.player_group) and self.owner not in sprite_groups.player_group):
        explosion = Explosion(
            
        )