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
docker-compose exec cfdb-api git clone https://github.com/obscuritylabs/OS-CFDB.git /root/OS-CFDB/
docker-compose exec cfdb-api python /root/cfdb-api/init_mongo.py /root/OS-CFDB/
