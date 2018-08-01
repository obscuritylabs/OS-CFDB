
# pull new findings 
git pull
# bring down old resources
docker-compose down
# clean old DB?
#  rm -rf data/mongo/*
# bring up new resources 
docker-compose up -d --build
# init new DB
docker exec -t site_cfdb-api_1 python /root/cfdb-api/init_mongo.py
