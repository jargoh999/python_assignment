from tic_tac_toe_games import tic_tac_toe_games
from value_in_cell import value_in_cell
from players_exception import *


class Player:
    def __init__(self, player_no: int):
        self.player_no = player_no
        self.player_signature = None
        self.set_player_signature(player_no)

    def set_player_signature(self, player_no: int) -> None:
        if player_no > 2 or player_no < 0:
            raise PlayerLimitReachedException("there can only be two players")
        elif player_no == 1:
            self.player_signature = value_in_cell.X
        if player_no == 2:
            self.player_signature = value_in_cell.O

    def get_player_signature(self):
        return self.player_signature

    def get_player_number(self):
        return self.player_no

    def play(self, my_tic_tac_toe_game: tic_tac_toe_games, row: int, column: int):
        if self.validate_cell(my_tic_tac_toe_game, row, column):
            my_tic_tac_toe_game.get_board()[row][column] = self.player_signature

    @staticmethod
    def validate_cell(my_tic_tac_toe_game: tic_tac_toe_games, row: int, column: int) -> bool:
        if my_tic_tac_toe_game.get_board()[row][column] != value_in_cell.EMPTY:
            raise TileIsOccupiedException("these tile is occupied")
        return True

    def play_with_single_number(self, my_tic_tac_toe_game: tic_tac_toe_games, tile_no: int):
        if 0 < tile_no > 9:
            raise ValueError("invalid tile position enter a number in range 1__9")

        if tile_no == 1:
            self.play(my_tic_tac_toe_game, 0, 0)
        elif tile_no == 2:
            self.play(my_tic_tac_toe_game, 0, 1)
        elif tile_no == 3:
            self.play(my_tic_tac_toe_game, 0, 2)
        elif tile_no == 4:
            self.play(my_tic_tac_toe_game, 1, 0)
        elif tile_no == 5:
            self.play(my_tic_tac_toe_game, 1, 1)
        elif tile_no == 6:
            self.play(my_tic_tac_toe_game, 1, 2)
        elif tile_no == 7:
            self.play(my_tic_tac_toe_game, 2, 0)
        elif tile_no == 8:
            self.play(my_tic_tac_toe_game, 2, 1)
        elif tile_no == 9:
            self.play(my_tic_tac_toe_game, 2, 2)


tic_tac_toe_game = tic_tac_toe_games()
player1 = Player(1)
player2 = Player(2)
player1.play_with_single_number(tic_tac_toe_game, 1)
tic_tac_toe_game.check_with_single_number(1)
player2.play_with_single_number(tic_tac_toe_game, 5)
print(tic_tac_toe_game.check_with_single_number(5))
player1.play_with_single_number(tic_tac_toe_game, 2)
tic_tac_toe_game.check_with_single_number(2)
player1.play_with_single_number(tic_tac_toe_game, 3)
print(tic_tac_toe_game.check_with_single_number(3))
tic_tac_toe_game.display_board()
