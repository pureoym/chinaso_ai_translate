#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : pureoym
# @Contact : pureoym@163.com
# @TIME    : 2018/7/6 15:30
# @File    : utils.py
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
import httplib
import md5
import urllib
import random

import sys
reload(sys)
sys.setdefaultencoding('utf-8')


APP_ID = '20180706000183232'
SECRET_KEY = '4Ay350mc66H_h_TyNYpZ'
API_URL = '/api/trans/vip/translate'
Q = 'apple'
FROM_LANGUAGE = 'zh'
TO_LANGUAGE = 'en'
SALT = random.randint(32768, 65536)


def translate(input_text):
    httpClient = None
    input_text = input_text.encode('utf-8')
    sign = APP_ID + input_text + str(SALT) + SECRET_KEY
    m1 = md5.new()
    m1.update(sign)
    sign = m1.hexdigest()
    url = API_URL + '?appid=' + APP_ID + '&q=' + urllib.quote(input_text) + \
          '&from=' + FROM_LANGUAGE + '&to=' + TO_LANGUAGE + '&salt=' + str(SALT) \
          + '&sign=' + sign

    result = ''
    try:
        httpClient = httplib.HTTPConnection('api.fanyi.baidu.com')
        httpClient.request('GET', url)

        # response是HTTPResponse对象
        response = httpClient.getresponse()
        result = response.read()
    except Exception, e:
        print e
    finally:
        if httpClient:
            httpClient.close()

    return result

