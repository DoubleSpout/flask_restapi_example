# -*- coding: utf-8 -*-
import sys,os
def cur_file_dir():
    #获取脚本路径
    path = sys.path[0]
    #判断为脚本文件还是py2exe编译后的文件，如果是脚本文件，则返回的是脚本的目录，如果是py2exe编译后的文件，则返回的是编译后的文件路径
    if os.path.isdir(path):
        pass
    elif os.path.isfile(path):
        path = os.path.dirname(path)
    return path+os.sep+'logs'

    
class Config(object):
    DEBUG = False
    TESTING = False
    SQLALCHEMY_DATABASE_URI = 'mysql://root:@192.168.150.3/6998_VIPCenter'
    SQLALCHEMY_POOL_SIZE = 5
    SQLALCHEMY_POOL_RECYCLE = 499
    SQLALCHEMY_POOL_TIMEOUT = 60

    
    HOST = "0.0.0.0"
    PORT = 5000
    PASSPORT_KEY = "aaaaaaa"

    LOG_PATH = cur_file_dir()
    LOGGER_NAME = 'mylog'
    SESSION_KEY = '05599c095f5900cc288bcadd9f9b4c34'
    P3P_HEADER = 'CURa ADMa DEVa PSAo PSDo OUR BUS UNI PUR INT DEM STA PRE COM NAV OTC NOI DSP COR'
    
    
class Production(Config):
    ENV = 'Production'
    SQLALCHEMY_DATABASE_URI = 'mysql://root:@192.168.1.143/6998_VIPCenter'
    SQLALCHEMY_POOL_SIZE = 20
    PORT = 5000


class Debug(Config):
    ENV = 'Debug'
    DEBUG = True
    SQLALCHEMY_ECHO = True
    