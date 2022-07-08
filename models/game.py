from unittest import result
from models.player import Player

def play_game(player_1, player_2):
    if player_1.player_move == "rock":
        if player_2.player_move == "rock":
            winning_player = None
        elif player_2.player_move == "paper":
            winning_player = player_2.player_name
        elif player_2.player_move == "scissors":
            winning_player = player_1.player_name
    elif player_1.player_move == "paper":
        if player_2.player_move == "rock":
            winning_player = player_1.player_name
        elif player_2.player_move == "paper":
            winning_player = None
        elif player_2.player_move == "scissors":
            winning_player = player_2.player_name
    elif player_1.player_move == "scissors":
        if player_2.player_move == "rock":
            winning_player = player_1.player_name
        elif player_2.player_move == "paper":
            winning_player = player_1.player_name
        elif player_2.player_move == "scissors":
            winning_player = None

    return print(f"{winning_player} wins")