from os import path, listdir
import re
import pandas as pd
from typing import Callable

class FileReader:
  def __init__(self, download_path: str, year: int):
    self._download_path = download_path
    self.year = str(year)
    self._info_path = path.join(download_path, '1.LEIA-ME')
    self._info_filename = 'Dicion'
    self._data_path = path.join(download_path, '3.DADOS')
  
  def read_files(self):
    data_file = self._get_file_path(self._data_path, lambda f: re.search(self.year, f))
    self.data = pd.read_csv(data_file, sep=';')

    info_file = self._get_file_path(self._info_path, self._filter_info_file)
    self.info = pd.read_excel(info_file, 'DICIONÁRIO', header=1)

    self.cities = pd.read_excel(info_file, 'MUNICÍPIOS', header=3)
    self.cities.dropna(how='all', axis='columns')

  def _get_file_path(self, file_path: str, filter_function: Callable):
    files = listdir(file_path)
    data_filenames = list(filter(filter_function, files))
    return path.join(file_path, data_filenames[0])
  
  def _filter_info_file(self, filename: str):
    return re.search(re.escape(self._info_filename) + r'.*' + re.escape(self.year), filename, flags=re.A|re.I)