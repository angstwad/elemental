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

import os

SECRET_KEY = os.urandom(32)

# This is obvious, isn't it?
MONGODB_SETTINGS = {
    'db': 'elemental',
    'host': 'vm.local'
}

# Login Settings
LOGIN_VIEW = "login"

# Debug Toolbar
DEBUG_TB_PROFILER_ENABLED = True