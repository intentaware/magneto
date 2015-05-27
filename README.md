# Whats with the name?
**Force Choke**, *'I find your lack of faith disturbing!'*

# Lets get the show on the road

## Pre Requisites
make sure you have these packages on your system

1. node & npm
2. postgres 9.4 (important, 9.4 is version is a must)
3. gulp & bower (npm install -g gulp bower)

## Setting your development environment
You know virtualenv, right? MAKE ONE and switch to it!

```bash
git clone git@github.com:adomattic/Vader.git && cd Vader
pip install -r requirements.txt
touch adomatic/conf/fabric/variables.py
```

the last command creates your fabric variables i.e. automate the crap out of this thing, edit this file in your favourite editor, and make your have the paths to these set accordingly

```python
DEPLOY_KEY = 'path to the live ssh key, if you have access i.e.'
STAGE_KEY = 'path to the dev ssh key, again, if you have access'
LOCAL_PROJECT_PATH = 'your local project path'
LOCAL_ENVIRONMENT_PATH = 'you virtual environment path'
```

one you have this set up, this is the magic command you run first before you can tame this monster

```bash
fab local update_envs
```

## The GIT branching structure
best that we follow the `git flow` model. Branches and their roles are as follow

- `master` > major releases, tagged by version number. version number is YY.MM.DD
- `develop` > major development branch, used for staging
- `feature/name` > we branch out from developing before developing a feature so that come back and checkout master to do hot-fixes
- `hot-fix/name` > for fixing stuff when things are live and we need to iron out minor kinks, this allows to leave our feature development on a seperate path

seriously, if you are not using git-flow plug uptil now, you MUST!

## UI/UX

everything frontend related is at the directory 'apps/dashboard/static/

with each function of ui having a seperate folder e.g

1. dash > everything related to dashboard
2. emails > to generate email friendly templates
3. impressions > standalone javascript files for serving impressions

to watch the static files which working on dashboard, we would need gulp with browser-sync which proxies django local development server. Do this

```bash
cd apps/dashboard/static/dash/
npm install
bower install
gulp serve
```

npm install read package.json, while bower install reads bower.json.
