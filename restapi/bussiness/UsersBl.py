# -*- coding: utf-8 -*-
from functools import wraps
import flask
import hashlib
import time
import httplib
import urllib
import json
import calendar
from datetime import datetime
from flask import render_template, request, redirect, url_for, sessions, Response, session
from sqlalchemy import *
from flask.ext.sqlalchemy import SQLAlchemy
from sqlalchemy.orm import load_only, joinedload, dynamic_loader, lazyload, defer, undefer
from sqlalchemy.ext.serializer import loads, dumps
from restapi import app
from restapi import config
from restapi.models.UsersModel import PlatUser
from restapi.models.faceModel import PlatUserFace
from restapi.bussiness.LoggerBl import log
from restapi.models.dbModel import db




class UsersBl(object):

    def __init__(self):
        self.username = None
        self.password = None
        pass
    
    def getInfoByPwd(self):
        log.error('save logger')
        return True, {}

    def regUser(self):
        user = PlatUser(self.username, self.password)
        db.session.add(user)
        userFace = PlatUserFace(user.Id, 'aaa', 'bbb')
        userFace2 = PlatUserFace(user.Id, 'aaa2', 'bbb3')
        userFace3 = PlatUserFace(user.Id, 'aaa2', 'bbb3')
        user.Faces.append(userFace)
        user.Faces.append(userFace2)
        user.Faces.append(userFace3)
        db.session.commit()
        user.sqlData = PlatUser.query.options(undefer('UserTips')).filter_by(Id=user.Id).all()
        FaceList = userFace.dumpToList(user.sqlData[0].Faces)
        return True, [user.dumpToList(),FaceList]

    def getUserById(self):
        user = PlatUser()
        userFace = PlatUserFace()
        #如果没有找到用户
        user.sqlData = PlatUser\
            .query\
            .options(defer('Password'))\
            .filter_by(Id=self.userId).first()
        if not user.sqlData:
            return False, 'no body'
        #找到用户
        userObj = user.dumpToList(user.sqlData)
        faceList = userFace.dumpToList(user.sqlData.Faces)
        userObj['Faces'] = faceList
        return True, userObj

