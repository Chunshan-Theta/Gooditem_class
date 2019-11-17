docker container stop container_goodclass_db_api
docker container rm container_goodclass_db_api
docker image rm image_goodclass_db_api
docker build --tag=image_goodclass_db_api .


# run
docker run -it -p 8080:8080  --name=container_goodclass_db_api image_goodclass_db_api
