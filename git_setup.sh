#!/bin/bash
# Git setup script for Resume Roaster

echo "🚀 Setting up Resume Roaster for GitHub..."
echo "GitHub Username: divython"
echo "Repository: https://github.com/divython/resume-roaster"
echo ""

# Check if git is installed
if ! command -v git &> /dev/null; then
    echo "❌ Git is not installed. Please install Git first."
    exit 1
fi

# Initialize git if not already initialized
if [ ! -d ".git" ]; then
    echo "📦 Initializing Git repository..."
    git init
else
    echo "✅ Git repository already initialized"
fi

# Add all files (except those in .gitignore)
echo "📁 Adding files to Git..."
git add .

# Check if there are any changes to commit
if git diff --cached --quiet; then
    echo "⚠️  No changes to commit"
else
    echo "💾 Committing changes..."
    git commit -m "Initial commit: Resume Roaster - AI-powered resume roasting app

Features:
- Serverless Netlify functions
- Multiple roast types (Gentle, Standard, Savage, Professional)
- AI-powered improvement suggestions
- Modern responsive UI
- Built with Python, Groq API, and Netlify

Ready for deployment! 🚀"
fi

# Add remote origin if not already added
if ! git remote get-url origin &> /dev/null; then
    echo "🔗 Adding remote origin..."
    git remote add origin https://github.com/divython/resume-roaster.git
else
    echo "✅ Remote origin already configured"
fi

# Check current branch
current_branch=$(git branch --show-current)
echo "📍 Current branch: $current_branch"

# Push to GitHub
echo "🚀 Pushing to GitHub..."
echo "Running: git push -u origin $current_branch"
git push -u origin $current_branch

if [ $? -eq 0 ]; then
    echo ""
    echo "🎉 Successfully pushed to GitHub!"
    echo "📍 Repository: https://github.com/divython/resume-roaster"
    echo "🌐 Next steps:"
    echo "1. Go to https://app.netlify.com"
    echo "2. Connect your GitHub repository"
    echo "3. Set GROQ_API_KEY in environment variables"
    echo "4. Deploy!"
    echo ""
    echo "📚 See NETLIFY_DEPLOYMENT.md for detailed instructions"
else
    echo "❌ Failed to push to GitHub"
    echo "Please make sure:"
    echo "1. You have created the repository on GitHub"
    echo "2. You have proper permissions"
    echo "3. Your Git credentials are set up"
fi
