import json
import os
import sys
from pathlib import Path
import traceback

# Add the project root to Python path
project_root = Path(__file__).parent.parent.parent
sys.path.insert(0, str(project_root))

try:
    from file_processor import sanitize_text
    from ai_service import ResumeRoaster
    from config import Config
except ImportError as e:
    # Fallback for missing imports
    print(f"Import error: {e}")
    
    # Simple fallback functions
    def sanitize_text(text):
        return text.strip()[:8000] if text else ""
    
    class Config:
        @staticmethod
        def validate_config():
            if not os.getenv('GROQ_API_KEY'):
                raise ValueError("GROQ_API_KEY not found in environment variables")
    
    class ResumeRoaster:
        def __init__(self):
            from groq import Groq
            self.client = Groq(api_key=os.getenv('GROQ_API_KEY'))
        
        def generate_roast(self, resume_text, roast_type='standard'):
            prompt = f"Roast this resume with humor and creativity: {resume_text}"
            response = self.client.chat.completions.create(
                messages=[{"role": "user", "content": prompt}],
                model="llama3-8b-8192",
                temperature=0.7,
                max_tokens=1024
            )
            return response.choices[0].message.content if response.choices else "No roast generated"

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
