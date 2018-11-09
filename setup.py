# -*- coding:utf-8 -*-
# @author bricker
# @date 2018/11/9
# @file mongo.py

"""
poseidon打包脚本
"""

from PyInstaller.__main__ import run

if __name__ == '__main__':
    opts = ['./src/poseidon.py', '-w', '-F', '--icon=favicon.ico']
    run(opts)