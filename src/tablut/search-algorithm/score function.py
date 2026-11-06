# Candidate Score Function:


def dist(CHESS1, CHESS2):
    row_dist = abs(CHESS1.row - CHESS2.row)
    col_dist = abs(CHESS1.column - CHESS2.column)
    dist = row_dist + col_dist
    return dist


def score(CHESS, chess_board, role):
    score = 0
    neighbor = None
    if role == "white":
        if CHESS.king:
            for win in chess_board.Wins:
                if win.row == CHESS.row & win.column == CHESS.column:
                    return 100000  # random large number
                if win.row == CHESS.row or win.column == CHESS.column:
                    check = False
                    for piece in chess_board.Pieces:
                        if piece.row == CHESS.row or piece.column == CHESS.column:
                            check = True
                            break
                    if check == False & score >= 0:
                        score += 2
                        break
        for piece in chess_board.Pieces:
            if dist(CHESS, piece) == 1 and piece.role == "black":
                score -= 1
                neighbor = piece
            if score == -2:
                break
        # pretty random value, the best approach is probably to test experimentally.
        # For captures:
        if score == -1:
            for piece in chess_board.Pieces:
                if (
                    dist(neighbor, piece) == 1
                    and piece.role == "white"
                    and (piece.row == CHESS.row or piece.column == CHESS.column)
                ):
                    score += 3
            # again, the values should be calibrated based on experiments

    # for black:
    else:
        for piece in chess_board.Pieces:
            if dist(CHESS, piece) == 1 and piece.role == "white":
                score += 1
                neighbor = piece
            if score == +2:
                break
            for piece in chess_board.Pieces:
                if piece.row == CHESS.row or piece.column == CHESS.column:
                    check = True
                    break
                if check == False & score >= 0:
                    score -= 2
                    break
        # pretty random value, the best approach is probably to test experimentally.
        # For captures:
        if score == +1:
            for piece in chess_board.Pieces:
                if (
                    dist(neighbor, piece) == 1
                    and piece.role == "black"
                    and (piece.row == CHESS.row or piece.column == CHESS.column)
                ):
                    if neighbor.king:
                        score -= 6
                    else:
                        score -= 3
            # again, the values should be calibrated based on experiments
    return score
