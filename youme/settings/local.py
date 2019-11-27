from .base import *
from decouple import config

SECRET_KEY = config('SECRET_KEY', default='9j==%5s2v$6j4(+3j&r&i48d(pg^1)6&v)=_5zkmsus2y!*$(_')

DEBUG = True

ALLOWED_HOSTS = []
