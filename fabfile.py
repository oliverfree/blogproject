#coding=utf-8

from fabric.api import env, run
from fabric.operations import sudo

GIT_REPO = "you git repository" ① 

env.user = 'you host username' ②
env.password = 'you host password'

# 填写你自己的主机对应的域名
env.hosts = ['demo.zmrenwu.com']

# 一般情况下为 22 端口，如果非 22 端口请查看你的主机服务提供商提供的信息
env.port = '22'


def deploy():
    source_folder = '/home/yangxg/sites/zmrenwu.com/django-blog-tutorial' ③

    run('cd %s && git pull' % source_folder) ④
    run("""
        cd {} &&
        ../env/bin/pip install -r requirements.txt &&
        ../env/bin/python3 manage.py collectstatic --noinput &&
        ../env/bin/python3 manage.py migrate
        """.format(source_folder)) ⑤ 
    sudo('restart gunicorn-demo.zmrenwu.com') ⑥
    sudo('service nginx reload')
