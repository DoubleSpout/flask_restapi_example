# -*- coding: utf-8 -*-

from flask import Flask, request
from flask.ext.restful import Resource, Api
from restapi.controllers.UsersController import UserLogin, UserReg, UserInfo, getHobbyUser
from restapi import app
api = Api(app)


api.add_resource(UserLogin, '/userlogin/')
api.add_resource(UserReg, '/userreg/')
api.add_resource(UserInfo, '/userinfo/')
api.add_resource(getHobbyUser, '/gethobby/')
