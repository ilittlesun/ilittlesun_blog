# -*- coding:utf-8 -*-

from flask import render_template

from . import main
from .. import models

@main.route('/')
def index():
    return render_template('main/main_index.html')

@main.route('/insert')
def insert():
    models.create_table(models.db)
    return 'create_table success'