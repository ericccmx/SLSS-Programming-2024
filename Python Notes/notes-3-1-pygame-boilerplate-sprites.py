# Intro to Pygame
#   - boilerplate
#   - Sprite class

import pygame
import random

WHITE   = (255, 255, 255)
BLACK   = (  0,   0,   0)
EMERALD = ( 21, 219, 147)
RED     = (255,   0,   0)
GREEN   = (  0, 255,   0)
BLUE    = (  0,   0, 255)
GRAY    = (128, 128, 128)

WIDTH   = 1280    # Pixels
HEIGHT  =  720
SCREEN_SIZE = (WIDTH, HEIGHT)

class Dvdlogo(pygame.sprite.Sprite):
    """Represents the DVD Logo"""
    def __init__(self):
        super().__init__()

        self.image = pygame.image.load("./Images/dvd-logo.png")

        # sets the x and y to 0
        #   - first position of the inage is at the top left
        self.rect = self.image.get_rect()   

        self.rect.x = random.randrange(0, 1280 - self.rect.width)
        self.rect.y = random.randrange(0,720 - self.rect.height)

        # How much position changes over time
        #   - pixels per tick
        self.vel_x = random.choice([-4, -2, 2, 4])
        self.vel_y = random.choice([-4, -2, 2, 4])

    def update(self):
        # Update the position of Dvdlogo
        self.rect.x = self.rect.x + self.vel_x
        self.rect.y += self.vel_y

        # Keep the Dvdlogo in the screen

        # Right side of the screen
        #   - if the right edge of dvdlogo > WIDTH
        #       - swich the direction (+vel-x -> -vel-x)
        if self.rect.right >= WIDTH:
            self.vel_x = -self.vel_x    # or: self.vel_x *= -1

        # Left side of the screen
        if self.rect.left <= 0:
            self.vel_x *= -1
        
        # Bottom of the screen
        if self.rect.bottom >= HEIGHT:
            self.vel_y *= -1
        
        # Top of the screen
        if self.rect.top <= 0:
            self.vel_y *= -1


        print(self.rect.x, self.rect.y)

def start():
    """Environment Setup and Game Loop"""

    pygame.init()

    # --CONSTANTS--
    # COLOURS


    # --VARIABLES--
    screen = pygame.display.set_mode(SCREEN_SIZE)
    done = False
    clock = pygame.time.Clock()

    dvdlogo = Dvdlogo()
    
    # Move the DVD logo to the middle-ish
    # dvdlogo.rect.centerx = WIDTH // 2   # // always gives an integer
    # dvdlogo.rect.centery = HEIGHT // 2
    all_sprites = pygame.sprite.Group()

    for _ in range (3):
        all_sprites.add(Dvdlogo())


    pygame.display.set_caption("DVD Screen Saver")

    # --MAIN LOOP--
    while not done:
        # --- Event Listener
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
        # Listen for the keyboard to be pressed
            # spawn a new dvdlogo object
            if event.type == pygame.KEYDOWN:
                # SPACE BAR
                if pygame.key.get_pressed()[pygame.K_SPACE]:
                    all_sprites.add(Dvdlogo())
                # press 1 to increase the vel_x of all sprites
                if pygame.key.get_pressed()[pygame.K_1]:
                    # iterate over all sprites in the sprite group
                        # for each sprite, increase the velocity by 10
                    for sprite in all_sprites:
                        if sprite.vel_x > 0:
                            sprite.vel_x += 10
                        elif sprite.vel_x < 0:
                            sprite.vel_x -= 10
                # press 2 to increase the vel_y of all sprites
                if pygame.key.get_pressed()[pygame.K_2]:
                    for sprite in all_sprites:
                        if sprite.vel_y > 0:
                            sprite.vel_y += 10
                        elif sprite.vel_y < 0:
                            sprite.vel_y -= 10 

		# --- Update the world state
        all_sprites.update()

        # Take Dvdlogo and change its x-position
        #  - x-coordinate + vel_x
        # dvdlogo.rect.x = dvdlogo.rect.x + dvdlogo.vel_x

        # Take Dvdlogo and change its y-position
        #  - y-coord + vel_y
        # dvdlogo.rect.y += dvdlogo.vel_y

        # --- Draw items
        screen.fill(BLACK)

        all_sprites.draw(screen)
      
        # Update the screen with anything new
        pygame.display.flip()

        # --- Tick the Clock
        clock.tick(60)    # 60 fps


def main():
    start()

if __name__ == "__main__":
    main()