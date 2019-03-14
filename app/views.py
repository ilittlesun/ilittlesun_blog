# -*- coding:utf-8 -*-

from . import app

@app.route('/')
def index():
    return 'hello world'
