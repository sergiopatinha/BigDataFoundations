import os
import pandas as pd
from pyathena import connect
from .config import REGION, S3_STAGING, DB_ATHENA

def get_athena_connection(work_group="primary"):
    return connect(
        s3_staging_dir=S3_STAGING,
        region_name=REGION,
        work_group=work_group,
        schema_name=DB_ATHENA,
        aws_access_key_id=os.getenv("AWS_ACCESS_KEY_ID"),
        aws_secret_access_key=os.getenv("AWS_SECRET_ACCESS_KEY"),
        aws_session_token=os.getenv("AWS_SESSION_TOKEN"),
    )

def read_sql_df(sql, conn=None):
    close = False
    if conn is None:
        conn = get_athena_connection()
        close = True
    df = pd.read_sql(sql, conn)
    if close:
        conn.close()
    return df

