# IMPORTS
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
if os.path.exists("env.py"):
    import env


# Create new app instance
app = Flask(__name__)
# Configure app
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY")
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DB_URL")

# Create new database instance
db = SQLAlchemy(app)

# Import routes file last to avoid circular import
from task_manager import routes