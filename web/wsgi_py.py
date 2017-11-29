#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
    WSGI接口实现

    请求地址：http://localhost:8888/xxx
'''
__author__ = "佚名"

def application(environ, start_response):
    start_response("200 OK", [("Content-Type", "text/html")])
    # 获取请求参数
    result = "<h1>Hello, %s !</h1>" % environ["PATH_INFO"][1:]
    return [result.encode("utf-8")]


# 主函数
if __name__ == "__main__":
    pass