from board import Board
from rules import valid_move, completed_boxes


class DotsAndBoxes:
    def __init__(self):
        self.board = Board()
        self.current = 0
        self.scores = [0, 0]

    def choose_board_size(self):
        print("Choose board size:")
        print("1. 2x2")
        print("2. 3x3")

        while True:
            choice = input("Enter choice (1 or 2): ").strip()

            if choice == "1":
                return 2
            elif choice == "2":
                return 3
            else:
                print("Invalid choice. Please enter 1 or 2.")

    def run(self):
        print("Dots and Boxes")

        size = self.choose_board_size()
        self.board = Board(size, size)

        print(f"Starting {size}x{size} board.")
        print("Enter moves as H row col or V row col.")
        print("Rows and columns start at 0.")
        print("Example: H 0 1")

        while not self.board.is_complete():
            self.board.display(self.scores, self.current)

            raw = input(
                f"Player {self.current + 1}, move: "
            ).strip().upper()

            parts = raw.split()

            if len(parts) != 3:
                print(
                    "Invalid command. "
                    "Use: H row col or V row col."
                )
                continue

            orientation, row, col = parts

            if orientation not in {"H", "V"}:
                print(
                    "Invalid orientation. "
                    "Use H for horizontal or V for vertical."
                )
                continue

            try:
                row = int(row)
                col = int(col)
            except ValueError:
                print(
                    "Invalid coordinates. "
                    "Row and column must be integers."
                )
                continue

            if not valid_move(self.board, orientation, row, col):

                if orientation == "H":
                    if not (
                        0 <= row <= self.board.rows
                        and 0 <= col < self.board.cols
                    ):
                        print("Invalid coordinates for this board.")
                    else:
                        print(
                            "That horizontal line "
                            "has already been used."
                        )

                else:
                    if not (
                        0 <= row < self.board.rows
                        and 0 <= col <= self.board.cols
                    ):
                        print("Invalid coordinates for this board.")
                    else:
                        print(
                            "That vertical line "
                            "has already been used."
                        )

                continue

            before = set(self.board.completed)

            self.board.add_line(orientation, row, col)

            newly_completed = completed_boxes(
                self.board, before
            )

            if newly_completed:
                self.scores[self.current] += newly_completed

                print(
                    f"Player {self.current + 1} completed "
                    f"{newly_completed} box(es) and plays again."
                )
            else:
                self.current = 1 - self.current

        self.board.display(self.scores, self.current)

        print("Game over!")

        if self.scores[0] == self.scores[1]:
            print("The game is a draw.")
        else:
            winner = 1 if self.scores[0] > self.scores[1] else 2
            print(f"Player {winner} wins!")