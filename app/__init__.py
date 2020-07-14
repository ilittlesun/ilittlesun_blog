# -*- coding: utf-8 -*-

import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

base_dir = os.getcwd()
print(base_dir)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(base_dir, 'ilittlesun_blog')

db = SQLAlchemy(app)

from . import views

from .main import main as main_blueprint
app.register_blueprint(main_blueprint, url_prefix='/main')