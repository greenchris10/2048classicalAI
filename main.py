import pygame
import sys
import ai
import model

pygame.init()

SIZE = 4  # 4x4 board
TILE_SIZE = 100
MARGIN = 10
WIDTH = SIZE * (TILE_SIZE + MARGIN) + MARGIN
HEIGHT = WIDTH
FONT = pygame.font.Font(None, 40)
BACKGROUND_COLOR = (187, 173, 160)
TILE_COLORS = {
    0: (205, 192, 180), 2: (238, 228, 218), 4: (237, 224, 200),
    8: (242, 177, 121), 16: (245, 149, 99), 32: (246, 124, 95),
    64: (246, 94, 59), 128: (237, 207, 114), 256: (237, 204, 97),
    512: (237, 200, 80), 1024: (237, 197, 63), 2048: (237, 194, 46)
}

# Initialize screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("2048 AI")

def draw_board(board):
    screen.fill(BACKGROUND_COLOR)
    for row in range(SIZE):
        for col in range(SIZE):
            value = board.board[row][col]
            color = TILE_COLORS.get(value, (60, 58, 50))
            pygame.draw.rect(screen, color, (col * (TILE_SIZE + MARGIN) + MARGIN,
                                             row * (TILE_SIZE + MARGIN) + MARGIN,
                                             TILE_SIZE, TILE_SIZE))
            if value != 0:
                text_surface = FONT.render(str(value), True, (0, 0, 0))
                text_rect = text_surface.get_rect(center=(col * (TILE_SIZE + MARGIN) + MARGIN + TILE_SIZE // 2,
                                                           row * (TILE_SIZE + MARGIN) + MARGIN + TILE_SIZE // 2))
                screen.blit(text_surface, text_rect)
    pygame.display.flip()

# Initialize game
board = model.Board()

def game_loop():
    running = True
    clock = pygame.time.Clock()
    while running:
        clock.tick(5) 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        if len(board.available_tiles()) == 0:
            print("Game Over!")
            running = False
        else:
            move = ai.getOptimalMove(board, 3)
            board.move(move)
            board.addTile()
            print(board)

        draw_board(board)
    
    pygame.quit()
    sys.exit()

game_loop()
