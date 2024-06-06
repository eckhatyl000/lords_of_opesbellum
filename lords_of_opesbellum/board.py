import pygame

# Colors
LIGHT_BROWN = (238, 197, 145)
DARK_BROWN = (160, 82, 45)

def draw_board(surface, tile_size):
    for row in range(16):
        for col in range(16):
            color = LIGHT_BROWN if (row + col) % 2 == 0 else DARK_BROWN
            pygame.draw.rect(surface, color, pygame.Rect(col * tile_size, row * tile_size, tile_size, tile_size))
