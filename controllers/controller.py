from flask import redirect, render_template, request, url_for
from app import app
from models.game import create_computer, play_game, play_game_from_url
from models.player import Player

@app.route('/')
def index():
    # player_1 = Player("Tom", "paper")
    # player_2 = Player("Amy", "paper")
    # play_game(player_1, player_2)
    # return render_template('index.html')
    return render_template('welcome.html')

@app.route('/<player_1_move>/<player_2_move>')
def game(player_1_move, player_2_move):
    this_game = play_game_from_url(player_1_move, player_2_move)
    return render_template('index.html', game_result=this_game)

@app.route('/welcome')
def welcome():
    return render_template('welcome.html')

@app.route('/play', methods=['POST'])
def play():
    player_name = request.form['name']
    player_move = request.form['move']
    player_submit = Player(player_name, player_move)
    computer = create_computer
    this_game = play_game(player_submit, computer)
    # play_game_with_computer(player_submit)
    return render_template('index.html', game_result=this_game)