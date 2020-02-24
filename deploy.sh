#!/usr/bin/env bash

git rev-parse HEAD > rev.txt
git reset --hard
git pull -f
# docker network create  --subnet=172.41.20.0/24 djecommerce
docker stop djecommerce_py
docker rm djecommerce_py
docker build -t djecommerce_py/py:1 .

docker run -d --restart=always --network=djecommerce --ip=172.41.20.10 --name=djecommerce djecommerce_py/py:1
#docker exec --tty bakshieva_web python /app/manage.py makemigrations
#docker exec --tty bakshieva_web python /app/manage.py migrate
#docker exec --it bakshieva_web "/usr/local/bin/python /app/manage.py migrate"