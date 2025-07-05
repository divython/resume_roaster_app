import streamlit as st
import os
from groq import Groq
import PyPDF2
import docx
from io import BytesIO
import time

# Page config
st.set_page_config(
    page_title="Resume Roaster 🔥",
    page_icon="🔥",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
<style>
    .main-header {
        font-size: 3rem;
        font-weight: bold;
        text-align: center;
        background: linear-gradient(45deg, #FF6B6B, #4ECDC4);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 2rem;
    }
    .subtitle {
        text-align: center;
        font-size: 1.2rem;
        color: #666;
        margin-bottom: 2rem;
    }
    .roast-container {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 2rem;
        border-radius: 15px;
        margin: 1rem 0;
        color: white;
    }
    .improvement-container {
        background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
        padding: 2rem;
        border-radius: 15px;
        margin: 1rem 0;
        color: white;
    }
    .stButton > button {
        background: linear-gradient(45deg, #FF6B6B, #4ECDC4);
        color: white;
        border: none;
        padding: 0.5rem 2rem;
        border-radius: 25px;
        font-weight: bold;
        transition: all 0.3s;
    }
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 5px 15px rgba(0,0,0,0.2);
    }
</style>
""", unsafe_allow_html=True)

# Initialize session state
if 'resume_text' not in st.session_state:
    st.session_state.resume_text = ""
if 'roast_result' not in st.session_state:
    st.session_state.roast_result = ""
if 'improvement_result' not in st.session_state:
    st.session_state.improvement_result = ""

# Initialize Groq client
@st.cache_resource
def get_groq_client():
    api_key = os.getenv('GROQ_API_KEY')
    if not api_key:
        st.error("⚠️ GROQ_API_KEY environment variable not set!")
        st.stop()
    return Groq(api_key=api_key)

def extract_text_from_pdf(pdf_file):
    """Extract text from PDF file."""
    try:
        reader = PyPDF2.PdfReader(pdf_file)
        text = ""
        for page in reader.pages:
            text += page.extract_text() + "\n"
        return text.strip()
    except Exception as e:
        st.error(f"Error reading PDF: {str(e)}")
        return ""

def extract_text_from_docx(docx_file):
    """Extract text from DOCX file."""
    try:
        doc = docx.Document(docx_file)
        text = ""
        for paragraph in doc.paragraphs:
            text += paragraph.text + "\n"
        return text.strip()
    except Exception as e:
        st.error(f"Error reading DOCX: {str(e)}")
        return ""

def generate_roast(client, resume_text, roast_type):
    """Generate roast using Groq API."""
    prompts = {
        "gentle": f"""
        Please provide a gentle, humorous critique of this resume. Be witty but kind, 
        pointing out areas for improvement with a light touch. Focus on constructive 
        feedback wrapped in humor.
        
        Resume: {resume_text}
        """,
        "standard": f"""
        Roast this resume with a perfect balance of humor and insight. Be funny 
        and creative while pointing out flaws and areas for improvement. Make it 
        entertaining but genuinely helpful.
        
        Resume: {resume_text}
        """,
        "savage": f"""
        Absolutely roast this resume! Be brutally honest, hilariously harsh, and 
        creatively savage. Point out every flaw, gap, and questionable choice. 
        Don't hold back - make it funny but devastating.
        
        Resume: {resume_text}
        """,
        "professional": f"""
        Provide a professional yet humorous analysis of this resume. Balance 
        constructive criticism with witty observations. Be clever and insightful 
        while maintaining a somewhat professional tone.
        
        Resume: {resume_text}
        """
    }
    
    try:
        response = client.chat.completions.create(
            messages=[
                {
                    "role": "system",
                    "content": "You are a witty and creative resume critic. Your job is to provide humorous but constructive feedback on resumes."
                },
                {
                    "role": "user",
                    "content": prompts[roast_type]
                }
            ],
            model="llama3-8b-8192",
            temperature=0.7,
            max_tokens=1024,
        )
        return response.choices[0].message.content
    except Exception as e:
        st.error(f"Error generating roast: {str(e)}")
        return ""

def generate_improvements(client, resume_text):
    """Generate improvement suggestions."""
    prompt = f"""
    Please analyze this resume and provide specific, actionable improvement suggestions:

    {resume_text}

    Focus on:
    1. Content improvements (missing sections, better descriptions)
    2. Formatting and structure suggestions
    3. Skills and experience presentation
    4. Industry-specific recommendations
    5. ATS (Applicant Tracking System) optimization tips

    Provide concrete, implementable advice.
    """
    
    try:
        response = client.chat.completions.create(
            messages=[
                {
                    "role": "system",
                    "content": "You are a professional career counselor and resume expert. Provide detailed, actionable advice."
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            model="llama3-8b-8192",
            temperature=0.5,
            max_tokens=1024,
        )
        return response.choices[0].message.content
    except Exception as e:
        st.error(f"Error generating improvements: {str(e)}")
        return ""

# Main app
def main():
    # Header
    st.markdown('<div class="main-header">🔥 Resume Roaster 🔥</div>', unsafe_allow_html=True)
    st.markdown('<div class="subtitle">Upload your resume and prepare to be roasted... constructively!</div>', unsafe_allow_html=True)
    
    # Initialize client
    client = get_groq_client()
    
    # Sidebar
    st.sidebar.title("🔥 Roast Settings")
    roast_type = st.sidebar.selectbox(
        "Choose your roast level:",
        ["gentle", "standard", "savage", "professional"],
        index=1,
        help="Select how harsh you want the roast to be"
    )
    
    roast_descriptions = {
        "gentle": "😊 Kind and humorous with light criticism",
        "standard": "🔥 Balanced humor and constructive criticism",
        "savage": "💀 Brutally honest and hilariously harsh",
        "professional": "💼 Professional tone with witty observations"
    }
    
    st.sidebar.info(roast_descriptions[roast_type])
    
    # File upload section
    st.subheader("📄 Upload Your Resume")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        uploaded_file = st.file_uploader(
            "Choose a file (PDF, DOCX, or TXT)",
            type=['pdf', 'docx', 'txt'],
            help="Upload your resume in PDF, DOCX, or TXT format"
        )
    
    with col2:
        st.markdown("### Supported Formats")
        st.markdown("- 📄 PDF files")
        st.markdown("- 📝 Word documents (.docx)")
        st.markdown("- 📋 Text files (.txt)")
    
    # Process uploaded file
    if uploaded_file is not None:
        file_type = uploaded_file.type
        
        if file_type == "application/pdf":
            resume_text = extract_text_from_pdf(uploaded_file)
        elif file_type == "application/vnd.openxmlformats-officedocument.wordprocessingml.document":
            resume_text = extract_text_from_docx(uploaded_file)
        elif file_type == "text/plain":
            resume_text = str(uploaded_file.read(), "utf-8")
        else:
            st.error("Unsupported file type!")
            return
        
        st.session_state.resume_text = resume_text
        
        if resume_text:
            st.success(f"✅ Resume loaded! ({len(resume_text)} characters)")
            
            # Show preview
            with st.expander("📖 Preview Resume Text"):
                st.text_area("Resume Content", resume_text, height=200, disabled=True)
        else:
            st.error("❌ Could not extract text from the file!")
    
    # Text input as alternative
    st.subheader("✍️ Or Paste Your Resume Text")
    manual_text = st.text_area(
        "Paste your resume text here:",
        height=200,
        placeholder="Copy and paste your resume text here if you don't have a file to upload..."
    )
    
    if manual_text:
        st.session_state.resume_text = manual_text
        st.success(f"✅ Resume text loaded! ({len(manual_text)} characters)")
    
    # Action buttons
    if st.session_state.resume_text:
        col1, col2 = st.columns(2)
        
        with col1:
            if st.button("🔥 Roast My Resume!", use_container_width=True):
                with st.spinner("🔥 Roasting your resume... This might hurt!"):
                    roast_result = generate_roast(client, st.session_state.resume_text, roast_type)
                    st.session_state.roast_result = roast_result
        
        with col2:
            if st.button("💡 Get Improvement Tips", use_container_width=True):
                with st.spinner("💡 Generating improvement suggestions..."):
                    improvement_result = generate_improvements(client, st.session_state.resume_text)
                    st.session_state.improvement_result = improvement_result
    
    # Display results
    if st.session_state.roast_result:
        st.markdown('<div class="roast-container">', unsafe_allow_html=True)
        st.markdown(f"### 🔥 Your Resume Roast ({roast_type.title()} Style)")
        st.markdown(st.session_state.roast_result)
        st.markdown('</div>', unsafe_allow_html=True)
        
        if st.button("🔄 Generate New Roast"):
            st.session_state.roast_result = ""
            st.experimental_rerun()
    
    if st.session_state.improvement_result:
        st.markdown('<div class="improvement-container">', unsafe_allow_html=True)
        st.markdown("### 💡 Improvement Suggestions")
        st.markdown(st.session_state.improvement_result)
        st.markdown('</div>', unsafe_allow_html=True)
        
        if st.button("🔄 Generate New Suggestions"):
            st.session_state.improvement_result = ""
            st.experimental_rerun()
    
    # Footer
    st.markdown("---")
    st.markdown("Made with ❤️ by [divython](https://github.com/divython) | [View Source](https://github.com/divython/resume-roaster)")

if __name__ == "__main__":
    main()
