import json
import os

def handler(event, context):
    """
    Ultra-simple roast function for Netlify
    Minimal dependencies to avoid import issues
    """
    
    # CORS headers
    headers = {
        'Access-Control-Allow-Origin': '*',
        'Access-Control-Allow-Headers': 'Content-Type',
        'Access-Control-Allow-Methods': 'POST, OPTIONS',
        'Content-Type': 'application/json'
    }
    
    # Handle preflight
    if event.get('httpMethod') == 'OPTIONS':
        return {
            'statusCode': 200,
            'headers': headers,
            'body': json.dumps({'message': 'CORS preflight'})
        }
    
    # Only POST
    if event.get('httpMethod') != 'POST':
        return {
            'statusCode': 405,
            'headers': headers,
            'body': json.dumps({'error': 'Method not allowed'})
        }
    
    try:
        # Parse body
        body = event.get('body', '')
        if event.get('isBase64Encoded'):
            import base64
            body = base64.b64decode(body).decode('utf-8')
        
        data = json.loads(body)
        resume_text = data.get('resume_text', '').strip()
        roast_type = data.get('roast_type', 'standard')
        
        if not resume_text:
            return {
                'statusCode': 400,
                'headers': headers,
                'body': json.dumps({'error': 'Resume text is required'})
            }
        
        # Get API key
        api_key = os.environ.get('GROQ_API_KEY')
        if not api_key:
            return {
                'statusCode': 500,
                'headers': headers,
                'body': json.dumps({'error': 'GROQ_API_KEY not configured'})
            }
        
        # Try to import and use Groq
        try:
            from groq import Groq
            
            client = Groq(api_key=api_key)
            
            # Build prompt based on roast type
            prompts = {
                'gentle': 'Please provide gentle, humorous critique of this resume with constructive feedback.',
                'savage': 'Absolutely roast this resume! Be brutally honest and hilariously harsh.',
                'professional': 'Provide professional yet humorous analysis with constructive criticism.',
                'standard': 'Roast this resume with humor and insight, pointing out flaws entertainingly.'
            }
            
            prompt = f"{prompts.get(roast_type, prompts['standard'])}\n\nResume:\n{resume_text}"
            
            response = client.chat.completions.create(
                messages=[
                    {"role": "system", "content": "You are a witty resume critic who provides humorous but constructive feedback."},
                    {"role": "user", "content": prompt}
                ],
                model="llama3-8b-8192",
                temperature=0.7,
                max_tokens=1024
            )
            
            if response.choices:
                roast_content = response.choices[0].message.content
            else:
                roast_content = "The AI seems speechless... which might say something about your resume! 😅"
            
        except ImportError:
            roast_content = f"🔥 Mock Roast ({roast_type} style):\n\nWell, well, well... someone decided to share their resume! While I can't access the AI service right now, I can tell you that any resume submitted here shows courage. That's already better than most! Your {len(resume_text)} characters of professional history await proper roasting once the AI is connected. For now, consider this a gentle warm-up! 😊"
        
        except Exception as e:
            roast_content = f"🤖 AI Hiccup Alert!\n\nThe roasting AI seems to have choked on your resume (which might be feedback in itself! 😄). Error: {str(e)}\n\nBut hey, at least the function is working! Try again, or maybe your resume is just too good to roast? 🔥"
        
        return {
            'statusCode': 200,
            'headers': headers,
            'body': json.dumps({
                'success': True,
                'roast': roast_content,
                'roast_type': roast_type
            })
        }
        
    except Exception as e:
        return {
            'statusCode': 500,
            'headers': headers,
            'body': json.dumps({'error': f'Server error: {str(e)}'})
        }
