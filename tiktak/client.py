import pygame
import sys
import socket
from tictaktoe import TikTakToeGame


if __name__ == "__main__":
    client = socket.socket()
    hostname = socket.gethostname()
    port = 12345
    client.connect((hostname, port))
    print("Успешно подключились к серверу!")
    print("Начинаем игру!")

    WIDTH, HEIGHT = 600, 600
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Крестики-нолики(клиент)")

    game = TikTakToeGame(screen, WIDTH, HEIGHT, client, False)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                game.click(event.pos[0], event.pos[1])
        game.render()