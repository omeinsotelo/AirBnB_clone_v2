#!/usr/bin/python3
"""Deply static"""
from fabric.api import local
from datetime import datetime


def do_pack():
    """create a .tgz with all content in web_static folder"""
    # create the folder if not exists
    local("mkdir -p versions")
    # create the name of the tgz
    now = datetime.now()
    nameTgz = "versions/web_static_"
    nameTgz += "{}{}{}".format(now.year, now.month, now.day)
    nameTgz += "{}{}{}".format(now.hour, now.minute, now.second)
    nameTgz += ".tgz"
    # create the tgz
    tgzCommand = "tar -cvzf {} web_static".format(nameTgz)
    # return de path if the file was created
    if local(tgzCommand) == 1:
        return None
    return nameTgz
