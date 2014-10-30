# -*- coding: utf-8 -*-
from datetime import datetime
from flask import Flask

from flask.ext.sqlalchemy import SQLAlchemy
from restapi import app
from restapi.models.dbModel import db
from restapi.models.faceModel import *
from restapi.bussiness.UtilsBl import DumpToDict
import json

#vip用户的model
class PlatUser(db.Model, DumpToDict):
    #表名
    __tablename__ = 'Plat_User'
    
    Id = db.Column(db.Integer, primary_key=True)
    UserName = db.Column(db.String(50))
    Password = db.Column(db.String(50))
    UserTips = db.deferred(db.Column(db.Text))
    WriteTime = db.Column(db.DateTime, onupdate=datetime.now, default=datetime.now)
    Faces = db.relationship('PlatUserFace', backref='Plat_User', lazy='select')


    def __init__(self, UserName=None, Password=None):
        self.UserName = UserName
        self.Password = Password
