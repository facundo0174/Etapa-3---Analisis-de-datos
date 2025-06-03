import pandas as pd
from sqlalchemy import create_engine #inicializador de ORM
from sqlalchemy.exc import SQLAlchemyError # errores para BD
from decouple import config #para leer variables de entonrno

class DataSaver:

    def __init__(self):
        user =config('DB_USER')
        password = config ('DB_PASSWORD')
        host = config('DB_HOST')
        port = config ('DB_PORT')
        database=config ('DB_NAME')
        url=f"mysql+pymysql://{user}:@{host}:{port}/{database}"# se quito {password} ya que al ser local la conexion no necesita comprobacion de usuario
        # en un entorno real remoto si necesita antes de @ password, el SO por default usa password de manera local,
        self.engine= create_engine(url )

    def save_df(self,df,table_name):
        if df is None:
            print (f"no se puede guarda datos nulos para {table_name}")
            return None
        if not isinstance(df, pd.DataFrame):
            print (f"tipo invalido, se esperaba un dataframe de pandas, se recibio{type(df)}")

        try:#guada todo lo que trae de la api
            df.to_sql(name=table_name, con=self.engine, if_exists='replace', index=False)
            print(f"datos guardados exitosamente en tabla {table_name} sql en db")


        except SQLAlchemyError as e:
            print(f"error guardando datos {e}")            