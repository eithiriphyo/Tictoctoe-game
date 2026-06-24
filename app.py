from flask import Flask, render_template
from flask_socketio import SocketIO, emit

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")

game_state = {"board": [""]*9, "turn": "X"}
scores = {"X": 0, "O": 0}

def check_winner(board):
    combos = [(0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6)]
    for a, b, c in combos:
        if board[a] and board[a] == board[b] == board[c]:
            return board[a]
    return None

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('make_move')
def handle_move(data):
    i = data['index']
    if game_state["board"][i] == "":
        game_state["board"][i] = game_state["turn"]
        winner = check_winner(game_state["board"])
        if winner:
            scores[winner] += 1
            emit('game_over', {"winner": winner, "scores": scores}, broadcast=True)
            game_state["board"] = [""]*9
            game_state["turn"] = "X"
        elif "" not in game_state["board"]:
            emit('game_over', {"winner": "Draw", "scores": scores}, broadcast=True)
            game_state["board"] = [""]*9
            game_state["turn"] = "X"
        else:
            game_state["turn"] = "O" if game_state["turn"] == "X" else "X"
            emit('update_board', game_state, broadcast=True)

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=5000)