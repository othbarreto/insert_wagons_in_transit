import pandas as pd
from sqlalchemy import create_engine

archive = 'data.xlsx'

df = pd.read_excel(archive, sheet_name=0)

USER = ''
PASSWORD = ''
HOST = ''
PORT = ''
DB = ''
TABLE = ''

engine = create_engine(f'postgresql+psycopg2://{USER}:{PASSWORD}@{HOST}:{PORT}/{DB}')

df.to_sql(TABLE, engine, if_exists='append', index=False)

print("Dados importados com sucesso!")