# ai/model.py
import pygame
import copy

def minimax(position, depth, max_player, game, alpha, beta):
    if depth == 0 or position.winner() is not None:
        return position.evaluate(), position
    
    if max_player:
        max_eval = float('-inf')
        best_move = None
        for move in get_all_moves(position, 'red', game):
            evaluation = minimax(move, depth - 1, False, game, alpha, beta)[0]
            max_eval = max(max_eval, evaluation)
            alpha = max(alpha, evaluation)
            if max_eval == evaluation:
                best_move = move
            if beta <= alpha:
                break
        return max_eval, best_move
    else:
        min_eval = float('inf')
        best_move = None
        for move in get_all_moves(position, 'white', game):
            evaluation = minimax(move, depth - 1, True, game, alpha, beta)[0]
            min_eval = min(min_eval, evaluation)
            beta = min(beta, evaluation)
            if min_eval == evaluation:
                best_move = move
            if beta <= alpha:
                break
        return min_eval, best_move

def simulate_move(piece, move, board, game, skip):
    board.move(piece, move[0], move[1])
    if skip:
        board.remove(skip)
    return board

def get_all_moves(board, color, game):
    moves = []

    for piece in board.get_all_pieces(color):
        valid_moves = board.get_valid_moves(piece)
        for move, skip in valid_moves.items():
            temp_board = copy.deepcopy(board)
            temp_piece = temp_board.get_piece(piece.row, piece.col)
            new_board = simulate_move(temp_piece, move, temp_board, game, skip)
            moves.append(new_board)

    return moves

def get_move_ai(game):
    value, new_board = minimax(game.board, 3, True, game, float('-inf'), float('inf'))
    return new_board
