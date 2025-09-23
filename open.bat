@echo off
echo Starting Heart Disease Project...

:: Start Flask backend
start cmd /k "cd /d C:\Users\some\Desktop\heartdisease && python app.py"

:: Start React frontend
start cmd /k "cd /d C:\Users\some\Desktop\heartdisease\frontend && npm start"

exit
