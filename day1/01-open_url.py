#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019/6/2 下午9:12
# @Author  : FangZhou
# @Site    : 
# @File    : 01-open_url.py
# @Software: PyCharm
import urllib.request as ul


def open_url():
    """
    简单的例子
    无参数的形式发送一个http请求
    获得一个相应并且保存
    :return:
    """
    # 注意在url一定要加协议类型(http://)
    url = "http://www.baidu.com"
    # urlopen函数可以给这个url发送访问请求，且获得返回
    response = ul.urlopen(url)
    # 解析数据, 得到的返回数据为bytes类型
    # 注意返回的数据类型并不一定是bytes类型，可能是str 根据不同的web而定
    data = response.read()
    # 将bytes类型转化为str 更方便阅读
    data = data.decode('utf-8')

    # 将数据保存到文件
    with open("baidu.html", 'w', encoding='utf-8') as f:
        f.write(data)

    print(data)


if __name__ == '__main__':
    open_url()
