#!/usr/bin/env python
# -*- coding: utf-8 -*-


from flask import Flask, render_template, url_for


app = Flask(__name__)
app.config.update(dict(
    TEMPLATES_AUTO_RELOAD=True,  # disable template cache
    SEND_FILE_MAX_AGE_DEFAULT=0,  # disable JS cache
    JSON_AS_ASCII=False  # avoid being garbled
))


@app.route('/')
def index():
    return render_template('base.html', title='Hello React!', js=url_for('static', filename='js/bundle.js'))
