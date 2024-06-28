from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return jsonify({"message": "Welcome to the Audio Streaming Server!"})

@app.route('/stream')
def stream():
    # Placeholder for streaming logic
    return jsonify({"message": "Streaming audio..."})

if __name__ == '__main__':
    app.run(debug=True)