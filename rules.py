def valid_move(board, orientation, row, col):
    if orientation not in {"H", "V"}:
        return False

    if orientation == "H":
        if not (0 <= row <= board.rows and 0 <= col < board.cols):
            return False

        if board.horizontal[row][col]:
            return False

        return True

    if not (0 <= row < board.rows and 0 <= col <= board.cols):
        return False

    if board.vertical[row][col]:
        return False

    return True


def completed_boxes(board, before):
    return len(board.completed - before)
