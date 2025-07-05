# Resume Roaster 🔥

A fun and interactive web application that uses AI to "roast" resumes with humor while providing constructive feedback and improvement suggestions.

## 🌐 Live Demo

**Streamlit App**: https://divython-resume-roaster.streamlit.app *(Coming Soon)*

## 🚀 **Quick Start**

```bash
# Choose your deployment option
python quick_start.py
```

## 🎯 **Deployment Options**

After testing various platforms, here are the best options:

### **🥇 Option 1: Streamlit Cloud (RECOMMENDED)**
```bash
streamlit run streamlit_app.py
```
- ✅ **FREE hosting**
- ✅ **Perfect for AI apps**
- ✅ **File uploads supported**
- ✅ **Beautiful UI**
- ✅ **Easy GitHub deployment**

### **🥈 Option 2: Docker + Railway/Render**
```bash
docker-compose --profile streamlit up
```
- ✅ **Professional deployment**
- ✅ **Full control**
- ✅ **Easy scaling**
- ✅ **Both Flask & Streamlit versions**

### **🥉 Option 3: Traditional Hosting**
```bash
python app.py
```
- ✅ **Original Flask version**
- ✅ **Full feature set**
- ✅ **Maximum flexibility**

## Features

### 🔥 Resume Roasting
- **Multiple Roast Types**: Choose from Gentle, Standard, Savage, or Professional roasting styles
- **AI-Powered Analysis**: Uses Groq's LLaMA models for creative and insightful feedback
- **Text Input**: Paste your resume text directly (optimized for Netlify serverless functions)

### 💡 Improvement Suggestions
- **Constructive Feedback**: Get actionable advice to improve your resume
- **Industry Best Practices**: Tips for better formatting, content, and ATS optimization
- **Professional Insights**: Career counselor-style recommendations

### 🎨 Modern UI/UX
- **Beautiful Design**: Modern gradient backgrounds and smooth animations
- **Responsive Layout**: Works perfectly on desktop and mobile devices
- **Interactive Elements**: Real-time feedback, tabbed results, loading indicators

### � Serverless Architecture
- **Netlify Functions**: Serverless backend functions for scalability
- **Fast Performance**: CDN-delivered static assets with serverless API
- **Cost Effective**: Pay-per-use serverless model

## 🚀 Quick Deploy to Netlify

[![Deploy to Netlify](https://www.netlify.com/img/deploy/button.svg)](https://app.netlify.com/start/deploy?repository=https://github.com/divython/resume-roaster)

### One-Click Deployment
1. Click the "Deploy to Netlify" button above
2. Connect your GitHub account
3. Fork the repository to your account
4. Set your `GROQ_API_KEY` in Netlify environment variables
5. Deploy! 🎉

### Manual Setup
```bash
# Clone the repository
git clone https://github.com/divython/resume-roaster.git
cd resume-roaster

# Install dependencies
pip install -r requirements.txt

# Set up environment variables
cp .env.example .env
# Edit .env and add your GROQ_API_KEY
```

## 📋 Manual Deployment

### Prerequisites
- GitHub account
- Netlify account (free tier is sufficient)
- Groq API key

### Steps
1. **Fork/Clone this repository**
2. **Push to your GitHub**
3. **Connect to Netlify**
4. **Set environment variables**:
   - `GROQ_API_KEY` (required)
   - `GROQ_MODEL` (optional, defaults to llama3-8b-8192)
5. **Deploy**

For detailed instructions, see [NETLIFY_DEPLOYMENT.md](NETLIFY_DEPLOYMENT.md)

## 🔧 Local Development

### Option 1: Netlify Dev (Recommended)
```bash
# Install Netlify CLI
npm install -g netlify-cli

# Install Python dependencies
pip install -r requirements.txt

# Start development server
netlify dev
```

### Option 2: Python Helper Script
```bash
# Run deployment helper
python deploy_helper.py

# Or use the launcher
python launcher.py
```

## 🏗️ Architecture

### Netlify Serverless Functions
- **Frontend**: Static HTML/CSS/JS served by Netlify CDN
- **Backend**: Python serverless functions
- **API Endpoints**:
  - `/.netlify/functions/roast` - Resume roasting
  - `/.netlify/functions/improve` - Improvement suggestions

### Project Structure
```
resume_roaster_app/
├── netlify/
│   └── functions/           # Serverless functions
│       ├── roast.py        # Resume roasting endpoint
│       └── improve.py      # Improvement suggestions
├── public/
│   └── index.html          # Static frontend
├── .github/workflows/      # GitHub Actions
├── config.py              # Configuration management
├── ai_service.py          # AI service layer
├── file_processor.py      # Text processing utilities
├── utils.py               # Utility functions
├── netlify.toml           # Netlify configuration
└── requirements.txt       # Python dependencies
```

## Supported File Formats

- **PDF**: Extracts text from PDF documents
- **TXT**: Plain text files with encoding auto-detection
- **DOCX**: Microsoft Word documents

## Roast Types

1. **Gentle Roast** 😊: Kind and humorous feedback with light criticism
2. **Standard Roast** 🔥: Balanced humor and constructive criticism
3. **Savage Roast** 💀: Brutally honest and hilariously harsh feedback
4. **Professional** 💼: Professional tone with witty observations

## Error Handling

The application includes comprehensive error handling for:
- Invalid file formats
- File size limits
- Text extraction failures
- AI API errors
- Network issues

## Logging

All application events are logged with timestamps and severity levels:
- Application logs stored in `logs/` directory
- Daily log rotation
- Console and file output

## Security Features

- File type validation
- File size limits
- Input sanitization
- Secure filename handling
- Error message sanitization

## Performance Optimizations

- Text length limiting to prevent API timeouts
- Efficient file processing
- Background task support
- Response caching ready

## Development

To run in development mode:
```bash
export FLASK_DEBUG=True
python app.py
```

For production deployment, consider using:
```bash
gunicorn -w 4 -b 0.0.0.0:5000 app:app
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## License

This project is open source and available under the MIT License.

## Support

For support, please open an issue in the GitHub repository or contact the maintainers.

---

Made with ❤️ and lots of ☕ by the Resume Roaster team!
