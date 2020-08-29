from flask import Flask, jsonify
from dice import Dice

app = Flask(__name__)

instructions = [
    'Roll a dice with any side count.',
    ' Use: Pass the number of sides the dice you want to roll has.',
    ' Example: dice-dice-production.herokuapp.com/20',
    ' Response: JSON',
    ' Response Data Example: {"roll": 10}'
]

HELP = ''.join(instructions)


@app.route('/')
def index():
    return jsonify({'help': HELP})


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
