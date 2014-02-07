#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This file is part of Elemental.
#
# Copyright 2014 Paul Durivage <pauldurivage+git@gmail.com>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from flask.ext.login import login_user, logout_user
from flask import render_template, request, flash, redirect, url_for

from elemental import app
from elemental.model.forms import SignupForm
from elemental.model.user import UserObj


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = request.form.get('email')
        passwd = request.form.get('password')
        try:
            assert user and passwd, "Username and password are required fields."
        except AssertionError as e:
            flash(e.message, 'danger')
        else:
            user = UserObj.login(user, passwd)
            if user:
                login_user(user)
                flash('Logged in successfully', 'success')
                return redirect(url_for('index'))
            else:
                flash('Unable to verify username and password', 'danger')
    return render_template('login.html')


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = SignupForm(request.form)
    if form.validate_on_submit():
        app.logger.debug('validate')
        email = request.form.get('email')
        passwd = request.form.get('passwd')
        passwd_verify = request.form.get('passwd_verify')
        if passwd == passwd_verify:
            result = UserObj.create(email, passwd)
            app.logger.debug(result)
            if result:
                flash('User account successfully created.')
                return redirect(url_for('index'))
        else:
            flash('Passwords do not match!', 'danger')
    return render_template('signup.html', form=form)
