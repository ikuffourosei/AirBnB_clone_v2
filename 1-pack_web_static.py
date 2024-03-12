#!/usr/bin/python3
"""a Fabric script that generates a .tgz archive
from the contents of the web_static folder of your AirBnB Clone repo
"""


import os
from datetime import datetime
from fabric.api import local


def do_pack():
    """
    Generates a .tgz archive from the contents of the web_static folder
    """
    try:
        # Create the 'versions' directory if it doesn't exist
        if not os.path.exists("versions"):
            os.makedirs("versions")

        current = datetime.now()
        timeformat = current.strftime("%Y%m%d%H%M%S")

        archive_name = "web_static_" + timeformat + ".tgz"

        # Compress the contents of the web_static folder into the archive
        local("tar -cvzf versions/{} web_static".format(archive_name))

        # Return the archive path if the archive has been correctly generated
        return os.path.abspath("versions/" + archive_name)
    except Exception as e:
        print(e)
        return None
