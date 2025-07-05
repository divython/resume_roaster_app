#!/usr/bin/env python3
"""
Deployment verification script for Resume Roaster
Checks if everything is ready for Netlify deployment
"""
import os
import sys
import json
from pathlib import Path

def check_git_status():
    """Check if git is properly set up"""
    print("🔍 Checking Git Status...")
    
    if not os.path.exists('.git'):
        print("❌ Git not initialized")
        return False
    
    try:
        import subprocess
        
        # Check if we have commits
        result = subprocess.run(['git', 'log', '--oneline', '-1'], 
                              capture_output=True, text=True)
        if result.returncode != 0:
            print("❌ No commits found")
            return False
        
        # Check if we have a remote
        result = subprocess.run(['git', 'remote', 'get-url', 'origin'], 
                              capture_output=True, text=True)
        if result.returncode != 0:
            print("❌ No remote origin set")
            return False
        
        remote_url = result.stdout.strip()
        if 'divython/resume_roaster' not in remote_url:
            print(f"⚠️  Remote URL: {remote_url}")
            print("⚠️  Expected: github.com/divython/resume_roaster")
        
        # Check if we're up to date
        result = subprocess.run(['git', 'status', '--porcelain'], 
                              capture_output=True, text=True)
        if result.stdout.strip():
            print("⚠️  Uncommitted changes found")
            print("Run: git add . && git commit -m 'Update' && git push")
        else:
            print("✅ Git status clean")
        
        return True
        
    except Exception as e:
        print(f"❌ Git check failed: {e}")
        return False

def check_required_files():
    """Check if all required files exist"""
    print("\n🔍 Checking Required Files...")
    
    required_files = [
        'netlify.toml',
        'requirements.txt',
        'public/index.html',
        'netlify/functions/roast.py',
        'netlify/functions/improve.py',
        'netlify/functions/roast_simple.py',
        'netlify/functions/improve_simple.py'
    ]
    
    missing = []
    for file in required_files:
        if not os.path.exists(file):
            missing.append(file)
    
    if missing:
        print(f"❌ Missing files: {missing}")
        return False
    else:
        print("✅ All required files present")
        return True

def check_netlify_toml():
    """Check netlify.toml configuration"""
    print("\n🔍 Checking netlify.toml...")
    
    if not os.path.exists('netlify.toml'):
        print("❌ netlify.toml not found")
        return False
    
    try:
        with open('netlify.toml', 'r') as f:
            content = f.read()
        
        required_sections = [
            '[build]',
            'command = "pip install -r requirements.txt"',
            'functions = "netlify/functions"',
            'publish = "public"'
        ]
        
        for section in required_sections:
            if section not in content:
                print(f"❌ Missing in netlify.toml: {section}")
                return False
        
        print("✅ netlify.toml properly configured")
        return True
        
    except Exception as e:
        print(f"❌ Error reading netlify.toml: {e}")
        return False

def check_functions():
    """Check if functions are properly structured"""
    print("\n🔍 Checking Functions...")
    
    functions_dir = Path('netlify/functions')
    if not functions_dir.exists():
        print("❌ Functions directory not found")
        return False
    
    python_files = list(functions_dir.glob('*.py'))
    if not python_files:
        print("❌ No Python functions found")
        return False
    
    print(f"✅ Found {len(python_files)} Python functions")
    
    # Check if functions have handler
    for func_file in python_files:
        try:
            with open(func_file, 'r') as f:
                content = f.read()
            
            if 'def handler(' not in content:
                print(f"⚠️  {func_file.name} missing handler function")
            else:
                print(f"✅ {func_file.name} has handler function")
                
        except Exception as e:
            print(f"❌ Error reading {func_file.name}: {e}")
    
    return True

def check_requirements():
    """Check requirements.txt"""
    print("\n🔍 Checking requirements.txt...")
    
    if not os.path.exists('requirements.txt'):
        print("❌ requirements.txt not found")
        return False
    
    try:
        with open('requirements.txt', 'r') as f:
            requirements = f.read().strip().split('\n')
        
        required_packages = ['groq', 'python-dotenv']
        
        for package in required_packages:
            if not any(package in req for req in requirements):
                print(f"❌ Missing package: {package}")
                return False
        
        print(f"✅ requirements.txt has {len(requirements)} packages")
        return True
        
    except Exception as e:
        print(f"❌ Error reading requirements.txt: {e}")
        return False

def main():
    """Main verification function"""
    print("🔥 Resume Roaster - Deployment Verification")
    print("=" * 50)
    
    checks = [
        check_git_status,
        check_required_files,
        check_netlify_toml,
        check_functions,
        check_requirements
    ]
    
    results = []
    for check in checks:
        try:
            result = check()
            results.append(result)
        except Exception as e:
            print(f"❌ Check failed: {e}")
            results.append(False)
    
    print(f"\n📊 Results: {sum(results)}/{len(results)} checks passed")
    
    if all(results):
        print("\n🎉 All checks passed! Ready for deployment!")
        print("\n🚀 Next steps:")
        print("1. Go to https://app.netlify.com")
        print("2. Click 'Add new site' → 'Import an existing project'")
        print("3. Choose GitHub → Select 'resume_roaster_app'")
        print("4. Set environment variable: GROQ_API_KEY")
        print("5. Deploy!")
        return 0
    else:
        print("\n❌ Some checks failed. Please fix the issues above.")
        return 1

if __name__ == "__main__":
    sys.exit(main())
