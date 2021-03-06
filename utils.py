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
import json
import sys
# import re

reload(sys)
sys.setdefaultencoding('utf-8')

APP_ID = '123'
SECRET_KEY = '123'
API_URL = '/api/trans/vip/translate'
Q = 'apple'
FROM_LANGUAGE = 'zh'
TO_LANGUAGE = 'en'
SALT = random.randint(32768, 65536)

white_list = {'朋友多了 路才好走': 'More friends, more opportunities.',
              '有路才能人畅其行 物畅其流': 'With roads in place, people and goods can flow.',
              '要幸福就要奋斗': 'Happiness comes out of arduous work.',
              '逢山开路 遇水架桥 将改革进行到底': 'We should surmount all obstacles to carry the reform further to its ultimate triumph.',
              '天下一家': 'The world being one family',
              '不驰于空想 不骛于虚声 一步一个脚印 踏踏实实干好工作': 'We have to avoid the distractions of unsubstantial ideas and superficial fame, take one step at a time, and approach our work with a firm footing.',
              '不驰于空想 不鹜于虚声 一步一个脚印 踏踏实实做好工作': 'We have to avoid the distractions of unsubstantial ideas and superficial fame, take one step at a time, and approach our work with a firm footing.'}


def translate(input_text):
    """
    中文翻译成英文
    :param input_text:
    :return:
    """
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

    # 增加白名单，如果在白名单中，直接翻译，返回结果
    preprocessed_input = preproces(input_text)
    if preprocessed_input in white_list:
        print '输入：' + preprocessed_input + '在白名单中'
        result = white_list[preprocessed_input]
        return result

    # 如果不在白名单中，则调用翻译接口
    try:
        httpClient = httplib.HTTPConnection('api.fanyi.baidu.com')
        httpClient.request('GET', url)

        # response是HTTPResponse对象
        response = httpClient.getresponse()
        resp = response.read()
        result = json.loads(resp).get("trans_result")[0].get("dst")
    except Exception, e:
        print e
    finally:
        if httpClient:
            httpClient.close()

    return result


def preproces(input_text):
    """
    预处理，将正文中的标点变成空格，再去除首尾空格
    :param input_text:
    :return:
    """
    # output_text = re.sub(r'[\,\.\!\?！，。？、]+', ' ', input_text).strip()
    output_text = input_text.replace(',', ' ').replace('，', ' ') \
        .replace('.', ' ').replace('。', ' ') \
        .replace('!', ' ').replace('！', ' ') \
        .replace(';', ' ').replace('；', ' ') \
        .replace('、', ' ') \
        .replace(':', ' ').replace('：', ' ') \
        .replace('?', ' ').replace('？', ' ').strip()
    return output_text


def translate_muti_language(input_text, from_language, to_language):
    """
    多语言翻译
    :param input_text: 
    :param from_language: 
    :param to_language: 
    :return: 
    """
    httpClient = None
    input_text = input_text.encode('utf-8')
    sign = APP_ID + input_text + str(SALT) + SECRET_KEY
    m1 = md5.new()
    m1.update(sign)
    sign = m1.hexdigest()
    url = API_URL + '?appid=' + APP_ID + '&q=' + urllib.quote(input_text) + \
          '&from=' + from_language + '&to=' + to_language + '&salt=' + str(SALT) \
          + '&sign=' + sign

    result = ''

    # 对于中翻英的翻译，增加白名单处理，直接翻译，返回结果
    if from_language == 'zh' and to_language == 'en':
        preprocessed_input = preproces(input_text)
        if preprocessed_input in white_list:
            result = white_list[preprocessed_input]
            return result

    # 否则，调用接口翻译
    try:
        httpClient = httplib.HTTPConnection('api.fanyi.baidu.com')
        httpClient.request('GET', url)

        # response是HTTPResponse对象
        response = httpClient.getresponse()
        resp = response.read()
        result = json.loads(resp).get("trans_result")[0].get("dst")
    except Exception, e:
        print e
    finally:
        if httpClient:
            httpClient.close()

    return result


if __name__ == '__main__':
    input_text = '逢山开路，遇水架桥，将改革进行到底'
    print("====" + preproces(input_text) + "====")
