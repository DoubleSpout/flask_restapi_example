# -*- coding: utf-8 -*-
from datetime import datetime
from flask import Flask

from flask.ext.sqlalchemy import SQLAlchemy
from restapi import app
from restapi.models.dbModel import *
from restapi.models.UsersModel import *
from restapi.bussiness.UtilsBl import DumpToDict
import json

#用户兴趣爱好model
class PlatUserHobby(db.Model, DumpToDict):
    #表名
    __tablename__ = 'Plat_User_Hobby'
    
    Id = db.Column(db.Integer, primary_key=True)
    HobbyName = db.Column(db.String(50))
    WriteTime = db.Column(db.DateTime, onupdate=datetime.now, default=datetime.now)


    def __init__(self, UserId=None, HobbyName=None):
        self.UserId = UserId
        self.HobbyName = HobbyName
