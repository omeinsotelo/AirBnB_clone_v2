#!/usr/bin/python3
"""
    generates a .tgz archive from the contents of the web_static folder
    of AirBnB Clone repo, using the function do_pack.
"""
from fabric.api import local
from datetime import datetime


def do_pack():
    """create a .tgz with all content in web_static folder"""
    # Flag -p to create the folder if not exists
    local("mkdir -p versions")
    # Create the name of tgz
    now = datetime.now()
    nameTgz = "versions/web_static_{}".format(now.strftime("%Y%m%d%H%M%S"))
    nameTgz += ".tgz"
    # Create tgz
    tgzCommand = "tar -cvzf {} web_static".format(nameTgz)
    # Return de path if the file was created
    if local(tgzCommand) == 1:
        return None
    return nameTgz
