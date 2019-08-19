#!/usr/bin/python3
from fabric.api import run, put
import os
env.hosts = ['34.74.176.216', '34.74.12.104']


def do_deploy(archive_path):
    """distributes an archive to your web servers"""
    if os.path.exists(archive_path) is False:
        return False
    result = put("{:}".format(archive_path), "/tmp/")
    if result.failed:
        return False
    archive_filename = archive_path.replace("versions/", "")
    filename_noext = archive_filename.replace(".tgz", "")
    result = run('mkdir -p /data/web_static/releases/{:}/'.format(
        filename_noext))
    if result.failed:
        return False
    result = run('tar -xzf /tmp/{:} -C /data/web_static/releases/{:}/'.format(
        archive_filename, filename_noext))
    if result.failed:
        return False
    result = run('rm /tmp/{:}'.format(archive_filename))
    if result.failed:
        return False
    result = run('mv /data/web_static/releases/{:}/web_static/*' +
                 '/data/web_static/releases/{:}/'.format(
                     filename_noext, filename_noext))
    if result.failed:
        return False
    result = run("rm -rf /data/web_static/releases/{:}/web_static".format(
        filename_noext))
    if result.failed:
        return False
    result = run('rm -rf /data/web_static/current')
    if result.failed:
        return False
    result = run(
        'ln -s /data/web_static/releases/{:}/ /data/web_static/current'.format(
            filename_notext))
    if result.failed:
        return False
    return True
