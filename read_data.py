import time
import re
from os import scandir, getenv
from sqlalchemy import create_engine
import pandas as pd

db_url = getenv('DB_URL', 'postgresql://postgres:postgrespassword@localhost:5432/postgres')
engine = create_engine(db_url)

dir_path = getenv('DATA_PATH', 'data')

with scandir(dir_path) as files:
  for file in files:
    start = time.time()
    df = pd.read_csv(file.path, sep=';')
    year = re.search(r'\d+', file.name).group(0)
    df.to_sql(f'answers_{year}', engine, index=False, if_exists='replace')
    end = time.time()
    print(f'{file.name} processed in {end - start} seconds.')
