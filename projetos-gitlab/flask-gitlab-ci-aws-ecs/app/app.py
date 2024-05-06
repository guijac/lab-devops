from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def health_check():
    return "<h1>Hello World! v2</h1>"

@app.route('/hello')
def hello():
    name = request.args.get("name")

    if not name:
        return "Nome não informado", 400
    else:
        return f"Hello, {name}!"

if __name__ == "__main__":
    #app.run(debug=True)
    app.run(host='0.0.0.0')