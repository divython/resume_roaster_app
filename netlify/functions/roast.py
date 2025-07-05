import json
import os
import sys
from pathlib import Path

# Add the project root to Python path
project_root = Path(__file__).parent.parent.parent
sys.path.insert(0, str(project_root))

from file_processor import extract_text_from_file, allowed_file, sanitize_text
from ai_service import ResumeRoaster
from config import Config

def handler(event, context):
    """Netlify function handler for resume roasting."""
    
    # Handle CORS
    headers = {
        'Access-Control-Allow-Origin': '*',
        'Access-Control-Allow-Headers': 'Content-Type',
        'Access-Control-Allow-Methods': 'POST, OPTIONS',
        'Content-Type': 'application/json'
    }
    
    # Handle preflight requests
    if event.get('httpMethod') == 'OPTIONS':
        return {
            'statusCode': 200,
            'headers': headers,
            'body': json.dumps({'message': 'CORS preflight'})
        }
    
    # Only allow POST requests
    if event.get('httpMethod') != 'POST':
        return {
            'statusCode': 405,
            'headers': headers,
            'body': json.dumps({'error': 'Method not allowed'})
        }
    
    try:
        # Validate configuration
        Config.validate_config()
        
        # Parse the request body
        body = event.get('body', '')
        if event.get('isBase64Encoded'):
            import base64
            body = base64.b64decode(body).decode('utf-8')
        
        # For multipart/form-data, we need to parse it differently
        # This is a simplified version - in production, you'd use a proper multipart parser
        if 'multipart/form-data' in event.get('headers', {}).get('content-type', ''):
            return {
                'statusCode': 400,
                'headers': headers,
                'body': json.dumps({'error': 'File upload not supported in this demo. Please use the text input version.'})
            }
        
        # Parse JSON body for text input
        try:
            data = json.loads(body)
        except json.JSONDecodeError:
            return {
                'statusCode': 400,
                'headers': headers,
                'body': json.dumps({'error': 'Invalid JSON in request body'})
            }
        
        # Get resume text and roast type
        resume_text = data.get('resume_text', '').strip()
        roast_type = data.get('roast_type', 'standard')
        
        if not resume_text:
            return {
                'statusCode': 400,
                'headers': headers,
                'body': json.dumps({'error': 'Resume text is required'})
            }
        
        # Sanitize the text
        resume_text = sanitize_text(resume_text)
        
        # Initialize the roaster and generate roast
        roaster = ResumeRoaster()
        roast_output = roaster.generate_roast(resume_text, roast_type)
        
        return {
            'statusCode': 200,
            'headers': headers,
            'body': json.dumps({
                'success': True,
                'roast': roast_output,
                'roast_type': roast_type
            })
        }
        
    except ValueError as e:
        return {
            'statusCode': 400,
            'headers': headers,
            'body': json.dumps({'error': str(e)})
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'headers': headers,
            'body': json.dumps({'error': 'Internal server error'})
        }
