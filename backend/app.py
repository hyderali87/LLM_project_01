import os
from flask import Flask, jsonify

# Create Flask app
app = Flask(__name__)

# Simple route
@app.route('/')
def hello():
    return "Hello, World!"

# Health check endpoint (required for Cloud Run)
@app.route('/health')
def health_check():
    return jsonify({"status": "healthy", "message": "Service is running"}), 200

# Error handler
@app.errorhandler(404)
def not_found(e):
    return jsonify({"error": "Not found"}), 404

if __name__ == '__main__':
    # Get port from environment variable or default to 8080
    port = int(os.environ.get('PORT', 8080))
    
    # Run the app with explicit host and port
    app.run(
        host='0.0.0.0',
        port=port,
        # Disable debug in production
        debug=os.environ.get('FLASK_DEBUG', 'false').lower() == 'true'
    )