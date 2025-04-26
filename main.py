import pandas as pd
from sqlalchemy import create_engine

archive = 'data.xlsx'

df = pd.read_excel(archive, sheet_name=0)

user = ''
password = ''
host = ''
port = ''
db = ''
table = ''

engine = create_engine(f'postgresql+psycopg2://{user}:{password}@{host}:{port}/{db}')

df.to_sql(table, engine, if_exists='append', index=False)

print("Dados importados com sucesso!")