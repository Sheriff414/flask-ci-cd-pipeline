from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>🚀 Hello from Flask CI/CD Pipeline!</h1><p>Built with Docker + GitHub Actions</p>"

@app.route('/health')
def health():
    return {"status": "healthy"}, 200

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
