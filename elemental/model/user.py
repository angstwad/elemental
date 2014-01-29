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

import flask

from elemental import crypt
from elemental.model import User


class UserObj(object):
    def __init__(self, user_obj=None):
        self._user_obj = user_obj

    @staticmethod
    def get(user_id):
        doc = User.objects(email=user_id).first()
        if doc:
            return UserObj(doc)

    @staticmethod
    def login(user_id, password):
        doc = User.objects(email=user_id).first()
        is_valid = None
        if doc:
            is_valid = crypt.check_password_hash(doc['password'], password)
        if is_valid:
            user = UserObj(doc)
            user.authenticated = True
            return user

    @staticmethod
    def create(user_id, password):
        hash = crypt.generate_password_hash(password)
        try:
            User(email=user_id, password=hash).save()
        except Exception as e:
            flask.flash(e.message, 'danger')
        else:
            return True

    def is_authenticated(self):
        return getattr(self, 'authenticated', None)

    def is_active(self):
        return getattr(self._user_obj, 'active', None)

    def is_anonymous(self):
        return False

    def get_id(self):
        return getattr(self._user_obj, 'email', None)
