from elasticsearch import Elasticsearch
from elasticsearch.helpers import bulk
HOST = "https://localhost:9200"
ELASTIC_USER = "elastic"
# The password for the 'elastic' user generated by Elasticsearch
ELASTIC_PASSWORD = "-JpPuDA43hk+xp*OYAPq"
# The path of ca certificates
CA_CERTS = "C:/UTEXLMS/Nam3_2022_2023/HK2/TruyTimThongTin/elasticsearch-8.6.2/config/certs/http_ca.crt"

DEV="NGOCPHAT"

if DEV=="NGOCPHAT":
    ELASTIC_PASSWORD = "AO_Xpp=erLN89MGxutL7"
    CA_CERTS="P:/Programming/JAVA/Enviroment/elasticsearch-8.6.2-windows-x86_64/elasticsearch-8.6.2/config/certs/http_ca.crt"


# Create the client instance
es = Elasticsearch(
    hosts=HOST,
    ca_certs=CA_CERTS,
    http_auth=(ELASTIC_USER, ELASTIC_PASSWORD),
)

# Define index name of project
index_name = 'finalproject_index'
type_name = "_search"