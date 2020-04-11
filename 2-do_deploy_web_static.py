#!/usr/bin/python3
"""Deply static"""
from fabric.api import local, put, run, env
from datetime import datetime
from os.path import isfile

env.hosts = ["54.172.160.86", "34.230.20.37"]


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


def do_deploy(archive_path):
    """
    Fabric scriptc that distributes an archive to your web servers,
    using the function do_deploy:
    """
    # If the path doesn't exists
    if isfile(archive_path) is False:
        return False
    # Try all the commands
    try:
        fullName = archive_path.split("/")[1]
        fileName = archive_path.split("/")[1].split(".")[0]
        # Upload the archive_path in /tmp/
        put(archive_path, "/tmp/{}".format(fullName))

        # Create the directory where are going to be uncompress
        command = "mkdir -p /data/web_static/releases/{}/".format(fileName)
        run(command)

        # Uncompress the file into /data/web_static/releases/
        command = "tar -xzf /tmp/{} -C ".format(fullName)
        command += "/data/web_static/releases/{}/".format(fileName)
        run(command)

        # Delete file from server
        command = "rm /tmp/{}".format(fullName)
        run(command)

        # Move all the files into the dir releases/web_static<number>
        command = "mv /data/web_static/releases/{}".format(fileName)
        command += "/web_static/* "
        command += "/data/web_static/releases/{}/".format(fileName)
        run(command)

        # Delete the folder that create the uncompres process
        command = "rm -rf /data/web_static/releases/{}".format(fileName)
        command += "/web_static"
        run(command)

        # Delete the symbolic link
        command = "rm -rf /data/web_static/current"
        run(command)

        # Create the new symbolic link
        command = "ln -s /data/web_static/releases/{}/ ".format(fileName)
        command += "/data/web_static/current"
        run(command)
    except Exception:
        # Return false if it fails
        return False
    # Return true if all run good
    return True
