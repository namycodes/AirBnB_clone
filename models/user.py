#!/usr/bin/emv python3

from models.base_model import BaseModel

''' public attributes class '''


class User(BaseModel):
    # public attributes class

    email = ""
    password = ""
    first_name = ""
    last_name = ""
