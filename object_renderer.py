import pygame as pg
from settings import *
import os


class ObjectRenderer:

    def __init__(self, game):
        self.game = game
        self.screen = game.screen
        self.base_path = os.path.dirname(__file__)
        self.wall_textures = self.load_wall_textures()
        self.sky_image = self.get_texture(os.path.join(self.base_path, 'images', 'ciel.jpg'), (WIDTH, HALF_HEIGHT))
        self.sky_offset = 0

    def draw(self):
        self.draw_background()
        self.render_game_objects()

    def draw_background(self):
        self.sky_offset = (self.sky_offset + 4.5 * self.game.player.rel) % WIDTH
        self.screen.blit(self.sky_image, (-self.sky_offset, 0))
        self.screen.blit(self.sky_image, (-self.sky_offset + WIDTH, 0))

        pg.draw.rect(self.screen, FLOOR_COLOR, (0, HALF_HEIGHT, WIDTH, HEIGHT))

    def render_game_objects(self):
        list_objects = self.game.raycasting.objects_to_render
        for depth, image, pos in list_objects:
            self.screen.blit(image, pos)

    @staticmethod
    def get_texture(path, res=(TEXTURE_SIZE, TEXTURE_SIZE)):
        base_path = os.path.dirname(__file__)
        path = os.path.join(base_path, path)
        texture = pg.image.load(path).convert_alpha()
        return pg.transform.scale(texture, res)
    
    def load_wall_textures(self):
        base_path = os.path.dirname(__file__)
        return {
            1: self.get_texture(os.path.join(base_path, 'images', 'wall.jpg')),
            2: self.get_texture(os.path.join(base_path, 'images', 'wall2.png')),
        }