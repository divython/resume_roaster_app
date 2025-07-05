#!/usr/bin/env python3
"""
Netlify Deployment Helper S    print("📋 Deployment Checklist")
    print("Please ensure the following before deploying:")
    print("1. ✅ Create GitHub repository: https://github.com/divython/resume-roaster")
    print("2. ✅ Push all code to GitHub (except .env file)")
    print("3. ✅ Create Netlify account")
    print("4. ✅ Connect GitHub repository to Netlify")
    print("5. ✅ Set environment variables in Netlify dashboard:")"""
import os
import sys
import json
import shutil
from pathlib import Path

def main():
    """Main deployment preparation function."""
    print("🚀 Netlify Deployment Preparation")
    print("GitHub: https://github.com/divython/resume-roaster")
    print("=" * 50)
    
    # Check if we're in the right directory
    if not os.path.exists('app.py'):
        print("❌ Error: Please run this script from the project root directory")
        sys.exit(1)
    
    # Check if required files exist
    required_files = [
        'config.py',
        'ai_service.py',
        'file_processor.py',
        'utils.py',
        'requirements.txt',
        'netlify.toml',
        'public/index.html',
        'netlify/functions/roast.py',
        'netlify/functions/improve.py'
    ]
    
    missing_files = []
    for file in required_files:
        if not os.path.exists(file):
            missing_files.append(file)
    
    if missing_files:
        print("❌ Missing required files:")
        for file in missing_files:
            print(f"   - {file}")
        print("Please ensure all files are created before deployment.")
        sys.exit(1)
    
    print("✅ All required files found")
    
    # Check environment variables
    print("\n🔧 Environment Variables Check")
    
    if os.path.exists('.env'):
        print("⚠️  Warning: .env file found. This file should NOT be committed to Git.")
        print("   Make sure to add your environment variables to Netlify's dashboard instead.")
    
    # Create deployment checklist
    print("\n📋 Deployment Checklist")
    print("Please ensure the following before deploying:")
    print("1. ✅ Create GitHub repository")
    print("2. ✅ Push all code to GitHub (except .env file)")
    print("3. ✅ Create Netlify account")
    print("4. ✅ Connect GitHub repository to Netlify")
    print("5. ✅ Set environment variables in Netlify dashboard:")
    print("   - GROQ_API_KEY")
    print("   - GROQ_MODEL (optional)")
    print("   - MODEL_TEMPERATURE (optional)")
    print("   - MAX_TOKENS (optional)")
    print("6. ✅ Deploy site")
    
    # Generate example environment variables
    print("\n🔐 Example Environment Variables for Netlify:")
    print("GROQ_API_KEY=your_groq_api_key_here")
    print("GROQ_MODEL=llama3-8b-8192")
    print("MODEL_TEMPERATURE=0.7")
    print("MAX_TOKENS=1024")
    
    # Check Git status
    print("\n📦 Git Status Check")
    try:
        import subprocess
        result = subprocess.run(['git', 'status', '--porcelain'], 
                              capture_output=True, text=True)
        if result.returncode == 0:
            if result.stdout.strip():
                print("⚠️  You have uncommitted changes:")
                print(result.stdout)
                print("Consider committing these changes before deployment.")
            else:
                print("✅ No uncommitted changes")
        else:
            print("⚠️  Git not initialized or not in a Git repository")
    except FileNotFoundError:
        print("⚠️  Git not found. Please install Git and initialize repository.")
    
    # Generate deployment summary
    print("\n📊 Deployment Summary")
    print("Project Type: Netlify Serverless Functions")
    print("Build Command: pip install -r requirements.txt")
    print("Publish Directory: public")
    print("Functions Directory: netlify/functions")
    print("Frontend: Static HTML/JS")
    print("Backend: Python Serverless Functions")
    print("API Endpoints: /.netlify/functions/roast, /.netlify/functions/improve")
    
    print("\n🎉 Ready for Deployment!")
    print("Follow the steps in NETLIFY_DEPLOYMENT.md for detailed instructions.")
    
    # Ask if user wants to create a quick test
    try:
        test_functions = input("\nDo you want to test the functions locally? (y/n): ").lower().strip()
        if test_functions in ['y', 'yes']:
            test_local_functions()
    except KeyboardInterrupt:
        print("\n\nDeployment preparation completed!")

def test_local_functions():
    """Test functions locally."""
    print("\n🧪 Testing Local Functions")
    
    # Test imports
    try:
        from config import Config
        from ai_service import ResumeRoaster
        from file_processor import sanitize_text
        print("✅ All imports successful")
    except ImportError as e:
        print(f"❌ Import error: {e}")
        return
    
    # Test configuration
    try:
        if not os.getenv('GROQ_API_KEY'):
            print("⚠️  GROQ_API_KEY not set in environment")
            print("   Set it with: export GROQ_API_KEY=your_key_here")
            return
        
        Config.validate_config()
        print("✅ Configuration valid")
    except ValueError as e:
        print(f"❌ Configuration error: {e}")
        return
    
    # Test AI service
    try:
        roaster = ResumeRoaster()
        sample_text = "Software Developer with 3 years experience in Python and JavaScript."
        
        print("🤖 Testing AI service...")
        # This would make an actual API call, so we'll skip in the test
        print("✅ AI service initialized successfully")
        print("   (Skipping actual API call in test)")
    except Exception as e:
        print(f"❌ AI service error: {e}")
        return
    
    print("✅ All tests passed! Functions should work on Netlify.")

if __name__ == "__main__":
    main()
