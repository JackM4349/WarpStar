@echo off

REM Set the Python executable path
set PYTHON_PATH=C:\path\to\python\executable

REM Set the Flask application file
set FLASK_APP=app.py

REM Set the Flask environment to development
set FLASK_ENV=development

REM Activate the virtual environment if needed
REM Uncomment the line below if you are using a virtual environment
REM call path\to\venv\Scripts\activate.bat

REM Install required Python packages
pip install -r requirements.txt

REM Run the Flask application
%PYTHON_PATH% -m flask run
