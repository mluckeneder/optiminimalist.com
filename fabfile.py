from fabric.api import *


env.hosts = ['luckeneder.net:2280']
env.user = "michael"


def deploy():
    """Updates the remote project
    """
    with cd('/www/optiminimalist'):
        run('git pull')
        with prefix('source /www/optiminimalist/venv/bin/activate'):
            run('pip install -r requirements.txt')
    reload_nginx()


def reload_nginx():
    """reloads nginx
    """
    sudo("service nginx reload")
