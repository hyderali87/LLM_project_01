from flask import Flask, jsonify, request
from flask_cors import CORS
import traceback  # Add this import

app = Flask(__name__)
CORS(app)

@app.route('/ask')
def ask():
    try:
        question = request.args.get('question', '')
        if not question:
            return jsonify({"error": "Question parameter is required"}), 400
        
        # Replace this with your actual logic
        response_text = f"Processed question: {question}"
        
        return jsonify({
            "text": response_text,
            "status": "success"
        })
    
    except Exception as e:
        app.logger.error(f"Error processing request: {str(e)}\n{traceback.format_exc()}")
        return jsonify({
            "error": "Internal server error",
            "details": str(e)
        }), 500

@app.route('/health')
def health():
    return jsonify({"status": "healthy"})

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8080))
    app.run(host='0.0.0.0', port=port)