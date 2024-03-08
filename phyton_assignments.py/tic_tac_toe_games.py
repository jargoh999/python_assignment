from value_in_cell import value_in_cell


class tic_tac_toe_games:
    def __init__(self):
        self.board = [[value_in_cell.EMPTY, value_in_cell.EMPTY, value_in_cell.EMPTY],
                      [value_in_cell.EMPTY, value_in_cell.EMPTY, value_in_cell.EMPTY],
                      [value_in_cell.EMPTY, value_in_cell.EMPTY, value_in_cell.EMPTY]]

    def get_board(self):
        return self.board

    def display_board(self):
        list1 = [list(x) for x in self.board]
        for list2 in list1:
            print(list2)

    def check_for_winner(self, row: int, column: int) -> bool:
        return self.check_row_for_winner(row) or self.check_column_for_winner(
            column) or self.check_diagonal_for_winner() or self.check_anti_diagonal_for_winner() is True

    def check_row_for_winner(self, row: int) -> bool:
        if self.get_board()[row][0] == self.get_board()[row][1] == self.get_board()[row][2] and self.get_board()[row][
            0] != value_in_cell.EMPTY: return True

    def check_column_for_winner(self, column: int) -> bool:
        if self.get_board()[0][column] == self.get_board()[1][column] == self.get_board()[2][column] and \
                self.get_board()[0][column] != value_in_cell.EMPTY: return True

    def check_diagonal_for_winner(self) -> bool:
        if self.get_board()[0][0] == self.get_board()[1][1] == self.get_board()[2][2] and \
                self.get_board()[0][0] != value_in_cell.EMPTY: return True

    def check_anti_diagonal_for_winner(self) -> bool:
        if self.get_board()[0][2] == self.get_board()[1][1] == self.get_board()[2][0] and \
                self.get_board()[0][2] != value_in_cell.EMPTY: return True

    def check_with_single_number(self, tile_number: int) -> bool:
        match tile_number:
            case 1:
                return self.check_for_winner(0, 0)
            case 2:
                return self.check_for_winner(0, 1)
            case 3:
                return self.check_for_winner(0, 2)
            case 4:
                return self.check_for_winner(1, 0)
            case 5:
                return self.check_for_winner(1, 1)
            case 6:
                return self.check_for_winner(1, 2)
            case 7:
                return self.check_for_winner(2, 0)
            case 8:
                return self.check_for_winner(2, 1)
            case 9:
                return self.check_for_winner(2, 2)
            case _:
                raise ValueError("invalid tile position enter a number in range 1__9")
