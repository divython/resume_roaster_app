# 🚀 Netlify Deployment Guide for Resume Roaster

## Overview
This guide will help you deploy your Resume Roaster application to Netlify using serverless functions.

**Author**: divython  
**Repository**: https://github.com/divython/resume-roaster

## 📋 Prerequisites
- GitHub account
- Netlify account (free tier is sufficient)
- Groq API key

## 🔧 Setup Steps

### 1. Prepare Your Repository
1. Create a new GitHub repository or use: https://github.com/divython/resume-roaster
2. Upload all your project files to the repository
3. Make sure to exclude `.env` file (it's already in `.gitignore`)

### 2. Configure Netlify
1. Go to [Netlify](https://app.netlify.com)
2. Click "New site from Git"
3. Connect your GitHub repository
4. Configure build settings:
   - **Build command**: `pip install -r requirements.txt`
   - **Publish directory**: `public`
   - **Functions directory**: `netlify/functions`

### 3. Set Environment Variables
In Netlify dashboard → Site settings → Environment variables, add:

```
GROQ_API_KEY=your_groq_api_key_here
GROQ_MODEL=llama3-8b-8192
MODEL_TEMPERATURE=0.7
MAX_TOKENS=1024
```

### 4. Deploy
1. Click "Deploy site"
2. Wait for deployment to complete
3. Your site will be available at `https://divython-resume-roaster.netlify.app` (or your custom domain)

## 📁 Project Structure for Netlify

```
resume_roaster_app/
├── netlify/
│   └── functions/
│       ├── roast.py          # Serverless function for roasting
│       └── improve.py        # Serverless function for improvements
├── public/
│   └── index.html           # Static frontend
├── config.py                # Configuration (used by functions)
├── ai_service.py           # AI service (used by functions)
├── file_processor.py       # File processing (used by functions)
├── utils.py                # Utilities (used by functions)
├── requirements.txt        # Python dependencies
├── netlify.toml           # Netlify configuration
└── README.md              # This file
```

## 🔗 API Endpoints

Once deployed, your API endpoints will be:
- `POST /.netlify/functions/roast` - Roast resume
- `POST /.netlify/functions/improve` - Get improvement suggestions

## 📝 Usage

### Frontend (Web Interface)
1. Visit your Netlify site URL
2. Paste your resume text in the textarea
3. Select roast type (Gentle, Standard, Savage, Professional)
4. Click "Roast My Resume" or "Get Improvement Tips"

### API Usage
```javascript
// Roast resume
const response = await fetch('/.netlify/functions/roast', {
    method: 'POST',
    headers: {
        'Content-Type': 'application/json',
    },
    body: JSON.stringify({
        resume_text: "Your resume text here...",
        roast_type: "standard"
    })
});

const result = await response.json();
console.log(result.roast);
```

## 🎯 Features

### ✅ What Works on Netlify
- ✅ Text-based resume input
- ✅ Multiple roast types (Gentle, Standard, Savage, Professional)
- ✅ AI-powered improvement suggestions
- ✅ Modern, responsive UI
- ✅ Serverless functions
- ✅ CORS handling
- ✅ Error handling

### ❌ Limitations
- ❌ File upload (PDF, DOCX, TXT) - Due to serverless limitations
- ❌ File storage - Serverless functions are stateless
- ❌ Session management - Each request is independent

## 🔧 Alternative Deployment Options

If you need file upload functionality, consider these alternatives:

### Option 1: Vercel (Recommended for file uploads)
- Supports file uploads in serverless functions
- Better for Python applications
- Similar setup process

### Option 2: Railway
- Full server environment
- Supports file uploads
- Database support

### Option 3: Heroku
- Traditional hosting
- Full Flask app deployment
- File storage capabilities

## 🐛 Troubleshooting

### Common Issues

1. **Functions not working**
   - Check function logs in Netlify dashboard
   - Verify environment variables are set
   - Ensure `netlify.toml` is configured correctly

2. **API key errors**
   - Verify `GROQ_API_KEY` is set in Netlify environment variables
   - Check API key is valid and has sufficient quota

3. **Build failures**
   - Check `requirements.txt` has all dependencies
   - Verify Python version compatibility

### Debug Steps
1. Check Netlify function logs
2. Test functions locally with `netlify dev`
3. Verify environment variables
4. Check API responses in browser dev tools

## 🎨 Customization

### Adding New Roast Types
1. Update the roast type options in `public/index.html`
2. Modify the `_build_prompt` method in `ai_service.py`

### Styling Changes
- Edit the CSS in `public/index.html`
- All styles are inline for simplicity

### Adding New Features
1. Create new serverless functions in `netlify/functions/`
2. Update the frontend to call new endpoints
3. Add corresponding HTML/JS for new features

## 🚀 Going Live

1. **Custom Domain**: Configure in Netlify → Domain settings
2. **SSL**: Automatically provided by Netlify
3. **Analytics**: Enable in Netlify dashboard
4. **Performance**: Netlify provides CDN automatically

## 📊 Monitoring

- Check Netlify dashboard for:
  - Function invocations
  - Build logs
  - Site analytics
  - Error reporting

## 🔒 Security

- Environment variables are secure in Netlify
- CORS is properly configured
- Input validation is implemented
- Rate limiting can be added if needed

## 💡 Tips

1. **Development**: Use `netlify dev` for local development
2. **Testing**: Test functions individually before deployment
3. **Monitoring**: Set up Netlify notifications for build failures
4. **Scaling**: Free tier has generous limits for personal projects

## 🆘 Support

If you encounter issues:
1. Check Netlify documentation
2. Review function logs
3. Test API endpoints with tools like Postman
4. Verify environment variables are correctly set

---

Your Resume Roaster is now ready for the web! 🔥🚀
