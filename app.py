from random import randint
from flask import Flask, jsonify
app = Flask(__name__)


@app.route('/')
def roll_the_dice():
    return jsonify(
        {'roll': 
            {idx: lambda a=idx: randint(1, a) for idx in range(2, 21)}[20]()
        }
    )

if __name__ == '__main__':
    app.run(threaded=True, port=5000)