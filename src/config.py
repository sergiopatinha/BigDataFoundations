import os
from dotenv import load_dotenv

# carregar variáveis do ficheiro .env
load_dotenv()

REGION = os.getenv("AWS_DEFAULT_REGION", "us-east-1")
S3_STAGING = os.getenv("S3_STAGING", "s3://bdf25-20-movielens/results/")
DB_ATHENA = "movielens1m"
