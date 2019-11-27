from .base import *
from decouple import config

SECRET_KEY = config('SECRET_KEY')

DEBUG = False

ALLOWED_HOSTS = ['you-me.xkgwyzmtvx.ap-northeast-2.elasticbeanstalk.com']
