from game.Board import board
from game.Map import game_map
from multiprocessing import Process
import time
import sys
import importlib
import os
import glob

def main():
    # TODO read sysargv, should come from rabbitMQ
    # TODO have an option to save history to local
    map_dir = sys.argv(0)
    player_a_dir = sys.argv(1)
    player_b_dir = sys.argv(2)

    # TODO needs to verify correctly formatted modules
    player_a_module = importlib.import_module(os.path.join(os.getcwd(), player_a_dir))
    player_b_module = importlib.import_module(os.path.join(os.getcwd(), player_b_dir))
    game_map = game_map(map_dir)

    # TODO need to verify player exists as part of module
    final_board = play_game(game_map, player_a.player, player_b.player)

    # TODO write out final board history and result to rabbitMQ



def play_game(game_map, player_a, player_b):
    game_board = board(game_map, build_history=True)    

    play_time = 1000

    timer = 0
    a_time = play_time
    b_time = play_time
    extra_join_time = 1000

    # TODO turn history recording on for board, turn off for copy given to players
    # TODO move timing code for moves to board
    while(game_board.getRoundNum() < 2000 and board.get_winner() is None):
        if(not game_board.get_bid_resolved()):
            bid_timeout = 5.1

            temp_board = board.get_copy()
            temp_board.set_build_history(False)
            a_bid = 0
            a_bid_process = Process(target=time_game_function, args=(player_a.bid, temp_board, a_bid, timer))
            a_bid_process.start()
            a_bid_process.join(timeout = bid_timeout + extra_join_time)

            if a_bid_process.is_alive():
                a_bid_process.terminate()
                a_bid_process.join()
                a_bid = 0

            elif (timer > bid_timeout):
                a_bid = 0

            temp_board = board.get_copy()
            temp_board.set_build_history(False)
            b_bid = 0
            b_bid_process = Process(target=time_game_function, args=(player_b.bid, temp_board, b_bid, timer))
            b_bid_process.start()
            b_bid_process.join(timeout = bid_timeout + extra_join_time)

            if b_bid_process.is_alive():
                b_bid_process.terminate()
                b_bid_process.join()
                b_bid = 0
            elif (timer > bid_timeout):
                b_bid = 0

            board.resolve_bid(bidA, bidB)

        if(board.a_turn()):
            temp_board = board.get_copy()
            temp_board.set_build_history(False)
            moves = None
            a_play_process = Process(target=time_game_function, args=(player_a.play, temp_board, moves, timer))
            a_play_process.start()
            a_play_process.join(timeout = a_time + extra_join_time)

            if a_play_process.is_alive():
                a_play_process.terminate()
                a_play_process.join()    
                board.set_winner(Result.PLAYER_B)
            elif (timer > a_time):
                board.set_winner(Result.PLAYER_B)
            else:
                valid = board.apply_turn(moves)
                if not valid:
                    board.set_winner(Result.PLAYER_B)
                a_time -= timer
        else:
            temp_board = board.get_copy()
            temp_board.set_build_history(False)
            moves = None
            b_play_process = Process(target=time_game_function, args=(player_b.play, temp_board, moves, timer))
            b_play_process.start()
            b_play_process.join(timeout = b_time + extra_join_time)

            if b_play_process.is_alive():
                b_play_process.terminate()
                b_play_process.join()    
                board.set_winner(Result.PLAYER_A)
            elif (timer > a_time):
                board.set_winner(Result.PLAYER_A)
            else:
                valid = board.apply_turn(moves)
                if not valid:
                    board.set_winner(Result.PLAYER_A)
                b_time -= timer

    if(board.get_winner() is None):
        board.tiebreak()
        if(board.get_winner() is None):
            error = 100
            if(int(a_time) > int(b_time) + error):
                board.set_winner(Result.PLAYER_A)
            elif (int(b_time) > int(a_time) + error):
                board.set_winner(Result.PLAYER_B)
            else:
                board.set_winner(Result.TIE)

    return board

    
def time_game_function(player_function, board, return_val, time_used):
    start = process_time_ns()
    return_val = player_function(board)
    stop = process_time_ns()
    time_used = stop-start


    # return 1 for a win, -1 for b win, 0 for tie

if __name__ == "__main__":
    main()