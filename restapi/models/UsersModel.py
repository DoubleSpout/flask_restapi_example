# -*- coding: utf-8 -*-
from datetime import datetime
from flask import Flask

from flask.ext.sqlalchemy import SQLAlchemy
from restapi import app
from restapi.models.dbModel import db
from restapi.models.faceModel import *
from restapi.models.hobbyModel import *
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
    Hobbies = db.relationship('PlatUserHobby', secondary='Plat_User_Hobby_Relation',
        backref=db.backref('Plat_User', lazy='select'), lazy='select')


    def __init__(self, UserName=None, Password=None):
        self.UserName = UserName
        self.Password = Password


#关联表
class UserHobby(db.Model):
    __tablename__ = 'Plat_User_Hobby_Relation'

    Id = db.Column(db.Integer, primary_key=True)
    UserId = db.Column(db.Integer, db.ForeignKey('Plat_User.Id'), nullable=False)
    HobbyId = db.Column(db.Integer, db.ForeignKey('Plat_User_Hobby.Id'), nullable=False)

    db.UniqueConstraint('UserId', 'HobbyId', name='unique_1')

    def __init__(self, UserId, HobbyId):
        self.UserId = UserId
        self.HobbyId = HobbyId

