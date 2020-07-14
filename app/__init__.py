# -*- coding: utf-8 -*-

import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

username = os.environ['MYSQL_USERNAME']
password = os.environ['MYSQL_PASSWORD']
host = 'localhost'
port = '3306'
db_name = 'ilittlesun_blog'

# engine = create_engine('mysql+pymysql://%s:%s@%s:%s/%s') %(username, password, host, port, db_name)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://%s:%s@%s:%s/%s' %(username, password, host, port, db_name)
db = SQLAlchemy(app)

from . import views

from .main import main as main_blueprint
app.register_blueprint(main_blueprint, url_prefix='/main')