import pygame, time, os
from pygame.locals import *
from GuyStory import *
from configuration import *

pygame.init()

# Declaring constants
SCREENWIDTH = 800
SCREENHEIGHT = 600
FPS = 30
pygame.display.set_icon(pygame.image.load("icon.png"))  # Sets program icon
win = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT))  # Sets size of the window
pygame.display.set_caption("GuyCraft")  # Title of project

# Loading in assets, such as font and background images.
Font = pygame.font.Font("Aldrich-Regular.ttf", 30)
bg = pygame.image.load("bg.png")
title = pygame.image.load("title.png")

clock = pygame.time.Clock()


class newButton(object):  # Creates a new class for buttons
    def __init__(self, name, x, y, width, height, shift):
        self.name = name  # sets the name, so that each button can have own function
        # Sets x and y position, as well as dimensions.
        # This is for detecting collisions with mouse
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        # Hitbox to interact with mouse
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        # Loads in the default image button
        self.image = pygame.image.load("button.png")
        # Text shift to center text. Lazy Solution.
        self.textShift = shift

    def update(self, mouseX, mouseY):
        # Creates a rectangle for the mouse position.
        # This will be used to detect if the mouse is touching the button.
        mouserect = pygame.Rect(mouseX, mouseY, 10, 10)
        # If the button's hitbox is colliding with the mouse, switches to second sprite.
        if self.rect.colliderect(mouserect):
            self.image = pygame.image.load("button2.png")  # Highlighted sprite.
        else:
            self.image = pygame.image.load("button.png")  # Regular sprite, if not touching mouse.

    def click(self, mouseX, mouseY):
        # Detects the mouse pointer's rect, similar to earlier.
        # This time it will make sure when the user click, they are touching a button.
        mouserect = pygame.Rect(mouseX, mouseY, 10, 10)
        # If the button's hitbox is colliding with mouse: do function
        if self.rect.colliderect(mouserect):
            if self.name.upper() == "PLAY":  # If option is exit, then quit the program.
                os.system('python GuyStory.py')
                # Write your own function here to be used when play button pressed
            if self.name.upper() == "Credits":  # If option is exit, then quit the program.
                os.system('python credits.py')
                # Write your own function here to be used when play button pressed
            if self.name.upper() == "Settings":  # If option is exit, then quit the program.
                os.system('python settings.py')
                # Write your own function here to be used when play button pressed
            if self.name.upper() == "EXIT":  # If option is exit, then quit the program.
                pygame.quit()
                os._exit(1)


def main():  # Main function
    run = True

    buttons = [  # create an array of instances of the button class.
        newButton("Play", 300, 320, 200, 50, 70),
        newButton("Settings", 300, 380, 200, 50, 40),
        newButton("Credits", 300, 440, 200, 50, 40),
        newButton("Exit", 300, 500, 200, 50, 70)
    ]

    while run:  # run is set to true at the start. Program will keep running.
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
                # Checks to see if close button pressed, or ESC button. If so, quits program.
                pygame.quit()
                os._exit(1)
        # Creates an array, mousePos that is populated with the mouse position
        mousePos = pygame.mouse.get_pos()
        # mousePos[0] -> mouse x position
        # mousePos[1] -> mouse y position
        pressed1, pressed2, pressed3 = pygame.mouse.get_pressed()  # Creates three variables, for mouse clicks.
        if pressed1:  # If left mouse button pressed, then check if touching a button...
            for button in buttons:  # Iterate through button list
                # Check if mouse is touching each button.
                # The mouse position will be passed to the function of each button,
                # Which will execute a function if the mouse is touching it.
                button.click(mousePos[0], mousePos[1])
        # Blit the background and title to the window.
        win.blit(bg, (0, 0))
        win.blit(title, (0, 0))
        # Iterate through the button array, where the button objects are stored.
        for button in buttons:
            # Update the button, to check if it is touching mouse
            # Afterwards, for each button, blit the image to it's co-ords.
            # This uses each button's individual atributes.
            button.update(mousePos[0], mousePos[1])
            win.blit(button.image, (button.x, button.y))
            # Render some text, using the button's name attribute
            text = Font.render(button.name, 1, (255, 255, 255))
            # Blit the text to the screen, using textShift to center the text.
            win.blit(text, (button.x + button.textShift, button.y + 15))

        pygame.display.update()  # Update the display
        clock.tick(FPS)  # Keep "Game" running at 30 FPS


if __name__ == '__main__':
    main()