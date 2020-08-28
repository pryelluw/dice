from random import randint
from flask import Flask, jsonify
app = Flask(__name__)


def roll():
    return {idx: lambda a=idx: randint(1, a) for idx in range(2, 21)}[20]()


@app.route('/')
def roll_the_dice():
    return jsonify(
        {'roll': roll()}
    )


if __name__ == '__main__':
    app.run(threaded=True, port=5000)
