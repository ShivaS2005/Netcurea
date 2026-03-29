import sys
import os

# Add the Backend directory to Python path
current_dir = os.path.dirname(os.path.abspath(__file__))
backend_dir = os.path.join(current_dir, 'Syed Medigrid', 'VINSUP HOSPITAL', 'Backend')
sys.path.insert(0, backend_dir)

# Change to backend directory to ensure proper imports
os.chdir(backend_dir)

# Now import the Flask app
from app import app

# Add frontend serving routes
from flask import send_from_directory

@app.route('/')
@app.route('/<path:path>')
def serve_frontend(path=None):
    frontend_dist = os.path.join(current_dir, 'Syed Medigrid', 'VINSUP HOSPITAL', 'frontend', 'dist')
    
    # If path is empty, serve index.html
    if not path:
        return send_from_directory(frontend_dist, 'index.html')
    
    # Try to serve the requested file
    try:
        return send_from_directory(frontend_dist, path)
    except:
        # If file not found, serve index.html for SPA routing
        return send_from_directory(frontend_dist, 'index.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
