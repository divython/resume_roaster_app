@echo off
REM Git setup script for Resume Roaster

echo 🚀 Setting up Resume Roaster for GitHub...
echo GitHub Username: divython
echo Repository: https://github.com/divython/resume-roaster
echo.

REM Check if git is installed
git --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ❌ Git is not installed. Please install Git first.
    pause
    exit /b 1
)

REM Initialize git if not already initialized
if not exist ".git\" (
    echo 📦 Initializing Git repository...
    git init
) else (
    echo ✅ Git repository already initialized
)

REM Add all files (except those in .gitignore)
echo 📁 Adding files to Git...
git add .

REM Commit changes
echo 💾 Committing changes...
git commit -m "Initial commit: Resume Roaster - AI-powered resume roasting app

Features:
- Serverless Netlify functions
- Multiple roast types (Gentle, Standard, Savage, Professional)
- AI-powered improvement suggestions
- Modern responsive UI
- Built with Python, Groq API, and Netlify

Ready for deployment! 🚀"

REM Add remote origin if not already added
git remote get-url origin >nul 2>&1
if %errorlevel% neq 0 (
    echo 🔗 Adding remote origin...
    git remote add origin https://github.com/divython/resume-roaster.git
) else (
    echo ✅ Remote origin already configured
)

REM Get current branch
for /f "tokens=*" %%i in ('git branch --show-current') do set current_branch=%%i
echo 📍 Current branch: %current_branch%

REM Push to GitHub
echo 🚀 Pushing to GitHub...
echo Running: git push -u origin %current_branch%
git push -u origin %current_branch%

if %errorlevel% equ 0 (
    echo.
    echo 🎉 Successfully pushed to GitHub!
    echo 📍 Repository: https://github.com/divython/resume-roaster
    echo 🌐 Next steps:
    echo 1. Go to https://app.netlify.com
    echo 2. Connect your GitHub repository
    echo 3. Set GROQ_API_KEY in environment variables
    echo 4. Deploy!
    echo.
    echo 📚 See NETLIFY_DEPLOYMENT.md for detailed instructions
) else (
    echo ❌ Failed to push to GitHub
    echo Please make sure:
    echo 1. You have created the repository on GitHub
    echo 2. You have proper permissions
    echo 3. Your Git credentials are set up
)

pause
