if __name__ == "__main__":
    app.run()from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'defencesquad1'


if __name__ == "__main__":
    app.run()
