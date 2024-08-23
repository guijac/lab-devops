from flask import Flask
app = Flask(__name__)

class App:
    @app.route('/')
    def hello():
        return '<h1>Hello World!</h1>'

if __name__ == "__main__":
    app.run(debug=True)