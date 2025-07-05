#!/usr/bin/env python3
"""
Resume Roaster Application Launcher
"""
import os
import sys
import subprocess
import platform

def main():
    """Main launcher function."""
    print("🔥 Resume Roaster Application Launcher 🔥")
    print("=" * 50)
    
    # Check Python version
    if sys.version_info < (3, 7):
        print("❌ Error: Python 3.7 or higher is required.")
        print(f"Current version: {sys.version}")
        sys.exit(1)
    
    # Check if .env file exists
    if not os.path.exists('.env'):
        print("⚠️  Warning: .env file not found!")
        print("Please copy .env.example to .env and add your Groq API key.")
        
        # Ask user if they want to create .env from example
        try:
            create_env = input("Do you want to create .env from .env.example? (y/n): ").lower().strip()
            if create_env in ['y', 'yes']:
                if os.path.exists('.env.example'):
                    import shutil
                    shutil.copy('.env.example', '.env')
                    print("✅ Created .env file from template.")
                    print("Please edit .env and add your Groq API key before continuing.")
                else:
                    print("❌ .env.example not found!")
                    sys.exit(1)
            else:
                print("Please create .env file manually.")
                sys.exit(1)
        except KeyboardInterrupt:
            print("\nOperation cancelled.")
            sys.exit(1)
    
    # Check if virtual environment should be created
    venv_path = "venv"
    if platform.system() == "Windows":
        venv_python = os.path.join(venv_path, "Scripts", "python.exe")
        venv_pip = os.path.join(venv_path, "Scripts", "pip.exe")
    else:
        venv_python = os.path.join(venv_path, "bin", "python")
        venv_pip = os.path.join(venv_path, "bin", "pip")
    
    if not os.path.exists(venv_path):
        print("📦 Creating virtual environment...")
        try:
            subprocess.run([sys.executable, "-m", "venv", venv_path], check=True)
            print("✅ Virtual environment created successfully.")
        except subprocess.CalledProcessError:
            print("❌ Failed to create virtual environment.")
            print("Please install venv: pip install virtualenv")
            sys.exit(1)
    
    # Install dependencies
    print("📦 Installing dependencies...")
    try:
        subprocess.run([venv_pip, "install", "-r", "requirements.txt"], check=True)
        print("✅ Dependencies installed successfully.")
    except subprocess.CalledProcessError:
        print("❌ Failed to install dependencies.")
        print("Please check your internet connection and try again.")
        sys.exit(1)
    
    # Start the application
    print("\n🚀 Starting Resume Roaster...")
    print("Open your browser to: http://localhost:5000")
    print("Press Ctrl+C to stop the server")
    print("-" * 50)
    
    try:
        subprocess.run([venv_python, "app.py"], check=True)
    except subprocess.CalledProcessError:
        print("❌ Failed to start application.")
        print("Please check the logs for errors.")
        sys.exit(1)
    except KeyboardInterrupt:
        print("\n👋 Resume Roaster stopped.")
        sys.exit(0)

if __name__ == "__main__":
    main()
