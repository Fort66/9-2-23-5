from pygame.sprite import groupcollide, spritecollide
from classes.class_SpriteGroups import SpriteGroups

from icecream import ic

def player_guard_collision(obj):
    sprite_groups = SpriteGroups()
    object_collide = groupcollide(sprite_groups.enemies_shot_group, sprite_groups.player_guard_group, dokilla=True, dokillb=False)
    if object_collide:
        if obj.guard_level > 0:
            obj.guard_level -= 1

        if obj.guard_level <= 0:
            obj.kill()


def enemies_guard_collision(obj):
    sprite_groups = SpriteGroups()
    object_collide = groupcollide(sprite_groups.player_shot_group, sprite_groups.enemies_guard_group, dokilla=True, dokillb=False)
    if object_collide:
        lot_hits = len(list(object_collide.values()))
        hits = list(object_collide.values())[0][0]
        if hits.guard_level > 0:
            hits.guard_level -= lot_hits

        if hits.guard_level <= 0:
            hits.kill()


def guards_collision(obj):
    sprite_groups = SpriteGroups()
    object_collide = groupcollide(sprite_groups.player_guard_group, sprite_groups.enemies_guard_group, dokilla=False, dokillb=False)
    if object_collide:
        hits_key = list(object_collide.keys())[0]
        hits_value = list(object_collide.values())[0][0]

        # hits = list(object_collide.values())[0][0]
        # if hits.guard_level > 0:
        #     hits.guard_level -= lot_hits

        # if hits.guard_level <= 0:
        #     hits.kill()
# hits_key: <Guardian Sprite(in 2 groups)>
# hits_value: <Guardian Sprite(in 2 groups)>