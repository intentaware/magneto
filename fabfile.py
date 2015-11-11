import sys

from fabric.api import env, require, run, put, cd, task, settings as fabric_settings
from fabric.api import local as lrun
from fabric.contrib.console import confirm

from fabric.network import ssh
# ssh.util.log_to_file("paramiko.log", 10)

IMPORT_ERROR = 'Please add the location of \n DEPLOY_KEY, \n STAGE_KEY, \n LOCAL_PROJECT_PATH, \n LOCAL_ENVIRONMENT_PATH in adomattic.conf.fabric.variables'

#importing fabric specific variables
try:
    from adomattic.conf.fabric.variables import DEPLOY_KEY, STAGE_KEY, LOCAL_PROJECT_PATH, LOCAL_ENVIRONMENT_PATH
except ImportError:
    sys.exit(IMPORT_ERROR)



def local():
    """
    Environment settings for local.

    Usage:
         fab local <task>
    """
    env.run = lrun
    env.name = 'local'
    env.conf_path = 'local'
    env.project_root = LOCAL_PROJECT_PATH
    env.hosts = ['localhost']
    env.branch = 'develop'
    env.venv_root = LOCAL_ENVIRONMENT_PATH
    env.venv = 'source %(venv_root)sbin/activate && ' % env

def stage():
    """
    Environment Settings for Staging Server

    Usage:
        fab stage <task>
    """
    env.run = run
    env.name = 'adomattic-stage'
    env.conf_path = 'stage'
    env.project_root = '/srv/%(name)s/' % env
    env.hosts = ['stage.intentaware.com']
    env.user = 'root'
    env.key_filename = STAGE_KEY
    # env.no_keys = True
    # env.use_ssh_config = False
    env.branch = 'develop'
    env.venv_root = '/srv/%(name)s/' % env
    env.venv = 'source /srv/%(name)s/bin/activate && ' % env
    env.dashboard = '/srv/%(name)s/apps/dashboard/static/dash/' % env
    env.impressions = '/srv/%(name)s/apps/dashboard/static/impressions/' % env


def live():
    """
    Environment Settings for Staging Server

    Usage:
        fab live <task>
    """
    env.run = run
    env.name = 'adomattic-live'
    env.conf_path = 'live'
    env.project_root = '/srv/%(name)s/' % env
    env.hosts = ['52.32.191.6']
    env.user = 'ec2-user'
    env.key_filename = DEPLOY_KEY
    # env.no_keys = True
    # env.use_ssh_config = False
    env.branch = 'master'
    env.venv_root = '/srv/%(name)s/' % env
    env.venv = 'source /srv/%(name)s/bin/activate && ' % env
    env.dashboard = '/srv/%(name)s/apps/dashboard/static/dash/' % env
    env.impressions = '/srv/%(name)s/apps/dashboard/static/impressions/' % env


def app():
    """
    Environment Settings for Staging Server

    Usage:
        fab live <task>
    """
    env.run = run
    env.name = 'ia-live'
    env.conf_path = 'live'
    env.project_root = '/srv/%(name)s/' % env
    env.hosts = ['52.32.191.6']
    env.user = 'ec2-user'
    env.key_filename = DEPLOY_KEY
    # env.no_keys = True
    # env.use_ssh_config = False
    env.branch = 'master'
    env.venv_root = '/srv/%(name)s/' % env
    env.venv = 'source /srv/%(name)s/bin/activate && ' % env
    env.dashboard = '/srv/%(name)s/apps/dashboard/static/dash/' % env
    env.impressions = '/srv/%(name)s/apps/dashboard/static/impressions/' % env



def update_envs():
    """
    Updates local environment settings to the default repo settings, useful for parallel programming
    Usage:
        fab local update_envs
    """
    with cd(env.project_root):
        env.run('cp adomattic/conf/%(conf_path)s/settings.py adomattic/settings/local.py' % env)


