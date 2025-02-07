from encodings.utf_8_sig import encode

import pygame


class TikTakToeGame:
    def __init__(self, screen, width, height, other_player_connection, is_server):
        self.screen = screen
        self.width = width
        self.height = height
        self.cell_size = self.width // 3
        self.other_player_connection = other_player_connection
        self.is_server = is_server
        self.field = [[None for _ in range(3)] for _ in range(3)]
        self.player_1 = "X"
        self.player_2 = "O"
        self.current_player = self.player_1
        self.count_of_turns = 0
        self.connection = other_player_connection
        self.font = pygame.font.SysFont("Arial", self.cell_size)
        if self.is_server is False:
            self.render()
            self.receive_data()
            self.render()

    def render(self):
        self.screen.fill((0, 0, 0))
        for row in range(3):
            for col in range(3):
                pygame.draw.rect(
                    self.screen,
                    (255, 255, 255),
                    (row * self.cell_size, col * self.cell_size, self.cell_size, self.cell_size),
                    2
                )
                if self.field[row][col] == self.player_1:
                    text = self.font.render(self.player_1, True, (255, 0, 0))
                    self.screen.blit(text, (col * self.cell_size, row * self.cell_size))
                elif self.field[row][col] == self.player_2:
                    text = self.font.render(self.player_2, True, (0, 0, 255))
                    self.screen.blit(text, (col * self.cell_size, row * self.cell_size))
        pygame.display.update()

    def click(self, mouse_x, mouse_y):
        col = mouse_x // self.cell_size
        row = mouse_y // self.cell_size
        if self.field[row][col] is None:
            self.field[row][col] = self.current_player
            self.send_data(row, col, self.current_player)
            self.change_player()
            self.render()
            self.receive_data()
            self.render()

    def change_player(self):
        if self.current_player == self.player_1:
            self.current_player = self.player_2
        else:
            self.current_player = self.player_1

    def send_data(self, row, col, player):
        self.connection.send(f"{row} {col} {player}".encode())

    def receive_data(self):
        data = self.connection.recv(1024).decode().split()
        row = int(data[0])
        col = int(data[1])
        self.field[row][col] = data[2]
        self.current_player = data[2]
        self.change_player()

    def check_winner(self):
        pass

    def restart(self):
        pass