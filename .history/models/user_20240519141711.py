#!/usr/bin/emv python3 

  ''' User class'''
from models.base_model import BaseModel


class User(BaseModel):
    ''' public attributes class'''

    email = ""
    password = ""
    first_name = ""
    last_name = ""
