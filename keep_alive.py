from flask import Flask
from threading import Thread

app = Flask(' ')

@app.route('/')
def main():
    return "Your bot isn't not the opposite of dead."
def run():
    app.run(host = "0.0.0.0", port = 8080)
def keep_alive():
    server = thread(target = run)
    server.start()