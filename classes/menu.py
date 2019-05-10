from configuration import *
from classes.button import *
import pygame


class menu():
    run = None
    button = None
    game = None
    window = None
    Credits = None
    Play = None
    Settings = None



    def init(self):
        self.run = True
        self.game = pygame
        self.game.init()
        self.window = self.game.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.Credits =
    def start_menu(self):

        while self.run:
            self.game.


    def button_pressed(self):
        if






