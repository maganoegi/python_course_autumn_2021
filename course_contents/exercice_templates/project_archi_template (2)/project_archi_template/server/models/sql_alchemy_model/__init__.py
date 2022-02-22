
from flask_sqlalchemy import SQLAlchemy
from server import app

DB_NAME = "my.db"
SQL_DATABASE_URI = f"sqlite:///{DB_NAME}"
app.config['SQLALCHEMY_DATABASE_URI'] = SQL_DATABASE_URI

db = SQLAlchemy(app)

