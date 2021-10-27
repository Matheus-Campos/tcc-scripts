from sqlalchemy import create_engine
import pandas as pd

class DatabaseWriter:
  def __init__(self, connection_url: str, year: int):
    self._connection_url = connection_url
    self._connection = None
    self.year = str(year)
  
  def open_connection(self):
    if self._connection is None:
      self._connection = create_engine(self._connection_url)
    return self._connection    

  def write_to_database(self, dataframe: pd.DataFrame, tablename: str):
    dataframe.to_sql(f'{tablename}_{self.year}', self._connection, index=False, if_exists='replace')
  
  def close_connection(self):
    self._connection.dispose()
    self._connection = None

  def __enter__(self):
    self.open_connection()
    return self
  
  def __exit__(self, type, value, traceback):
    self.close_connection()