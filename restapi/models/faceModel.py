# -*- coding: utf-8 -*-
from datetime import datetime
from flask import Flask

from flask.ext.sqlalchemy import SQLAlchemy
from restapi import app
from restapi.models.dbModel import *
from restapi.models.UsersModel import *
from restapi.bussiness.UtilsBl import DumpToDict
import json

#vip用户的model
class PlatUserFace(db.Model, DumpToDict):
    #表名
    __tablename__ = 'Plat_User_Face'
    
    Id = db.Column(db.Integer, primary_key=True)
    FaceUrl = db.Column(db.String(50))
    FaceName = db.Column(db.String(50))
    WriteTime = db.Column(db.DateTime, onupdate=datetime.now, default=datetime.now)
    UserId = db.Column(db.Integer, db.ForeignKey('Plat_User.Id'), nullable=False)


    def __init__(self, UserId=None, FaceUrl=None, FaceName=None):
        self.UserId = UserId
        self.FaceUrl = FaceUrl
        self.FaceName = FaceName