def prepare():
    """
    For things that need to be installed via apt-get.
    These are installed before requirements.txt in the venv otherwise some python modules won't install properly
    """
    env.run('sudo apt-get update')
    env.run("sudo apt-get install locate python-setuptools git-core subversion mercurial htop screen byobu gcc")
    env.run('sudo apt-get install libjpeg62 libjpeg62-dev zlib1g-dev libfreetype6 libfreetype6-dev python-pycurl-dbg libcurl4-openssl-dev')
    env.run('sudo apt-get install build-essential libpq-dev python-dev')
    env.run('sudo apt-get install libxml2-dev libxslt-dev')
    env.run('sudo apt-get install nginx-full uwsgi uwsgi-plugin-python')
    env.run('sudo apt-get install python-pip')
    env.run('sudo apt-get install libreadline6 libreadline6-dev libncurses5-dev')
    env.run('sudo apt-get install libffi-dev libssl-dev')
    env.run('sudo pip install virtualenv')
    env.run('sudo apt-get install nodejs-legacy')
    env.run('sudo npm i -g bower gulp yo')

def yum():
    env.run('sudo yum -y update')
    env.run('sudo yum -y groupinstall "Development tools"')
    env.run('sudo yum -y install zlib-devel')
    env.run('sudo yum -y install python27-devel python27-tools')
    env.run('sudo yum -y install python27-pip')
    env.run('sudo yum -y install ibxml2-devel libxslt-devel geos')
    env.run('sudo yum install -y gcc openssl-devel libyaml-devel libffi-devel readline-devel zlib-devel gdbm-devel ncurses-devel')
    # Adding extra packages
    env.run('sudo yum-config-manager --enable epel')
    env.run('sudo yum -y install postgresql94-libs postgresql94-devel')
    env.run('sudo yum -y install nginx nodejs npm')
    #env.run('sudo yum -y install uwsgi uwsgi-plugin-python')
    env.run('sudo npm i -g bower gulp yo')


def virtualenv_setup():
    """
    The third step
    """
    env.run("virtualenv %(venv_root)s" % env)
    with cd(env.project_root):
        env.run("mkdir logs")
        env.run("touch logs/error-django.log")


def clone():
    """
    This second step of server setup
    """
    env.run("sudo mkdir %(project_root)s" % env)
    env.run("sudo chown -R ec2-user:ec2-user %(project_root)s" % env)
    env.run("git clone --recursive git@github.com:adomattic/Vader.git %(project_root)s" % env)


def git_pull():
    """
    pull from git
    Usage:
        fab <env> git_pull
    """
    with cd(env.project_root):
        env.run('git fetch;' % env)
        env.run('git checkout %(branch)s; git reset --hard origin/%(branch)s' % env)

def install_requirements():
    """
    install the environment python packages
    Usage:
        fab <env> install_requirements
    """
    with cd(env.project_root):
        env.run('%(venv)s pip install -r requirements.txt' % env)

def migrate():
    """
    migrates the database
    """
    with cd(env.project_root):
        env.run('%(venv)s python manage.py migrate' % env)

def collect_static():
    with cd(env.project_root):
        env.run('%(venv)s python manage.py collectstatic --noinput -i node_modules' % env)


def uwsgi_install():
    """
    first install of uwsgi
    """
    with cd(env.project_root):
        env.run('%(venv)s pip install uwsgi' % env)

def copy_nginx_conf():
    """
    update nginx settings for the site and make them available in sites-available
    """
    env.run('sudo cp /srv/%(name)s/adomattic/conf/%(conf_path)s/nginx/%(conf_path)s.conf /etc/nginx/sites-available/%(conf_path)s.conf' % env)


def restart_uwsgi():
    with cd(env.project_root):
        env.run('touch uwsgi/touch.py')


def npm():
    with cd(env.dashboard):
        env.run('npm install')
    with cd(env.impressions):
        env.run('npm install')


def bower():
    with cd(env.dashboard):
        env.run('bower install --allow-root')


def gulp():
    with cd(env.dashboard):
        env.run('gulp html')
    with cd(env.impressions):
        env.run('gulp adomattic:%(conf_path)s' % env)


def clean_pyc():
    with cd(env.project_root):
        env.run('find . -name "*.pyc" -exec rm -rf {} \;')

def get_ipdb():
    """
    gets the latest ipdb file from maxmind
    """
    with cd(env.project_root):
        env.run('mkdir adomattic/ipdb')
        env.run('wget -P adomattic/ipdb/ http://geolite.maxmind.com/download/geoip/database/GeoLite2-City.mmdb.gz')
        env.run('gunzip adomattic/ipdb/GeoLite2-City.mmdb.gz')

def deploy():
    """
    pull the latest from the repo, and deploy accordingly
    """
    git_pull()
    install_requirements()
    update_envs()
    migrate()
    bower()
    gulp()
    collect_static()
    restart_uwsgi()
