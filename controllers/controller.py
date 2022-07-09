from flask import render_template, request
from app import app
from models.game import create_computer, play_game, play_game_from_url
from models.player import Player

@app.route('/')
def index():
    return render_template('welcome.html')

@app.route('/<player_1_move>/<player_2_move>')
def game(player_1_move, player_2_move):
    this_game = play_game_from_url(player_1_move, player_2_move)
    return render_template('index.html', game_result=this_game)

@app.route('/welcome')
def welcome():
    return render_template('welcome.html')

@app.route('/play')
def play_test():
    return render_template('play.html')

@app.route('/play', methods=['POST', 'GET'])
def play():
    player_name = request.form['name']
    player_move = request.form['move']
    player_submit = Player(player_name, player_move)
    computer = create_computer()
    this_game = play_game(player_submit, computer)
    return render_template('index.html', game_result=this_game)