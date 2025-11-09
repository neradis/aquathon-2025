import os

import pandas as pd
import sqlalchemy

from os import path as osp
from pandas import DataFrame


this_dir = osp.dirname(__file__)
project_root: str = osp.dirname(this_dir)

pd.options.display.width = 0

production_vosges_csv = osp.join(project_root, 'production_vosges.csv')


def cleanup(df: DataFrame) -> DataFrame:
    df['dt'] = pd.to_datetime(df['t'], format='ISO8601')
    df = df.rename(columns={'sin_org': 'actual'})
    return df[['dt', 'actual', 'xgboost']]

def get_production_data() -> DataFrame:
    production_vosges_raw: DataFrame = pd.read_csv(production_vosges_csv)
    return cleanup(production_vosges_raw)

def retrieve_conn_string(in_colab: bool = False) -> str:
    if in_colab:
        from google.colab import userdata
        # Secrets in colab notebooks have a too restrictive site limit to have the DB password
        # directly part of the `conn_str` secret. Workaround: Store the long password in a second
        # secret and use `DBPW` as insertion marker
        return userdata.get('conn_str').replace('DBPW', userdata.get('db_pw'))
    else:
        import dotenv
        dotenv.load_dotenv(os.path.join(this_dir, '.env'))
        return os.environ['SCALINGO_PG_CONN_STRING']

def upload_to_db(df: DataFrame, name: str, schema: str | None = None, in_colab: bool = False) -> None:
    conn_str = retrieve_conn_string(in_colab)
    engine = sqlalchemy.create_engine(conn_str, pool_size=4)
    production_vosges.to_sql('production', engine, schema='vosges', if_exists='replace', chunksize=100)

def load_from_db(in_colab: bool = False) -> DataFrame:
    conn_str = retrieve_conn_string(in_colab)
    engine = sqlalchemy.create_engine(conn_str, pool_size=4)
    return pd.read_sql('SELECT * FROM vosges.production', engine)

if __name__ == '__main__':
    production_vosges = get_production_data()
    print('DB upload start')
    upload_to_db(production_vosges, 'production', schema='vosges')
    print('DB upload finished')
    print(load_from_db())