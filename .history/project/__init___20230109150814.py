import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

from project.core.views import core
from project.error_pages.handlers import error_pages

app.register_blueprint(core)
app.register_blueprint(error_pages)

#####################################################