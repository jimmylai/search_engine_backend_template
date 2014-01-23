#!/usr/bin/env python
# -*- encoding: utf8 -*-
'''Fabric functions
'''

import os
import sys
from fabric.api import run, sudo, prefix, local, env


__author__ = 'noahsark'


ENV_PATH = 'pyenv'
SOLR_DIR = 'solr-4.6.0'


def setup_env(env_path=ENV_PATH):
    '''Create virtualenv called pyenv'''
    if os.path.isdir(env_path) is False:
        local('virtualenv --no-site-packages %s' % env_path)

    with prefix('. %s/bin/activate' % env_path):
        local('pip install -r data/dependency_list.txt')

    if not os.path.isdir(SOLR_DIR) is False and not os.path.isfile('%s.tgz' % SOLR_DIR):
        local('wget http://www.carfab.com/apachesoftware/lucene/solr/4.6.0/solr-4.6.0.tgz')

    if not os.path.isdir(SOLR_DIR):
        local('tar -zvxf %s.tgz' % SOLR_DIR)


def run_django(port='8888'):
    '''Run django server'''
    with prefix('. %s/bin/activate' % ENV_PATH):
        with prefix('cd web'):
            local('python manage.py runserver 0.0.0.0:%s' % port)


def create_core(core_name):
    '''Create a new core in solr.'''
    local('cp -r data/solr_core_template solr_conf/%s' % core_name)
    with open('solr_conf/%s/core.properties' % core_name) as fp:
        lines = fp.readlines()

    string = ''.join(lines)
    string = string % core_name

    with open('solr_conf/%s/core.properties' % core_name, 'w') as fp:
        fp.write(string)


def run_solr(solr_main='%s/example' % SOLR_DIR, solr_home='%s/solr_conf' % os.getcwd(),
               solr_data='%s/solr_data' % os.getcwd(), port='8983'):
    '''Run Solr server'''
    if os.path.isdir(SOLR_DIR) is False:
        local('tar -zvxf %s.tgz' % SOLR_DIR)
    with prefix('cd %s' % solr_main):
        local('java -Dsolr.solr.home=%s -Djetty.port=%s -jar start.jar' % (solr_home, port))


def feed_data(core, fpath, port='8983'):
    '''Feed data to solr index'''
    url = 'http://localhost:%s/solr/%s/update' % (port, core)
    local("curl %s/json?commit=true --data-binary @%s -i -H 'Content-type:application/json'" % (
        url, fpath))
    local("curl %s?softCommit=true -i" % (url))
