#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : pureoym
# @Contact : pureoym@163.com
# @TIME    : 2018/9/4 9:35
# @File    : test.py
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
from urllib2 import urlopen


def test_download():
    url = 'http://data.mgt.chinaso365.com/cp-center/tfs/getkey?' \
          'imgurl=https://wx2.sinaimg.cn/orj360/70f96dffgy1fuqn12cvzqj20k109wdhm.jpg'
    response = urlopen(url)
    print response.read()


if __name__ == '__main__':
    test_download()
