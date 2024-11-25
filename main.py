import pygame
from constants import * # I need to grab all the variables from the constants module
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init() # I am using pygame for this project and initialize it here
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (updatable, drawable, shots)
    player = Player(SCREEN_WIDTH/2,SCREEN_HEIGHT/2)
    asteroid_field = AsteroidField()
    while True:
        for event in pygame.event.get(): # This is so that the exit button works on the window the program makes
            if event.type == pygame.QUIT:
                return
        screen.fill((0,0,0,0))
        for u in updatable:
            u.update(dt)
        for a in asteroids:
            if a.check_collision(player):
                print("Game Over!")
                return
            for s in shots:
                if a.check_collision(s):
                    a.split()
                    s.kill()
        for d in drawable:
            d.draw(screen)

        pygame.display.flip() # This updates the window every loop
        clock.tick(60)
        dt = clock.get_time() / 1000

if __name__ == "__main__": # Makes sure main() only runs when the file is run directly and not if imported as module
    main()