import os
import pandas as pd
from pyathena import connect
from .config import REGION, S3_STAGING, DB_ATHENA

def get_athena_connection(work_group="primary"):
    return connect(
        s3_staging_dir=S3_STAGING,
        region_name=REGION,
        work_group=work_group
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

