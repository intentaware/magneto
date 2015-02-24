import sys

from fabric.api import env, require, run, put, cd, task, settings as fabric_settings
from fabric.api import local as lrun
from fabric.contrib.console import confirm

IMPORT_ERROR = 'Please add the location of \n DEPLOY_KEY, \n STAGE_KEY, \n LOCAL_PROJECT_PATH, \n LOCAL_ENVIRONMENT_PATH in adomatic.conf.fabric.variables'

#importing fabric specific variables
try:
    from adomatic.conf.fabric.variables import DEPLOY_KEY, STAGE_KEY, LOCAL_PROJECT_PATH, LOCAL_ENVIRONMENT_PATH
except ImportError:
    sys.exit(IMPORT_ERROR)



def local():
    '''
    Environment settings for local.

    Usage:
         fab local <task>
    '''
    env.run = lrun
    env.name = 'local'
    env.conf_path = 'local'
    env.project_root = LOCAL_PROJECT_PATH
    env.hosts = ['localhost']
    env.branch = 'dev'
    env.venv_root = LOCAL_ENVIRONMENT_PATH
    env.venv = 'source %(venv_root)sbin/activate && ' % env

def stage():
    '''
    Environment Settings for Staging Server

    Usage:
        fab stage <task>
    '''
    env.run = run
    env.name = 'adomattic-stage'
    env.conf_path = 'stage'
    env.project_root = '/srv/%(name)s/' % env
    env.hosts = ['app.adomattic.com']
    env.user = 'root'
    env.key_filename = DEPLOY_KEY
    env.branch = 'dev'
    env.venv_root = '/srv/%(name)s/' % env
    env.venv = 'source /srv/%(name)s/bin/activate && ' % env
    #env.backoffice = '/srv/%(name)s/apps/backoffice/static/backoffice/' % env



def update_envs():
    '''
    Updates local environment settings to the default repo settings, useful for parallel programming
    Usage:
        fab local update_envs
    '''
    env.run('cp adomatic/conf/%(conf_path)s/settings.py adomatic/settings/local.py' % env)


def prepare():
    """
    For things that need to be installed via apt-get.
    These are installed before requirements.txt in the venv otherwise some python modules won't install properly
    """
    env.run('sudo apt-get update')
    env.run("sudo apt-get install locate python-setuptools git-core subversion mercurial htop screen byobu gcc")
    env.run('sudo apt-get install libjpeg62 libjpeg62-dev zlib1g-dev libfreetype6 libfreetype6-dev python-pycurl-dbg libcurl4-openssl-dev')
    env.run('sudo apt-get install libpq-dev python-dev')
    env.run('sudo apt-get install libxml2-dev libxslt-dev')
    env.run('sudo apt-get install nginx-full uwsgi uwsgi-plugin-python')
    env.run('sudo apt-get install python-pip')
    env.run('sudo apt-get install libreadline6 libreadline6-dev libncurses5-dev')
    env.run('sudo pip install virtualenv')
    env.run('sudo apt-get install nodejs-legacy')
    env.run('sudo npm i -g bower gulp yo')
