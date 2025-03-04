from pygame.sprite import groupcollide, spritecollideany
from classes.class_SpriteGroups import SpriteGroups
from units.class_Explosion import Explosion

from icecream import ic


def enemies_collision():
    sprite_groups = SpriteGroups()
    object_collide = groupcollide(
        sprite_groups.enemies_group,
        sprite_groups.player_shot_group,
        dokilla=False,
        dokillb=True,
    )
    if object_collide:
        lot_hits = len(list(object_collide.values())[0])
        hits_damage = list(object_collide.values())[0][0].damage
        hits = list(object_collide.keys())[0]

        if hits.hp > 0:
            hits.decrease_hp(lot_hits * hits_damage)

        if hits.hp <= 0:
            explosion = Explosion(
                dir_path = 'images/explosions/ship1_expl',
                speed_frame=.12,
                scale_value=(.75, .75),
                loops=1,
                obj=hits,
                angle=hits.angle
                )
            if not explosion:
                hits.kill()
