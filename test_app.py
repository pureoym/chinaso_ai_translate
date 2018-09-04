#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : pureoym
# @Contact : pureoym@163.com
# @TIME    : 2018/9/4 10:55
# @File    : test_app.py
# Copyright 2017 pureoym. All Rights Reserved.
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
# ========================================================================
import sqlite3
from flask import Flask, request, session, g, redirect, url_for, \
    abort, render_template, flash

# configuration
DATABASE = '/tmp/test_app.db'
DEBUG = True
SECRET_KEY = 'development key'
USERNAME = 'admin'
PASSWORD = 'default'

# create our little application :)
# from_object() 将会寻找给定的对象(如果它是一个字符串，则会导入它)，
# 搜寻里面定义的全部大写的变量。在我们的这种情况中，配置文件就是我们上
# 面写的几行代码。 你也可以将他们分别存储到多个文件。
app = Flask(__name__)
app.config.from_object(__name__)


# 通常，从配置文件中加载配置是一个好的主意。这是 from_envvar() 所做的，
# 用它替换上面的 from_object()。这种方法我们可以设置一个名为
# FLASKR_SETTINGS 环境变量来设定一个配置文件载入后是否覆盖默认值。 静
# 默开关告诉 Flask 不去关心这个环境变量键值是否存在。
# app.config.from_envvar('FLASKR_SETTINGS', silent=True)

# secret_key 是需要为了保持客户端的会话安全。明智地选择该键，使得它难以
# 猜测，尽可能复杂。 调试标志启用或禁用交互式调试。决不让调试模式在生产系
# 统中启动，因为它将允许用户在服务器上执行代码！

# 我们还添加了一个轻松地连接到指定数据库的方法，这个方法用于在请求时打开一
# 个连接，并且在交互式 Python shell 和脚本中也能使用。这对以后很方便。
def connect_db():
    return sqlite3.connect(app.config['DATABASE'])


if __name__ == '__main__':
    app.run()