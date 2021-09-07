from flask import Flask
from threading import Thread

__all__ = (
    'keep_alive',
)

app = Flask('')

@app.route('/')
def main():
    return "I'm alive!"

def run():
    app.run('0.0.0.0', port=8080)

def keep_alive():
    server = Thread(target=run)
    server.start()

