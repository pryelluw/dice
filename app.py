from flask import Flask, jsonify
from dice import Dice

app = Flask(__name__)


@app.route('/<sides>')
def roll_the_dice(sides):
    try:
        sides = int(sides)
    except ValueError:
        return jsonify({'roll': 0}), 400

    dice = Dice(int(sides))
    return jsonify(
        {'roll': dice.roll()}
    )


if __name__ == '__main__':
    app.run(threaded=True, port=5000)
