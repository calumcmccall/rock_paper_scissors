from flask import render_template
from app import app
from models.game import play_game, play_game_from_url
from models.player import Player

@app.route('/')
def index():
    player_1 = Player("Tom", "paper")
    player_2 = Player("Amy", "paper")
    play_game(player_1, player_2)
    return render_template('index.html')

@app.route('/<player_1_move>/<player_2_move>')
def game(player_1_move, player_2_move):
    this_game = play_game_from_url(player_1_move, player_2_move)
    print(this_game)
    return render_template('index.html', game_result=this_game)