#!/usr/bin/python3.8

from decouple import config

username = config('username', default='')
password = config('password', default='')

print(username, password)
