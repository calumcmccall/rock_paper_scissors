import random
from models.player import Player

winning_player = None
game_result = {
    "result": "no result yet",
    "player_one_name": "",
    "move_one": "",
    "player_two_name": "",
    "move_two": ""
}

def play_game_from_url(player_1_move, player_2_move):
    player_1 = Player("Player 1", player_1_move)
    player_2 = Player("Player 2", player_2_move)

    return play_game(player_1, player_2)

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
            winning_player = player_2.player_name
        elif player_2.player_move == "paper":
            winning_player = player_1.player_name
        elif player_2.player_move == "scissors":
            winning_player = None
    
    if winning_player != None:
        game_result["result"] = f"{winning_player} wins"
        game_result["player_one_name"] = player_1.player_name
        game_result["move_one"] = player_1.player_move
        game_result["player_two_name"] = player_2.player_name
        game_result["move_two"] = player_2.player_move
    else:
        game_result["result"] = "A draw! Nobody wins, or loses."

    return game_result

def create_computer():
    moves = ["rock", "paper", "scissors"]
    computer_move = random.choice(moves)
    computer = Player("Computer", computer_move)

    return computer