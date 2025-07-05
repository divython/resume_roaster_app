#!/usr/bin/env python3
"""
Quick Start Script for Resume Roaster
Choose your deployment option and get started!
"""
import os
import sys

def main():
    print("🔥 Resume Roaster - Quick Start Guide")
    print("=" * 50)
    print()
    
    print("You have multiple deployment options:")
    print()
    
    print("🥇 1. Streamlit Cloud (RECOMMENDED - FREE)")
    print("   ✅ Perfect for AI apps")
    print("   ✅ Beautiful UI") 
    print("   ✅ File uploads work")
    print("   ✅ Easy GitHub deployment")
    print("   📁 File: streamlit_app.py")
    print("   🌐 Deploy: https://share.streamlit.io")
    print()
    
    print("🥈 2. Docker + Railway/Render")
    print("   ✅ Professional deployment")
    print("   ✅ Full Flask app support")
    print("   ✅ Easy scaling")
    print("   📁 Files: Dockerfile_streamlit, Dockerfile_flask")
    print("   🌐 Deploy: https://railway.app or https://render.com")
    print()
    
    print("🥉 3. Traditional Hosting (Heroku)")
    print("   ✅ Established platform")
    print("   ⚠️  No longer free")
    print("   📁 File: app.py (original Flask)")
    print("   🌐 Deploy: https://heroku.com")
    print()
    
    try:
        choice = input("Which option would you like to try? (1/2/3): ").strip()
        
        if choice == "1":
            print("\n🎨 Setting up Streamlit version...")
            print("✅ File: streamlit_app.py")
            print("✅ Requirements: requirements_streamlit.txt")
            print("✅ Config: .streamlit/config.toml")
            print()
            print("🚀 Next steps:")
            print("1. Set environment variable: GROQ_API_KEY")
            print("2. Run: streamlit run streamlit_app.py")
            print("3. Or deploy to: https://share.streamlit.io")
            
            # Test if we can run Streamlit
            try:
                test_run = input("\nWould you like to test it locally? (y/n): ").lower().strip()
                if test_run in ['y', 'yes']:
                    if not os.getenv('GROQ_API_KEY'):
                        print("⚠️  Please set GROQ_API_KEY environment variable first")
                        print("   Windows: set GROQ_API_KEY=your_key_here")
                        print("   Linux/Mac: export GROQ_API_KEY=your_key_here")
                    else:
                        print("🚀 Starting Streamlit...")
                        os.system("streamlit run streamlit_app.py")
            except KeyboardInterrupt:
                pass
                
        elif choice == "2":
            print("\n🐳 Setting up Docker version...")
            print("✅ Streamlit Docker: Dockerfile_streamlit")
            print("✅ Flask Docker: Dockerfile_flask") 
            print("✅ Compose: docker-compose-full.yml")
            print()
            print("🚀 Next steps:")
            print("1. Choose: Railway (https://railway.app) or Render (https://render.com)")
            print("2. Connect your GitHub repository")
            print("3. Set environment variable: GROQ_API_KEY")
            print("4. Deploy!")
            
        elif choice == "3":
            print("\n⚡ Setting up Traditional Flask...")
            print("✅ File: app.py")
            print("✅ Requirements: requirements.txt")
            print("✅ Templates: templates/index.html")
            print()
            print("🚀 Next steps:")
            print("1. Deploy to Heroku, DigitalOcean, or similar")
            print("2. Set environment variable: GROQ_API_KEY")
            print("3. Configure web server")
            
        else:
            print("Invalid choice. Please run the script again.")
            
    except KeyboardInterrupt:
        print("\n\n👋 Goodbye!")
    
    print("\n📚 For detailed instructions, see:")
    print("• DEPLOYMENT_OPTIONS.md - Comprehensive guide")
    print("• README.md - Project overview")
    print()
    print("Made with ❤️ by divython")
    print("GitHub: https://github.com/divython/resume-roaster")

if __name__ == "__main__":
    main()
