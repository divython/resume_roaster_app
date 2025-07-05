# 🚨 Netlify Deployment Troubleshooting Guide

## Common Deployment Issues and Solutions

### Issue 1: "git ref refs/heads/main does not exist"
**Problem**: Netlify can't find your main branch
**Solutions**:
1. ✅ **FIXED**: We just pushed your changes to GitHub
2. In Netlify, check that you're connecting to the correct repository
3. Make sure the branch name in Netlify matches your actual branch

### Issue 2: Python Runtime Issues
**Problem**: Netlify might not recognize Python functions
**Solutions**:
1. ✅ **FIXED**: Updated `netlify.toml` with proper Python runtime
2. ✅ **FIXED**: Created simplified function versions

### Issue 3: Import Path Issues
**Problem**: Python modules can't find each other
**Solutions**:
1. ✅ **FIXED**: Updated import paths in functions
2. ✅ **FIXED**: Added simplified standalone functions

### Issue 4: Missing Dependencies
**Problem**: Required packages not installed
**Solutions**:
1. ✅ **FIXED**: Updated `requirements.txt` with exact versions
2. All dependencies are properly specified

## 🔧 Step-by-Step Deployment Fix

### Step 1: Verify Repository Settings
1. Go to your Netlify dashboard
2. Check that the repository is: `divython/resume_roaster_app`
3. Verify the branch is set to: `main`

### Step 2: Check Build Settings
In Netlify, ensure these settings:
- **Build command**: `pip install -r requirements.txt`
- **Publish directory**: `public`
- **Functions directory**: `netlify/functions`

### Step 3: Environment Variables
Add in Netlify → Site settings → Environment variables:
- `GROQ_API_KEY` = your_groq_api_key_here

### Step 4: Redeploy
1. Go to Netlify dashboard
2. Click "Trigger deploy" → "Deploy site"
3. Watch the build logs

## 🚀 Alternative Deployment Methods

### Method 1: Manual Deploy
1. Go to Netlify dashboard
2. Click "Add new site" → "Import an existing project"
3. Choose GitHub → Select your repository
4. Configure build settings as above

### Method 2: Netlify CLI
```bash
npm install -g netlify-cli
netlify login
netlify deploy --prod
```

### Method 3: GitHub Integration
1. Connect your GitHub account to Netlify
2. Select the repository
3. Configure auto-deploy on push

## 📋 Deployment Checklist

Before redeploying, verify:
- ✅ Repository exists on GitHub
- ✅ Code is pushed to main branch
- ✅ netlify.toml is configured
- ✅ requirements.txt has all dependencies
- ✅ Public folder contains index.html
- ✅ Functions folder contains Python files
- ✅ Environment variables are set

## 🧪 Test Your Functions Locally

Test before deploying:
```bash
# Install Netlify CLI
npm install -g netlify-cli

# Test locally
netlify dev
```

## 📊 Build Log Analysis

Look for these in build logs:
- ✅ "Downloading Python dependencies"
- ✅ "Python dependencies installed"
- ✅ "Functions prepared"
- ❌ "Import errors" (check function code)
- ❌ "Module not found" (check requirements.txt)

## 🆘 Common Runtime Errors

### Error: "Unexpected token '<', '<!DOCTYPE'..." 
**Problem**: Functions returning HTML instead of JSON
**Solutions**:
1. ✅ **FIXED**: Updated netlify.toml redirects
2. ✅ **FIXED**: Corrected function paths
3. Check functions are properly deployed in Netlify dashboard

### Error: "Function not found" or 404
**Problem**: Functions not deployed or wrong paths
**Solutions**:
1. Verify functions appear in Netlify dashboard
2. Check function names match file names
3. Ensure functions directory is correct

## 🆘 If Still Failing

1. **Check build logs** in Netlify dashboard
2. **Look for specific error messages**
3. **Try the simplified functions** (roast_simple.py, improve_simple.py)
4. **Contact support** with build log details

## 📱 Alternative: Deploy to Vercel

If Netlify continues to fail:
1. Go to [Vercel](https://vercel.com)
2. Import your GitHub repository
3. Vercel has better Python support
4. Add your environment variables

## 🔗 Useful Links

- [Netlify Functions Documentation](https://docs.netlify.com/functions/overview/)
- [Netlify Python Runtime](https://docs.netlify.com/functions/lambda-compatibility/)
- [Your Repository](https://github.com/divython/resume_roaster_app)
- [Netlify Dashboard](https://app.netlify.com)

---

Your deployment should now work! 🎉
