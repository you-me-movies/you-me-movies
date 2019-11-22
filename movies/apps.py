from django.apps import AppConfig
import requests
from decouple import config
from pprint import pprint
import csv


class MoviesConfig(AppConfig):
    name = 'movies'
