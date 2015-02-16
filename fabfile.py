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

def update_envs():
    '''
    Updates local environment settings to the default repo settings, useful for parallel programming
    Usage:
        fab local update_envs
    '''
    env.run('cp adomatic/conf/%(conf_path)s/settings.py adomatic/settings/local.py' % env)
