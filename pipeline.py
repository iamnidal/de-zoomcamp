import sys

import pandas as pd 


URL=""
# python ingest_data \
#     --user= root \
#     --password=nidal \
#     --host=localhost\
#     --port=5432\
#     --db==ny_taxi\
#     --table_name=yellow_taxi__data\
#     --url={URL}\

# URL="http://172.23.96.1:8000/"
# docker run -it --network=pg-network taxi_ingest:v001 --user=root --password=nidal --host=pg-database --port=5432 --db==ny_taxi --table_name=yellow_taxi__data --url="http://172.23.96.1:8000/yellow_tripdata_2021-01.csv" 
    

    

# docker run -it -e POSTGRES_USER="root" -e POSTGRES_PASSWORD="root" -e POSTGRES_DB="ny_taxi" -v D:\DatumLabs\Data-Engineering\my_taxi_postgre_data:/var/lib/postgresql/data -p 5432:5432 postgres:13