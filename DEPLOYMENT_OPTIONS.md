# 🚀 Resume Roaster - Deployment Options Guide

## 🎯 **Recommended Deployment Options**

After encountering Netlify's Python limitations, here are the best alternatives:

### **🥇 Option 1: Streamlit Cloud (RECOMMENDED)**
- ✅ **Perfect for AI/ML apps**
- ✅ **Built-in file uploads**
- ✅ **Free hosting**
- ✅ **Easy GitHub integration**
- ✅ **No serverless limitations**

### **🥈 Option 2: Docker + Railway/Render**
- ✅ **Full Flask app support**
- ✅ **Professional deployment**
- ✅ **All features work**
- ✅ **Easy scaling**

### **🥉 Option 3: Heroku (Traditional)**
- ✅ **Established platform**
- ✅ **Good documentation**
- ⚠️ **No longer free**

---

## 🎨 **Option 1: Streamlit Deployment**

### **Features of Streamlit Version:**
- 🔥 Beautiful, modern UI with gradients
- 📄 File upload support (PDF, DOCX, TXT)
- ✍️ Text paste option
- 🎚️ Roast level selector
- 💡 Improvement suggestions
- 📱 Mobile responsive
- 🎨 Custom styling

### **Deploy to Streamlit Cloud:**

1. **Push Streamlit files to GitHub**:
   ```bash
   git add streamlit_app.py requirements_streamlit.txt .streamlit/
   git commit -m "Add Streamlit version"
   git push
   ```

2. **Deploy on Streamlit Cloud**:
   - Go to [share.streamlit.io](https://share.streamlit.io)
   - Connect your GitHub account
   - Select repository: `divython/resume_roaster_app`
   - Main file: `streamlit_app.py`
   - Add environment variable: `GROQ_API_KEY`

3. **Your app will be live at**:
   `https://divython-resume-roaster.streamlit.app`

### **Local Development (Streamlit)**:
```bash
# Install dependencies
pip install -r requirements_streamlit.txt

# Set environment variable
export GROQ_API_KEY="your_api_key_here"

# Run Streamlit
streamlit run streamlit_app.py
```

---

## 🐳 **Option 2: Docker Deployment**

### **Deploy to Railway (Recommended)**:

1. **Create account**: [railway.app](https://railway.app)

2. **Deploy with one click**:
   - Connect GitHub repository
   - Railway auto-detects Dockerfile
   - Add environment variable: `GROQ_API_KEY`

3. **Choose version**:
   - **Streamlit**: Uses `Dockerfile_streamlit`
   - **Flask**: Uses `Dockerfile_flask`

### **Deploy to Render**:

1. **Create account**: [render.com](https://render.com)

2. **Create new Web Service**:
   - Connect GitHub repository
   - Choose Docker
   - Dockerfile: `Dockerfile_streamlit` or `Dockerfile_flask`
   - Add environment variable: `GROQ_API_KEY`

### **Local Docker Development**:

```bash
# Streamlit version
docker build -f Dockerfile_streamlit -t resume-roaster-streamlit .
docker run -p 8501:8501 -e GROQ_API_KEY="your_key" resume-roaster-streamlit

# Flask version
docker build -f Dockerfile_flask -t resume-roaster-flask .
docker run -p 5000:5000 -e GROQ_API_KEY="your_key" resume-roaster-flask

# Using Docker Compose
docker-compose -f docker-compose-full.yml --profile streamlit up
```

---

## 🔧 **Option 3: Traditional Hosting**

### **Deploy to Heroku**:

1. **Install Heroku CLI**
2. **Create Heroku app**:
   ```bash
   heroku create divython-resume-roaster
   heroku config:set GROQ_API_KEY="your_key"
   ```

3. **Choose version**:
   - For Streamlit: Use `requirements_streamlit.txt`
   - For Flask: Use `requirements.txt`

4. **Deploy**:
   ```bash
   git push heroku main
   ```

---

## 📊 **Comparison Table**

| Platform | Cost | Ease | Features | Speed |
|----------|------|------|----------|--------|
| **Streamlit Cloud** | Free | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ |
| **Railway** | $5/month | ⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ |
| **Render** | Free tier | ⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ |
| **Heroku** | $7/month | ⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐ |

---

## 🎯 **My Recommendation**

### **For Quick Demo**: Streamlit Cloud
- Free, fast deployment
- Perfect for showcasing AI capabilities
- Beautiful UI out of the box

### **For Production**: Railway + Docker
- Professional deployment
- Full control over environment
- Easy scaling and monitoring

---

## 🚀 **Next Steps**

1. **Choose your preferred option**
2. **Follow the deployment guide above**
3. **Set your `GROQ_API_KEY` environment variable**
4. **Go live!** 🎉

**Need help?** Check the detailed guides for each option below.

---

Made with ❤️ by [divython](https://github.com/divython)
