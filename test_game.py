import unittest

from board import Board
from rules import valid_move, completed_boxes


class TestDotsAndBoxes(unittest.TestCase):

    def test_valid_horizontal_move(self):
        board = Board(2, 2)

        self.assertTrue(valid_move(board, "H", 0, 0))

        board.add_line("H", 0, 0)

        self.assertTrue(board.horizontal[0][0])
        self.assertFalse(valid_move(board, "H", 0, 0))

    def test_valid_vertical_move(self):
        board = Board(2, 2)

        self.assertTrue(valid_move(board, "V", 0, 0))

        board.add_line("V", 0, 0)

        self.assertTrue(board.vertical[0][0])
        self.assertFalse(valid_move(board, "V", 0, 0))

    def test_invalid_or_repeated_move(self):
        board = Board(2, 2)

        board.add_line("H", 0, 0)

        self.assertFalse(valid_move(board, "H", 0, 0))
        self.assertFalse(valid_move(board, "X", 0, 0))
        self.assertFalse(valid_move(board, "H", 99, 99))
        self.assertFalse(valid_move(board, "V", -1, 0))

    def test_completing_box_gives_one_new_box(self):
        board = Board(2, 2)

        before = set(board.completed)

        board.add_line("H", 0, 0)
        board.add_line("H", 1, 0)
        board.add_line("V", 0, 0)

        self.assertEqual(completed_boxes(board, before), 0)
        self.assertEqual(len(board.completed), 0)

        board.add_line("V", 0, 1)

        self.assertIn((0, 0), board.completed)
        self.assertEqual(completed_boxes(board, before), 1)

    def test_end_of_game_detection(self):
        board = Board(2, 2)

        self.assertFalse(board.is_complete())

        # A 2x2 board has 12 total lines.
        moves = [
            ("H", 0, 0),
            ("H", 0, 1),
            ("H", 1, 0),
            ("H", 1, 1),
            ("H", 2, 0),
            ("H", 2, 1),
            ("V", 0, 0),
            ("V", 0, 1),
            ("V", 0, 2),
            ("V", 1, 0),
            ("V", 1, 1),
            ("V", 1, 2),
        ]

        for orientation, row, col in moves:
            self.assertTrue(
                valid_move(board, orientation, row, col)
            )
            board.add_line(orientation, row, col)

        self.assertTrue(board.is_complete())
        self.assertEqual(len(board.completed), 4)


if __name__ == "__main__":
    unittest.main()