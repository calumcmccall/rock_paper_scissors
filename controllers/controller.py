from flask import render_template
from app import app
from models.game import play_game, result
from models.player import Player

@app.route('/')
def index():
    player_1 = Player("Tom", "paper")
    player_2 = Player("Amy", "paper")
    play_game(player_1, player_2)
    return render_template('index.html')