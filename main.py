import pygame
import sys
from logger import log_state, log_event
from constants import *
import player as pl
import asteroid as ast
import asteroidfield as af
import shot as sh



def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) # Creating the screen.
    clock = pygame.time.Clock() # Initializing a Clock.
    dt = 0 # Date/time variable.
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    updatable = pygame.sprite.Group() # Pygame groups.
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    pl.Player.containers = (updatable, drawable) # Class containers.
    ast.Asteroid.containers = (asteroids, updatable, drawable) 
    af.AsteroidField.containers = (updatable,) 
    sh.Shot.containers = (shots, updatable, drawable)
    player = pl.Player(x = SCREEN_WIDTH / 2, y = SCREEN_HEIGHT / 2) # Player start position.
    asteroidfield = af.AsteroidField() # AsteroidField object.

    while True: # Game loop.
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return # Exit sequence for game.
        screen.fill("black") 
        updatable.update(dt) # Updating the updatable group.
        for asteroid in asteroids:
            if asteroid.collides_with(player) == True:
                log_event("player_hit")
                print("Game over!")
                sys.exit()
        for sprite in drawable:
            sprite.draw(screen) # Drawing all objects in drawable group.
        pygame.display.flip()
        dt = clock.tick(60) / 1000 # Framerate/ticks.



if __name__ == "__main__":
    main()


