FROM python:3

ENV C_FORCE_ROOT true

ENV PROD_TYPE production
ENV HOST 0.0.0.0
ENV PORT 5000
ENV DEBUG false
ENV MONGODB_URL mongodb://mongo:27017
ENV REDIS_RATELIMIT_STORAGE_URL redis://redis:6379/0
ENV CACHE_REDIS_URL redis://redis:6379/0

RUN pip install flask && \
    pip install uwsgi && \
    pip install pymongo && \
    pip install psutil && \
    pip install flask_limiter && \
    pip install redis && \
    pip install Flask-Caching && \
    pip install flask_apscheduler

RUN git clone https://github.com/obscuritylabs/OS-CFDB.git /root/OS-CFDB/

#RUN python '/root/cfdb-api/init_mongo.py' /root/OS-CFDB/

ENTRYPOINT ["uwsgi", "--ini", "/root/cfdb-api/uwsgi.ini"]