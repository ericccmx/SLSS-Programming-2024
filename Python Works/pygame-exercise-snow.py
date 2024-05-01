import random
import pygame as pg

# --CONSTANTS--
# COLOURS
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
EMERALD = (21, 219, 147)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
GRAY = (128, 128, 128)

WIDTH = 1280  # Pixels
HEIGHT = 720
SCREEN_SIZE = (WIDTH, HEIGHT)

class Snowflake(pg.sprite.Sprite):
    def __init__(self, size: int):
        """
        Params:
            size: diameter of snowflake in pixels
            """
        
        # Super class constructor
        super().__init__()

        # Create a blank surface
        self.image = pg.Surface((size, size))

        # Draw a circle inside of the blank surface
        pg.draw.circle(
            self.image,
            WHITE,
            (size // 2, size // 2),
            size // 2
        )

        self.rect = self.image.get_rect()

        # Spawn it in the middle of the screen
        # TODO: Choose a random x-coordinate for flake
        self.rect.centerx = random.randrange(0, WIDTH + 1)
        self.rect.centery = random.randrange(0, HEIGHT + 1)
        
    def update(self):
        """Make the snow fall from top to bottom"""
        self.vel_x = 0
        self.vel_y = random.randrange(1, 6)
        self.rect.y += self.vel_y

        if self.rect.bottom > HEIGHT:
            self.rect.y = 0

class Money(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.image = pg.image.load("./Images/money.png")

        self.image = pg.transform.scale(self.image, (self.image.get_width() // 10, self.image.get_height() // 10))

        self.rect = self.image.get_rect()   
        self.rect.centerx = random.randrange(0, WIDTH + 1)
        self.rect.centery = random.randrange(0, HEIGHT + 1)

    def update(self):
        """Make the snow fall from top to bottom"""
        self.vel_x = 0
        self.vel_y = random.randrange(1, 4)
        self.rect.y += self.vel_y

        if self.rect.bottom > HEIGHT:
            self.rect.x = random.randrange(0, WIDTH + 1)
            self.rect.y = 0

def start():
    """Environment Setup and Game Loop"""

    pg.init()

    # --Game State Variables--
    screen = pg.display.set_mode(SCREEN_SIZE)
    done = False
    clock = pg.time.Clock()

    # All sprites go in this sprite Group
    all_sprites = pg.sprite.Group()

    # Add 100 snowflake to the all_sprites Group
    for _ in range (50):
        all_sprites.add(Snowflake(10))
        all_sprites.add(Snowflake(8))
    
    for _ in range (10):
        all_sprites.add(Money())

    pg.display.set_caption("<Snowfall Landscape>")

    # --Main Loop--
    while not done:
        # --- Event Listener
        for event in pg.event.get():
            if event.type == pg.QUIT:
                done = True

        # --- Update the world state
        # Update the state of all sprites
        all_sprites .update()

        # --- Draw items
        screen.fill(BLACK)

        # Draw all the sprites
        all_sprites.draw(screen)

        # Update the screen with anything new
        pg.display.flip()

        # --- Tick the Clock
        clock.tick(60)  # 60 fps


def main():
    start()


if __name__ == "__main__":
    main()