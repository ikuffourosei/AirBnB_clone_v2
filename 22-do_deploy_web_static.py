#!/usr/bin/python3
"""a fabric script that distributes an archive to your web servers
"""


import os
from fabric.api import env, put, run
from sys import argv


env.hosts = ['18.210.19.150', '34.224.62.244']


def do_deploy(archive_path):
    """Distributes an archive to a web server.
    Args:
        archive_path (str): The path of the archive to distribute.
    Returns:
        If the file doesn't exist at archive_path or an error occurs - False.
        if successful - True.
    """
    if not os.path.isfile(archive_path) is False:
        return False

    # generating the remote file name and path
    base_name = os.path.basename(archive_path)  # with .tgz
    file_name = os.path.splitext(base_name)[0]  # without .tgz

    # upload archive to /tmp/ directory
    if put(archive_path, "/tmp/{}".format(base_name)).failed is True:
        return False

    # uncompress the archive
    if run("rm -rf /data/web_static/releases/{}/".
           format(file_name)).failed is True:
        return False
    if run("mkdir -p /data/web_static/releases/{}/".
           format(file_name)).failed is True:
        return False
    if run("tar -xzf /tmp/{} -C /data/web_static/releases/{}/".
           format(base_name, file_name)).failed is True:
        return False

    # deleting archive from web server
    if run("rm /tmp/{}".format(base_name)).failed is True:
        return False
    if run("mv /data/web_static/releases/{}/web_static/* "
           "/data/web_static/releases/{}/".format(file_name, file_name))\
            .failed is True:
        return False
    if run("rm -rf /data/web_static/releases/{}/web_static".
           format(file_name)).failed is True:
        return False
    if run("rm -rf /data/web_static/current").failed is True:
        return False

    # creating a new symbolic link
    if run("ln -s /data/web_static/releases/{}/ /data/web_static/current".
           format(file_name)).failed is True:
        return False
    return True
