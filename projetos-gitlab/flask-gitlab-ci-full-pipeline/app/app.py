import logging
import json
from flask import Flask, request

app = Flask(__name__)

# Configuração básica do logger
logger = logging.getLogger()
logger.setLevel(logging.INFO)

# Handler para escrever os logs em stdout
handler = logging.StreamHandler()
handler.setFormatter(logging.Formatter(
    '{"time": "%(asctime)s", "level": "%(levelname)s", "message": %(message)s}'
))
logger.addHandler(handler)

@app.route('/health-check')
def health_check():
    return "<h1>Hello From ECS! v6</h1>"

@app.route('/hello')
def hello():
    name = request.args.get("name")
    user_agent = request.headers.get("User-Agent")

    if not name:
        logger.error(json.dumps({
            "event": "hello-error",
            "url": request.url,
            "user_agent": user_agent,
            "error_message": "Nome não informado"
        }))
        return "Nome não informado", 400
    else:
        logger.info(json.dumps({
            "event": "hello-success",
            "url": request.url,
            "user_agent": user_agent,
            "nome": name
        }))
        return f"Hello, {name}!"

if __name__ == "__main__":
    #app.run(debug=True)
    app.run(host='0.0.0.0')