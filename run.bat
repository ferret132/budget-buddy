@echo off
echo Starting Budget Buddy...
echo.

cd /d "%~dp0"

python -c "import flask" 2>nul
if errorlevel 1 (
    echo Installing Flask...
    pip install flask
    echo.
)

python app.py
pause
