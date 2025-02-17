import pygame as pg
from loguru import logger
from sys import exit

pg.init()


@logger.catch
def main():
    from classes.class_Game import Game

    game = Game()
    game.run_game()


if __name__ == "__main__":
    main()
    pg.quit()
    exit()
