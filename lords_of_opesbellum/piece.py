import pygame

class Piece:
    def __init__(self, name, color, image, tile_size):
        self.name = name
        self.color = color
        self.image = pygame.image.load(image)
        self.image = pygame.transform.scale(self.image, (tile_size, tile_size))
        self.rect = self.image.get_rect()

    def draw(self, surface):
        surface.blit(self.image, self.rect.topleft)

def draw_pieces(surface, pieces):
    for piece in pieces:
        piece.draw(surface)