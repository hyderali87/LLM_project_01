import os
from flask import Flask, jsonify
import signal
import sys

app = Flask(__name__)

@app.route('/')
def hello():
    return jsonify({"status": "running", "message": "LLM Backend Service"})

@app.route('/health')
def health_check():
    return jsonify({"status": "healthy"}), 200

@app.route('/ask')
def ask():
    question = request.args.get('question')
    return jsonify({  # Explicitly use jsonify
        "text": "This is the response",
        "status": "success"
    })

def handle_shutdown(signum, frame):
    print("Received shutdown signal")
    sys.exit(0)

if __name__ == '__main__':
    signal.signal(signal.SIGTERM, handle_shutdown)  # For Cloud Run shutdowns
    port = int(os.environ.get('PORT', 8080))
    app.run(host='0.0.0.0', port=port, threaded=True)