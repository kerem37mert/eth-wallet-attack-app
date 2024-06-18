from flask import Flask
from attack import attack

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
     return str(attack("7a1b41e956dd449f9d94db7ae838faad")["status"])


if __name__ == '__main__':
    app.run()
