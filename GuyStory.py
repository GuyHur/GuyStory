"""
GuyStory v1.0.0
"""
import pygame

from classes.player import Player
from configuration import *


class Game(object):
    window = None
    game = None
    background = None
    game_is_running = True
    player = None
    stance_event = None

    def init(self):
        """
        Initializes the game
        :return:
        """
        self.game = pygame
        self.game.init()

        # Game setup
        self.window = self.game.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.game.display.set_caption(WINDOW_TITLE)

        # Draw the image background
        self.background = self.game.image.load(DEFAULT_BACKGROUND)
        self.window.blit(self.background, (DEFAULT_BACKGROUND_X, DEFAULT_BACKGROUND_Y))
        self.game.display.update()

        # Initialize the player class
        self.player = Player()

        # Initialize user events
        self.stance_event = self.game.USEREVENT + 1
        self.game.time.set_timer(self.stance_event, CHARACTER_STANCE_EVENT_INTERVAL)

        # Start game loop
        self.loop()

    def update(self):
        # Step 1, update the player
        self.window.blit(self.player.current_image, self.player.current_position)

        # Final step, update all of the information to the game
        pygame.display.update()

    def loop(self):
        while self.game_is_running:
            # Close event
            for event in self.game.event.get():
                if event.type == self.game.QUIT:
                    self.game_is_running = False
                elif event.type == self.stance_event:
                    self.player.movement()
                    self.update()
                keys = self.game.key.get_pressed()
                if keys[self.game.K_LEFT]:
                    self.player.move_left()
                    self.update()
                if keys[self.game.K_RIGHT] and Player.current_position[0] < SCREEN_WIDTH - Player.width:
                    self.player.move_right()
                    self.update()
                # if keys[self.game.K_SPACE]:
                #     self.player.jump()

            self.update()


def main():
    guystory = Game()
    guystory.init()


if __name__ == '__main__':
    main()
