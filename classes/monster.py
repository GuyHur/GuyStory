from configuration import *
import pygame
from tkinter import *
from tkinter import messagebox

class Monster(pygame.sprite.Sprite):
    game = None
    image = None
    current_position = None
    stance = 0
    standing_image_index = 0
    attacking_image_index = 0
    lastDirection = None
    health = None

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.game = pygame
        self.pyg = pygame.Surface((64, 64))
#        self.player.fill((144, 155, 167))
        self.image = self.game.image.load(CHARACTER_LEFT_STANDING.format(pos=self.stance))
        self.rect = self.image.get_rect()
        self.rect.center = (CHARACTER_SPAWN_X, CHARACTER_SPAWN_Y)
        self.health = CHARACTER_MAX_HEALTH

    def movement(self):
        if self.stance >= 3:
            self.stance = 0
        self.stance += 1
        if self.lastDirection == 1:
            self.image = self.game.image.load(CHARACTER_LEFT_STANDING.format(pos=self.stance))
        elif self.lastDirection == 0:
            self.image = self.game.image.load(CHARACTER_RIGHT_STANDING.format(pos=self.stance))

    def move_left(self):
        self.image = self.game.image.load(CHARACTER_LEFT_WALKING.format(pos=self.standing_image_index))
        self.rect.x -= CHARACTER_MOVEMENT_PIXELS
        if self.standing_image_index >= 4:
            self.standing_image_index = 0
        self.standing_image_index += 1
        self.lastDirection = 1

    def move_right(self):
        self.image = self.game.image.load(CHARACTER_RIGHT_WALKING.format(pos=self.standing_image_index))
        self.rect.x += CHARACTER_MOVEMENT_PIXELS
        if self.standing_image_index >= 4:
            self.standing_image_index = 0
        self.standing_image_index += 1
        self.lastDirection = 0

    def die(self):
        Tk().wm_withdraw()  # to hide the main window
        messagebox.showinfo('You have died.', 'Exit')

    def attack(self):
        if self.lastDirection == 1:
            self.image = self.game.image.load(CHARACTER_LEFT_ATTACKING.format(pos=self.attacking_image_index))
        if self.lastDirection == 0:
            self.image = self.game.image.load(CHARACTER_RIGHT_ATTACKING.format(pos=self.attacking_image_index))

        if self.attacking_image_index >= 3:
            self.attacking_image_index = 0
        self.attacking_image_index += 1

    def hit(self, damage):
        self.health -= damage
        if self.health <= 0:
            self.die()











