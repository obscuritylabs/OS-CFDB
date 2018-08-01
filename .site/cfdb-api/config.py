import os
from apscheduler.jobstores.redis import RedisJobStore

def print_me():
    print('me')

DEBUG = bool(os.environ.get('DEBUG', True))
MONGODB_URL = str(os.environ.get('MONGODB_URL', 'mongodb://127.0.0.1:27017'))
KEY = str(os.environ.get('KEY', 'c3O0KYVdpG3717QNB7bcMvl0711fJG3v'))
RATELIMIT_STORAGE_URL = str(os.environ.get('REDIS_RATELIMIT_STORAGE_URL', 'redis://127.0.0.1:6379/0'))
CACHE_TYPE = str(os.environ.get('CACHE_TYPE', 'redis'))
CACHE_REDIS_URL = str(os.environ.get('CACHE_REDIS_URL', 'redis://127.0.0.1:6379/0'))



JOBS = [
        {
            'id': 'print_job',
            'func': print_me,
            'trigger': 'interval',
            'seconds': 10,
            'replace_existing': True
        }
    ]
SCHEDULER_JOBSTORES = {
        'default': RedisJobStore()
    }
SCHEDULER_API_ENABLED = True

