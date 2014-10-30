# -*- coding: utf-8 -*-
#coding=utf-8
from functools import wraps
import flask
from flask import render_template, request, redirect, url_for, sessions, Response, session
import urllib
import types
import datetime

#define utils Class
class Utils(object):
     @staticmethod
     def genResponse(ok, obj):
         if ok:
             status = 1
         else:
             status = 0

         return {
            'status':status,
            'data':obj
         }

     #check sign is Correct
     @staticmethod
     def checkSign(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            #sign logic
            print('in check sign func')
            return f(*args, **kwargs)
        return decorated_function

     #check user token
     @staticmethod
     def checkToken(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            #sign logic
            print('in check token func')
            return f(*args, **kwargs)
        return decorated_function


class DumpToDict(object):
    def __init__(self):
        pass
    def dumpToList(self, result=None):
        if not result:
            result = self.sqlData

        #获取model的所遇key
        keyList = self.__mapper__.c.keys()
        #定义数组

        if isinstance(result, list):
            resultLength = len(result)
            tempList = range(resultLength)
            i = 0

            for sqlObj in result:
                tempList[i] = {}
                for key in keyList:
                    tempList[i][key] = getattr(sqlObj, key)
                    if isinstance(tempList[i][key], datetime.date):
                        tempList[i][key] = tempList[i][key].strftime("%Y-%m-%d %H:%M:%S")
                i += 1
        else:
            tempList = {}
            for key in keyList:
                    tempList[key] = getattr(result, key)
                    if isinstance(tempList[key], datetime.date):
                        tempList[key] = tempList[key].strftime("%Y-%m-%d %H:%M:%S")

        return tempList