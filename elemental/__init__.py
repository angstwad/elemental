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

from flask import Flask
from flask.ext.admin import Admin
from flask.ext.bcrypt import Bcrypt
from flask.ext.login import LoginManager
from flask.ext.mongoengine import MongoEngine

from elemental.config import config

app = Flask(__name__)
app.config.from_object(config)

# Jinja Prettiness
app.jinja_env.trim_blocks = True
app.jinja_env.lstrip_blocks = True

# Exctensions
admin = Admin(app)
crypt = Bcrypt(app)
db = MongoEngine(app)
login_manager = LoginManager(app)

# Import the MVC elements
import elemental.view
import elemental.view.admin
import elemental.model.login
import elemental.control.filters