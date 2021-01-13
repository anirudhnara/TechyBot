from flask import Flask, jsonify
from threading import Thread
import json

app = Flask('') 

@app.route('/')
def main():
	return "yeet"


@app.route('/api')
def api():
    with open('botstats.json', 'r') as f:
        api = json.load(f)
    
    return jsonify(api)

def run():
    app.run(host='0.0.0.0', port=8080)



def keep_alive():
    server = Thread(target=run)
    server.start()