import os
import logging
from flask import Flask, request, render_template, jsonify, flash, redirect, url_for
from werkzeug.exceptions import RequestEntityTooLarge
from config import Config
from utils import setup_logging, log_request
from file_processor import extract_text_from_file, allowed_file, sanitize_text
from ai_service import ResumeRoaster

# Setup logging
logger = setup_logging()

app = Flask(__name__)
app.config.from_object(Config)

# Validate configuration
Config.validate_config()

# Initialize AI service
roaster = ResumeRoaster()

@app.errorhandler(RequestEntityTooLarge)
def handle_file_too_large(e):
    """Handle file too large error."""
    return render_template('index.html', 
                         error="File too large. Please upload a file smaller than 16MB."), 413

@app.errorhandler(Exception)
def handle_exception(e):
    """Handle general exceptions."""
    logger.error(f"Unhandled exception: {str(e)}")
    return render_template('index.html', 
                         error="An unexpected error occurred. Please try again."), 500

@app.route('/', methods=['GET', 'POST'])
@log_request
def index():
    """Main route for the resume roaster."""
    if request.method == 'GET':
        return render_template('index.html')
    
    try:
        # Validate file upload
        if 'resume' not in request.files:
            return render_template('index.html', error="No file uploaded")
        
        file = request.files['resume']
        
        if file.filename == '':
            return render_template('index.html', error="No file selected")
        
        if not allowed_file(file.filename):
            return render_template('index.html', 
                                 error="Unsupported file type. Please upload a .txt, .pdf, or .docx file.")
        
        # Extract text from file
        resume_text = extract_text_from_file(file)
        resume_text = sanitize_text(resume_text)
        
        if not resume_text:
            return render_template('index.html', error="Could not extract text from the file")
        
        # Get roast type from form
        roast_type = request.form.get('roast_type', 'standard')
        
        # Generate roast
        roast_output = roaster.generate_roast(resume_text, roast_type)
        
        logger.info(f"Successfully generated roast for file: {file.filename}")
        
        return render_template('index.html', 
                             roast_output=roast_output,
                             roast_type=roast_type,
                             success=True)
        
    except ValueError as e:
        logger.warning(f"User input error: {str(e)}")
        return render_template('index.html', error=str(e))
    except Exception as e:
        logger.error(f"Unexpected error in index route: {str(e)}")
        return render_template('index.html', error="An unexpected error occurred. Please try again.")

@app.route('/api/roast', methods=['POST'])
@log_request
def api_roast():
    """API endpoint for roasting resumes."""
    try:
        if 'resume' not in request.files:
            return jsonify({'error': 'No file uploaded'}), 400
        
        file = request.files['resume']
        
        if file.filename == '':
            return jsonify({'error': 'No file selected'}), 400
        
        if not allowed_file(file.filename):
            return jsonify({'error': 'Unsupported file type'}), 400
        
        resume_text = extract_text_from_file(file)
        resume_text = sanitize_text(resume_text)
        
        if not resume_text:
            return jsonify({'error': 'Could not extract text from the file'}), 400
        
        roast_type = request.form.get('roast_type', 'standard')
        roast_output = roaster.generate_roast(resume_text, roast_type)
        
        return jsonify({
            'roast': roast_output,
            'roast_type': roast_type,
            'success': True
        })
        
    except ValueError as e:
        return jsonify({'error': str(e)}), 400
    except Exception as e:
        logger.error(f"API error: {str(e)}")
        return jsonify({'error': 'An unexpected error occurred'}), 500

@app.route('/api/improve', methods=['POST'])
@log_request
def api_improve():
    """API endpoint for getting improvement suggestions."""
    try:
        if 'resume' not in request.files:
            return jsonify({'error': 'No file uploaded'}), 400
        
        file = request.files['resume']
        
        if file.filename == '':
            return jsonify({'error': 'No file selected'}), 400
        
        if not allowed_file(file.filename):
            return jsonify({'error': 'Unsupported file type'}), 400
        
        resume_text = extract_text_from_file(file)
        resume_text = sanitize_text(resume_text)
        
        if not resume_text:
            return jsonify({'error': 'Could not extract text from the file'}), 400
        
        suggestions = roaster.generate_improvement_suggestions(resume_text)
        
        return jsonify({
            'suggestions': suggestions,
            'success': True
        })
        
    except ValueError as e:
        return jsonify({'error': str(e)}), 400
    except Exception as e:
        logger.error(f"API error: {str(e)}")
        return jsonify({'error': 'An unexpected error occurred'}), 500

@app.route('/health')
def health_check():
    """Health check endpoint."""
    import time
    return jsonify({'status': 'healthy', 'timestamp': str(time.time())})

if __name__ == '__main__':
    app.run(debug=Config.DEBUG, host='0.0.0.0', port=int(os.getenv('PORT', 5000)))
