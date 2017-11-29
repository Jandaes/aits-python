#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 从wsgiref模块导入:
from wsgiref.simple_server import make_server
# 导入我们自己编写的application函数:
from wsgi_py import application

'''
    负责启动wsgi接口的服务
'''
__author__ = "佚名"

# 创建一个服务器
httpd = make_server("", 8888, application)
print("Serving HTTP on port 8888...")
# 开始监听HTTP请求:
httpd.serve_forever()

