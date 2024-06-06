import pygame

class Card:
    def __init__(self, name, effect, image):
        self.name = name
        self.effect = effect
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()

    def draw(self, surface, x, y):
        self.rect.topleft = (x, y)
        surface.blit(self.image, self.rect)

def draw_cards(surface, cards):
    for i, card in enumerate(cards):
        card.draw(surface, 10, i * 110 + 10)