from configuration import *
import pygame


class Player(pygame.sprite.Sprite):
    game = None
    current_image = None
    current_position = None
    stance = 0
    standing_image_index = 0
    lastDirection = None
    jumping = None
    left = None
    right = None
    jumpMags = None
    width = None
    height = None
    jumpGravity = None

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.game = pygame
        self.current_image = self.game.image.load(CHARACTER_LEFT_STANDING.format(pos=self.stance))
        self.current_position = (CHARACTER_SPAWN_X, CHARACTER_SPAWN_Y)
        self.jumping = False
        self.right = False
        self.left = False
        self.jumpMags = 10
        self.width = 64
        self.height = 64
        self.jumpGravity = 10

    def movement(self):
        if self.stance >= 3:
            self.stance = 0
        self.stance += 1
        if self.lastDirection == 1:
            self.current_image = self.game.image.load(CHARACTER_LEFT_STANDING.format(pos=self.stance))
        elif self.lastDirection == 0:
            self.current_image = self.game.image.load(CHARACTER_RIGHT_STANDING.format(pos=self.stance))

    def move_left(self):
        self.current_image = self.game.image.load(CHARACTER_LEFT_WALKING.format(pos=self.standing_image_index))
        self.current_position = (self.current_position[0] - 10, self.current_position[1])
        if self.standing_image_index >= 4:
            self.standing_image_index = 0
        self.standing_image_index += 1
        self.lastDirection = 1

    def move_right(self):
        self.current_image = self.game.image.load(CHARACTER_RIGHT_WALKING.format(pos=self.standing_image_index))
        self.current_position = (self.current_position[0] + 10, self.current_position[1])
        if self.standing_image_index >= 4:
            self.standing_image_index = 0
        self.standing_image_index += 1
        self.lastDirection = 0

    def jump(self):






