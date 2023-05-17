from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return '<h1>Hello From ECS! v3</h1>'

if __name__ == "__main__":
    #app.run(debug=True)
    app.run(host='0.0.0.0')