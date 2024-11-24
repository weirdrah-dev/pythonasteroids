import pygame
from constants import * # I need to grab all the variables from the constants module
from player import Player

def main():
    pygame.init() # I am using pygame for this project and initialize it here
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    player = Player(SCREEN_WIDTH/2,SCREEN_HEIGHT/2)
    while True:
        for event in pygame.event.get(): # This is so that the exit button works on the window the program makes
            if event.type == pygame.QUIT:
                return
        screen.fill((0,0,0,0))
        player.update(dt)
        player.draw(screen)

        pygame.display.flip() # This updates the window every loop
        clock.tick(60)
        dt = clock.get_time() / 1000

if __name__ == "__main__": # Makes sure main() only runs when the file is run directly and not if imported as module
    main()