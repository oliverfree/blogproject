from fabric.api import env, run
from fabric.operations import sudo

GIT_REPO = "https://github.com/oliverfree/blogproject.git" 

env.user = 'daniel' 
env.password = 'Dengyu8403'


env.hosts = ['doraemon.red']


env.port = '22'


def deploy():
    source_folder = '/home/daniel/sites/doraemon.red/blogproject' 

    run('cd %s && git pull' % source_folder) 
    run("""
        cd {} &&
        ../env/bin/pip install -r requirements.txt &&
        ../env/bin/python3 manage.py collectstatic --noinput &&
        ../env/bin/python3 manage.py migrate
        """.format(source_folder)) 
    sudo('restart gunicorn-doraemon.red') 
    sudo('service nginx reload')
