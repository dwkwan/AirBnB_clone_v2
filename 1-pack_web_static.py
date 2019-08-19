#!/usr/bin/python3
from datetime import datetime
from fabric.api import local


def do_pack():
    """generates a .tgz archive from the contents of the web_static folder"""
    now = datetime.now()
    dt_string = now.strftime("%Y%m%d%H%m")
    output_file = "./versions/{:}.tgz".format(dt_string)
    local("mkdir versions")
    result = local("tar -cvzf {:} web_static".format(output_file))
    if result.failed:
        print("None")
