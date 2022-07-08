from models.player import Player

winning_player = None
game_result = "no result yet"

def play_game_from_url(player_1_move, player_2_move):
    player_1 = Player("player 1", player_1_move)
    player_2 = Player("player 2", player_2_move)
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
            winning_player = player_1.player_name
        elif player_2.player_move == "paper":
            winning_player = player_1.player_name
        elif player_2.player_move == "scissors":
            winning_player = None

    print(f"{winning_player} wins")
    game_result = f"{winning_player} wins"
    return game_result