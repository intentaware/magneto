import sys

from fabric.api import env, require, run, put, cd, settings as fabric_settings
from fabric.api import local as lrun
from fabric.contrib.console import confirm