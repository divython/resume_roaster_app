from groq import Groq
import logging
from config import Config
import time

logger = logging.getLogger(__name__)

class ResumeRoaster:
    """Handle AI interactions for resume roasting."""
    
    def __init__(self):
        self.client = Groq(api_key=Config.GROQ_API_KEY)
        self.model = Config.GROQ_MODEL
        
    def generate_roast(self, resume_text, roast_type="standard"):
        """Generate a roast based on the resume text."""
        try:
            prompt = self._build_prompt(resume_text, roast_type)
            
            start_time = time.time()
            
            chat_completion = self.client.chat.completions.create(
                messages=[
                    {
                        "role": "system",
                        "content": "You are a witty and creative resume critic. Your job is to provide humorous but constructive feedback on resumes. Be clever and entertaining while pointing out areas for improvement."
                    },
                    {
                        "role": "user",
                        "content": prompt
                    }
                ],
                model=self.model,
                temperature=Config.MODEL_TEMPERATURE,
                max_tokens=Config.MAX_TOKENS,
                top_p=1,
                stop=None,
                stream=False,
            )
            
            processing_time = time.time() - start_time
            logger.info(f"Roast generated in {processing_time:.2f} seconds")
            
            if chat_completion.choices:
                return chat_completion.choices[0].message.content
            else:
                raise ValueError("No response generated from AI model")
                
        except Exception as e:
            logger.error(f"Error generating roast: {str(e)}")
            raise ValueError(f"Failed to generate roast: {str(e)}")
    
    def _build_prompt(self, resume_text, roast_type):
        """Build the prompt based on roast type."""
        
        base_prompt = f"Here's a resume to analyze:\n\n{resume_text}\n\n"
        
        if roast_type == "gentle":
            return base_prompt + """
            Please provide a gentle, humorous critique of this resume. Be witty but kind, 
            pointing out areas for improvement with a light touch. Focus on constructive 
            feedback wrapped in humor.
            """
        elif roast_type == "savage":
            return base_prompt + """
            Absolutely roast this resume! Be brutally honest, hilariously harsh, and 
            creatively savage. Point out every flaw, gap, and questionable choice. 
            Don't hold back - make it funny but devastating.
            """
        elif roast_type == "professional":
            return base_prompt + """
            Provide a professional yet humorous analysis of this resume. Balance 
            constructive criticism with witty observations. Be clever and insightful 
            while maintaining a somewhat professional tone.
            """
        else:  # standard
            return base_prompt + """
            Roast this resume with a perfect balance of humor and insight. Be funny 
            and creative while pointing out flaws and areas for improvement. Make it 
            entertaining but genuinely helpful.
            """
    
    def generate_improvement_suggestions(self, resume_text):
        """Generate constructive improvement suggestions."""
        try:
            prompt = f"""
            Please analyze this resume and provide specific, actionable improvement suggestions:

            {resume_text}

            Focus on:
            1. Content improvements (missing sections, better descriptions)
            2. Formatting and structure suggestions
            3. Skills and experience presentation
            4. Industry-specific recommendations
            5. ATS (Applicant Tracking System) optimization tips

            Provide concrete, implementable advice without being overly critical.
            """
            
            chat_completion = self.client.chat.completions.create(
                messages=[
                    {
                        "role": "system",
                        "content": "You are a professional career counselor and resume expert. Provide detailed, actionable advice to help job seekers improve their resumes."
                    },
                    {
                        "role": "user",
                        "content": prompt
                    }
                ],
                model=self.model,
                temperature=0.5,  # Lower temperature for more focused advice
                max_tokens=Config.MAX_TOKENS,
                top_p=1,
                stop=None,
                stream=False,
            )
            
            if chat_completion.choices:
                return chat_completion.choices[0].message.content
            else:
                raise ValueError("No suggestions generated from AI model")
                
        except Exception as e:
            logger.error(f"Error generating suggestions: {str(e)}")
            raise ValueError(f"Failed to generate suggestions: {str(e)}")
