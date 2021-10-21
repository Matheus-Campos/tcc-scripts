from os import getenv
from database_writer import DatabaseWriter
from file_reader import FileReader

def main():
  download_path = getenv('DOWNLOAD_PATH', 'data')
  year = 2019
  file_reader = FileReader(download_path, year)

  db_url = getenv('DATABASE_URL', f'postgresql://postgres:postgrespassword@postgres')
  with DatabaseWriter(db_url, year) as db_writer:
    db_writer.write_to_database(file_reader.data, 'questionario')

if __name__ == '__main__':
  main()