import json
import os
import traceback

def handler(event, context):
    """Simple improve function for Netlify."""
    
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
        # Check for API key
        api_key = os.getenv('GROQ_API_KEY')
        if not api_key:
            return {
                'statusCode': 400,
                'headers': headers,
                'body': json.dumps({'error': 'GROQ_API_KEY not configured'})
            }
        
        # Parse the request body
        body = event.get('body', '')
        if event.get('isBase64Encoded'):
            import base64
            body = base64.b64decode(body).decode('utf-8')
        
        # Parse JSON body
        try:
            data = json.loads(body)
        except json.JSONDecodeError:
            return {
                'statusCode': 400,
                'headers': headers,
                'body': json.dumps({'error': 'Invalid JSON in request body'})
            }
        
        # Get resume text
        resume_text = data.get('resume_text', '').strip()
        
        if not resume_text:
            return {
                'statusCode': 400,
                'headers': headers,
                'body': json.dumps({'error': 'Resume text is required'})
            }
        
        # Sanitize the text
        resume_text = resume_text[:8000]  # Limit length
        
        # Import and use Groq
        try:
            from groq import Groq
            
            client = Groq(api_key=api_key)
            
            prompt = f"""Please analyze this resume and provide specific, actionable improvement suggestions:

{resume_text}

Focus on:
1. Content improvements (missing sections, better descriptions)
2. Formatting and structure suggestions
3. Skills and experience presentation
4. Industry-specific recommendations
5. ATS (Applicant Tracking System) optimization tips

Provide concrete, implementable advice."""
            
            chat_completion = client.chat.completions.create(
                messages=[
                    {
                        "role": "user",
                        "content": prompt
                    }
                ],
                model="llama3-8b-8192",
                temperature=0.5,
                max_tokens=1024,
                top_p=1,
                stop=None,
                stream=False,
            )
            
            if chat_completion.choices:
                suggestions = chat_completion.choices[0].message.content
            else:
                suggestions = "No suggestions generated. Try again!"
            
            return {
                'statusCode': 200,
                'headers': headers,
                'body': json.dumps({
                    'success': True,
                    'suggestions': suggestions
                })
            }
            
        except Exception as api_error:
            return {
                'statusCode': 500,
                'headers': headers,
                'body': json.dumps({'error': f'API Error: {str(api_error)}'})
            }
        
    except Exception as e:
        # Log the full traceback for debugging
        error_trace = traceback.format_exc()
        print(f"Function error: {error_trace}")
        
        return {
            'statusCode': 500,
            'headers': headers,
            'body': json.dumps({'error': f'Internal server error: {str(e)}'})
        }
