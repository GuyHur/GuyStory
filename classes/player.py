from configuration import *
import pygame


class Player(pygame.sprite.Sprite):
    game = None
    current_image = None
    current_position = None
    stance = 0
    standing_image_index = 0

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.game = pygame
        self.current_image = self.game.image.load(CHARACTER_LEFT_STANDING.format(pos=self.stance))
        self.current_position = (CHARACTER_SPAWN_X, CHARACTER_SPAWN_Y)

    def movement(self):
        if self.stance >= 3:
            self.stance = 0
        self.stance += 1
        self.current_image = self.game.image.load(CHARACTER_LEFT_STANDING.format(pos=self.stance))

    def move_left(self):
        self.current_image = self.game.image.load(CHARACTER_LEFT_WALKING.format(pos=self.standing_image_index))
        self.current_position = (self.current_position[0] - 10, self.current_position[1])
        if self.standing_image_index >= 4:
            self.standing_image_index = 0
        self.standing_image_index += 1

    def move_right(self):
        self.current_image = self.game.image.load(CHARACTER_RIGHT_WALKING.format(pos=self.standing_image_index))
        self.current_position = (self.current_position[0] + 10, self.current_position[1])
        if self.standing_image_index >= 4:
            self.standing_image_index = 0
        self.standing_image_index += 1



