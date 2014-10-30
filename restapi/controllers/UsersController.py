# -*- coding: utf-8 -*-
#coding=utf-8

#import package
import os
import flask
import json
from flask import render_template, request, redirect, url_for, sessions, Response, session, make_response
import httplib
import urllib
from xml.dom.minidom import parse, parseString
from datetime import datetime
from flask.ext.restful import reqparse, abort, Api, Resource

#import custom
from restapi.bussiness.UtilsBl import Utils
from restapi.models import UsersModel
from restapi.bussiness.UsersBl import UsersBl
from restapi.bussiness import LoggerBl
from restapi import config
from restapi import app


#user login controller

#login param
loginParser = reqparse.RequestParser()
loginParser.add_argument('username', type=str, required=True, location='form')
loginParser.add_argument('password', type=str, required=True, location='form')

#reg param
regParser = reqparse.RequestParser()
regParser.add_argument('username', type=str, required=True, location='form')
regParser.add_argument('password', type=str, required=True, location='form')

#reg param
infoParser = reqparse.RequestParser()
infoParser.add_argument('user_id', type=int, required=True, dest='userId')


class UserLogin(Resource):

    @Utils.checkSign
    def put(self):
        #check param
        args = loginParser.parse_args()
        user = UsersBl()
        user.username = args['username']
        user.password = args['password']
        #do get info
        ok, userObj = user.getInfoByPwd()
        return Utils.genResponse(ok, userObj)


class UserReg(Resource):

    #regist user
    @Utils.checkSign
    def post(self):
        #check param
        args = regParser.parse_args()
        user = UsersBl()
        user.username = args['username']
        user.password = args['password']
        #do reg
        ok, userObj = user.regUser()
        return Utils.genResponse(ok, userObj)


class UserInfo(Resource):

    @Utils.checkSign
    @Utils.checkToken
    def get(self):
        #check param
        args = infoParser.parse_args()
        user = UsersBl()
        user.userId = args['userId']
        #do userObj
        ok, userObj = user.getUserById()
        return Utils.genResponse(ok, userObj)

    @Utils.checkSign
    @Utils.checkToken
    def post(self, user_id):
        # modify user info
        pass
