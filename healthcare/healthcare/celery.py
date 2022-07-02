import os

from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'healthcare.settings')

app = Celery('healthcare', broker='redis://localhost:6379',
             include=['healthcare.tasks'])

if __name__ == '__main__':
    app.start()
