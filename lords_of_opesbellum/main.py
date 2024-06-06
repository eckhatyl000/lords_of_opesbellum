import pygame
import sys
from board import draw_board
from piece import Piece, draw_pieces, handle_click, move_piece
from card import Card, draw_cards

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 800
FPS = 30
TILE_SIZE = SCREEN_WIDTH // 16

# Create the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Lords of Opesbellum')

# Load images
pawn_image_white = 'assets/pawn_white.png'
pawn_image_black = 'assets/pawn_black.png'

# Create pieces
pieces = []
for i in range(16):
    pieces.append(Piece('Pawn', 'White', pawn_image_white, TILE_SIZE))
    pieces.append(Piece('Pawn', 'Black', pawn_image_black, TILE_SIZE))

# Set initial positions
for i in range(16):
    pieces[i].rect.topleft = (i * TILE_SIZE, 2 * TILE_SIZE)  # White pawns
    pieces[16 + i].rect.topleft = (i * TILE_SIZE, 13 * TILE_SIZE)  # Black pawns

# Example card
cards = [Card('Move Extra', 'Move one extra piece this turn', 'assets/card_image.png')]

selected_piece = None

def handle_click(x, y):
    global selected_piece
    for piece in pieces:
        if piece.rect.collidepoint(x, y):
            selected_piece = piece
            break

def move_piece(piece, x, y):
    piece.rect.topleft = (x, y)

# Main game loop
clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if selected_piece:
                move_piece(selected_piece, event.pos[0] // TILE_SIZE * TILE_SIZE, event.pos[1] // TILE_SIZE * TILE_SIZE)
                selected_piece = None
            else:
                handle_click(event.pos[0], event.pos[1])

    draw_board(screen, TILE_SIZE)
    draw_pieces(screen, pieces)
    draw_cards(screen, cards)
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
sys.exit()