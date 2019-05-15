"""
GuyStory v1.0.0
"""
import pygame

from classes.player import Player
from configuration import *
from classes.monster import Monster


class Game(object):
    window = None
    game = None
    background = None
    game_is_running = True
    player = None
    stance_event = None
    sprites = None
    clock = None
    health_bar = None
    monster = None

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

        #Initialize the monster class
        self.monster = Monster()

        # Initialize user events
        self.stance_event = self.game.USEREVENT + 1
        self.attacking_event = self.game.USEREVENT + 2
        self.game.time.set_timer(self.stance_event, CHARACTER_STANCE_EVENT_INTERVAL)
        self.sprites = pygame.sprite.Group()
        self.sprites.add(self.player)
        self.sprites.draw(self.window)

        # Define a health bar

        # Define a clock
        self.clock = self.game.time.Clock()

        # Start game loop
        self.loop()

    def update(self):
        # Step 1, update the player
        self.sprites.update()
        self.window.blit(self.background, (DEFAULT_BACKGROUND_X, DEFAULT_BACKGROUND_Y))
        self.sprites.draw(self.window)
        pygame.draw.rect(self.window, (0, 0, 0), pygame.Rect(self.player.rect.x - 15, self.player.rect.y - 15, 100, 7))
        pygame.draw.rect(self.window, (255, 0, 0), pygame.Rect(self.player.rect.x - 15, self.player.rect.y - 15, self.player.health, 7))
        self.game.display.flip()
        self.clock.tick(30)

    def loop(self):
        while self.game_is_running:
            # Close event
            for event in self.game.event.get():
                if event.type == self.game.QUIT:
                    self.game_is_running = False

                if event.type == self.stance_event:
                    self.player.movement()

                if event.type == self.game.KEYDOWN:
                    self.player.hit(5)
                    # Check left right
                    if (event.key == self.game.K_LEFT):
                        self.player.move_left()
                    elif (event.key == self.game.K_RIGHT):
                        self.player.move_right()

            keys_pressed = self.game.key.get_pressed()

            if keys_pressed[self.game.K_LEFT]:
                self.player.move_left()

            if keys_pressed[self.game.K_RIGHT]:
                self.player.move_right()
            if keys_pressed[self.game.K_LCTRL]:
                self.player.attack()
            if keys_pressed[self.game.K_SPACE]:
                self.player.jump()

            self.update()


def main():
    guystory = Game()
    guystory.init()


if __name__ == '__main__':
    main()
