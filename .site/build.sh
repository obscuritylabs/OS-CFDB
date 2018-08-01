# pull new findings 
git pull

# bring down old resources
docker-compose down

# clean old DB?
rm -rf data/mongo/*

# bring up new resources 
# docker-compose build --force-rm --no-cache --pull  
docker-compose up -d

# init new DB
docker exec -t site_cfdb-api_1 git clone https://github.com/obscuritylabs/OS-CFDB.git /root/OS-CFDB/
docker exec -t site_cfdb-api_1 python /root/cfdb-api/init_mongo.py /root/OS-CFDB/
