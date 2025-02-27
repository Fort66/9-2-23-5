from pygame.sprite import groupcollide, spritecollideany, spritecollide
from classes.class_SpriteGroups import SpriteGroups
from units.class_Explosion import Explosion
from icecream import ic
sprite_groups = SpriteGroups()



def shot_collision(self):
    if self.owner in sprite_groups.player_group:
        ic('player_shot')
    if self.owner in sprite_groups.enemies_group:
        ic('enemy_shot')

    # if (
    #     spritecollideany(self, sprite_groups.player_guard_group)
    #     and self.owner not in sprite_groups.player_group):
    # # ) or (
    # #     spritecollideany(self, sprite_groups.player_group)
    # #     and self.owner not in sprite_groups.player_group
    # # ):
    # if spritecollide(self, sprite_groups.enemies_guard_group, False) and self.owner in sprite_groups.player_group:
    #     explosion = Explosion(
    #         dir_path="images/explosions/pulsar",
    #         speed_frame=0.01,
    #         scale_value=(0.25, 0.25),
    #         loops=1,
    #         obj=self,
    #         angle=self.angle,
    #     )


# def enemies_shot_collision(self):
#     # if (
#     #     spritecollideany(self, sprite_groups.enemies_guard_group)
#     #     and self.owner not in sprite_groups.enemies_group
#     # ) or (
#     #     spritecollideany(self, sprite_groups.enemies_group)
#     #     and self.owner not in sprite_groups.enemies_group
#     # ):
#     if spritecollide(self, sprite_groups.player_guard_group, False) and self.owner in sprite_groups.enemies_group:
#         explosion = Explosion(
#             dir_path="images/explosions/rocket1_expl",
#             speed_frame=0.01,
#             scale_value=(0.5, 0.5),
#             loops=1,
#             obj=self,
#             angle=self.angle,
#         )