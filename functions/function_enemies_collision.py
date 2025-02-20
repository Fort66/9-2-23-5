from pygame.sprite import groupcollide, spritecollide
from classes.class_SpriteGroups import SpriteGroups

from icecream import ic

def enemies_collision(obj):
    sprite_groups = SpriteGroups()
    object_collide = groupcollide(sprite_groups.player_shot_group, sprite_groups.enemies_group, dokilla=True, dokillb=False)
    # if object_collide:
    #     if obj.guard_level > 0:
    #         obj.guard_level -= 1

    #     if obj.guard_level == 0:
    #         obj.kill()