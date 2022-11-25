# 5ocean
# Install
- Clone this repo.
- In project folder run python **-m venv venv command (bold)**. This will create virtual environment with local clean python installation.
- Activate created virtual environment using venv\Scripts\activate command on Windows or source ./venv/Scripts/activate on Linux or MacOS.
- Run pip install -r requirements.txt command to install all necessary dependencies.
- Run set FLASK_APP=app.py on Windows or FLASK_APP=app.py on Linux or MacOS.
- Optionnaly run set FLASK_ENV=development or FLASK_ENV=development to enable debug mode and autorestart on source code changes on Windows or Linux and MacOS respectively.
- Run flask run command to start development server.
- Run gunicorn app:app to start production server.
