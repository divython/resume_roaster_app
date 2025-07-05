@echo off
echo Starting Resume Roaster Application...
echo.

REM Check if virtual environment exists
if not exist "venv\" (
    echo Creating virtual environment...
    python -m venv venv
    echo.
)

REM Activate virtual environment
echo Activating virtual environment...
call venv\Scripts\activate.bat

REM Install dependencies
echo Installing dependencies...
pip install -r requirements.txt

REM Check if .env file exists
if not exist ".env" (
    echo.
    echo WARNING: .env file not found!
    echo Please copy .env.example to .env and add your Groq API key.
    echo.
    pause
    exit /b 1
)

REM Start the application
echo.
echo Starting Resume Roaster...
echo Open your browser to: http://localhost:5000
echo.
python app.py

pause
