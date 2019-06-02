#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019/6/2 下午9:31
# @Author  : FangZhou
# @Site    : 
# @File    : 02-get_parameter.py
# @Software: PyCharm
import urllib.parse
import string
import urllib.request as ur


def is_contain_chinese(str):
    """
    judge a str if contain a chinese
    :param str:
    :return:
    """
    for _char in str:
        if '\u4e00' <= _char <= '\u9fa5':
            return True
    return False


def get_with_params():
    """
    use the get method to send a request with get params
    :return:
    """
    url = "http://www.baidu.com/s?wd="
    params = "spider"
    # splice the string
    url += params

    # python3 在这里如果参数是中文的话, 直接拼接会出现错误需要转义
    # 所以如果url中出现中文，则需要转义
    if is_contain_chinese(url):
        url = urllib.parse.quote(url, safe=string.printable)

    response = ur.urlopen(url)
    data = response.read()
    data = data.decode('utf-8')

    # save data
    with open('baidu_with_params.html', 'w', encoding='utf-8') as f:
        f.write(data)
    print(data)


if __name__ == '__main__':
    get_with_params()
