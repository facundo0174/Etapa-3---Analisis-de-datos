import pandas as pd
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy import create_engine
from decouple import config

class DataSaver():
    def __init__(self):
        user=config('DB_USER')
        password=config('DB_PASSWORD')
        host=config('DB_HOST')
        port=config('DB_PORT')
        db=config('DB_NAME')

        url = f"mysql+pymysql://{user}:{password}@{host}:{port}/{db}"#localmente no usa contraseña asi que ojo
        self.engine=create_engine(url)


    def guardar_dataframe(self, df, table_name):
        if df is None:
            print(" datos vacios en df")
            return
        
        if not isinstance(df, pd.DataFrame):
            print(f"error df no valido del tipo pandas, se recibio {type(df)}")
            return
        try:
            df.to_sql(name=table_name, con=self.engine, if_exists='replace', index=False)
            print("datos cargados correctamente")

        except SQLAlchemyError as e:
            print(f'error al intentar cargar datos, el error es: {e}')
