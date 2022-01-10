from flask import Flask


app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>This is a test for Hello, World!</p>"

if __name__ == '__main__':
    app.run()