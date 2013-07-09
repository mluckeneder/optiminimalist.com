from fabric.api import *


env.hosts = ['luckeneder.net:2280']
env.user = "michael"


def update_project():
    """Updates the remote project
    """
    with cd('/www/optiminimalist'):
        run('git pull')
        with prefix('source /www/optiminimalist/venv/bin/activate'):
            run('pip install -r requirements.txt')
