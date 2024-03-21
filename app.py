from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def hello():
    ip = request.host.split(':')[0]
    return f'Hello, Flask! Server IP: {ip}'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
