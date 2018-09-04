#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : pureoym
# @Contact : pureoym@163.com
# @TIME    : 2018/7/6 14:57
# @File    : web_app.py
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
from flask import Flask, request, Response, render_template
import json

import utils

app = Flask(__name__)


@app.route('/test')
@app.route('/test/<name>')
def test_page(name=None):
    """
    home page
    :return:
    """
    return render_template('hello.html', name=name)


@app.route('/translate', methods=['GET', 'POST'])
def translate():
    """
    翻译页面，支持GET,POST
    输入参数：input=输入文本
    :return:
    """
    if request.method == 'POST':    # POST方法
        input_text = request.form['input']
        output_text = utils.translate(input_text)
        json_data = {'result': 1, 'data': {'input': input_text, 'output': output_text}}
        content = json.dumps(json_data, ensure_ascii=False)
        resp = Response(content)
        return resp
    else:   # GET方法
        input_text = request.args.get('input')
        output_text = utils.translate(input_text)
        json_data = {'result': 1, 'data': {'input': input_text, 'output': output_text}}
        content = json.dumps(json_data, ensure_ascii=False)
        resp = Response(content)
        return resp


@app.route('/translate/mutilanguage', methods=['GET', 'POST'])
def translate_muti_language():
    """
    多语言翻译，支持POST,GET
    输入参数：input=输入文本，from=源语言代码，to=目标语言代码
    :return:
    """
    if request.method == 'POST':    # POST方法
        input_text = request.form['input']
        from_language = request.form['from']
        to_language = request.form['to']
        output_text = utils.translate_muti_language(input_text, from_language, to_language)
        json_data = {'result': 1, 'data': {'input': input_text, 'output': output_text}}
        content = json.dumps(json_data, ensure_ascii=False)
        resp = Response(content)
        return resp
    else:   # GET方法
        input_text = request.args.get('input')
        from_language = request.args.get('from')
        to_language = request.args.get('to')
        output_text = utils.translate_muti_language(input_text, from_language, to_language)
        json_data = {'result': 1, 'data': {'input': input_text, 'output': output_text}}
        content = json.dumps(json_data, ensure_ascii=False)
        resp = Response(content)
        return resp


if __name__ == '__main__':
    app.run(host='0.0.0.0')
