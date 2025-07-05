"""
WSGI configuration for Resume Roaster application.
This file is used for production deployment with gunicorn or other WSGI servers.
"""
import os
import sys
from pathlib import Path

# Add the project directory to the Python path
project_dir = Path(__file__).parent
sys.path.insert(0, str(project_dir))

# Import the Flask application
from app import app

# Configure for production
if not os.getenv('FLASK_DEBUG'):
    app.config['DEBUG'] = False

# Application entry point
application = app

if __name__ == "__main__":
    # This is for debugging only
    app.run(debug=False)
