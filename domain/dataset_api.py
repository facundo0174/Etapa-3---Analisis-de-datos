import requests as rq
import pandas as pd
from domain.dataset import Dataset
class DatasetAPI(Dataset):
    def __init__(self ,source):
        super().__init__(source)

    def cargar_datos(self):
        try:
            rs=rq.get(self.source)
            if rs.status_code == 200:#codigos de paginas html 200 es ok
                df=pd.json_normalize(rs.json())#si es fisico el json esta en el disco sino se lo hace asi
            

                #si es lista devuelve verdadero
                def es_lista(colum):
                    return isinstance(colum,list)
                #transforma las columnas tipo list a comlumnas
                def list_string_converter(colum):
                    if isinstance(colum,list):
                        return ", ".join(map(str,colum))
                
                for col in df.columns:
                    if df[col].apply(es_lista).any():
                        df[col]=df[col].apply(list_string_converter)
                self.data=df
                print("API cargada")
                if self.validar_datos():
                    self.transformar_datos()
            else:
                print("error obpencion de api")

        except Exception as e:
            print(f"Error API. {e}")
    """
    ejemplos de procesamiento de api
    import pandas as pd
import requests

def cargar_datos(self):
    try:
        rs = requests.get(self.source)
        if rs.status_code == 200:
            # Normalizar datos y separar diccionarios anidados
            df = pd.json_normalize(rs.json(), sep="_")

            # Convertir listas en múltiples filas en lugar de texto plano
            for col in df.columns:
                if df[col].apply(lambda x: isinstance(x, list)).any():
                    df = df.explode(col)

            self.data = df
            print("API cargada")

            if self.validar_datos():
                self.transformar_datos()
        else:
            print("Error obteniendo API")

    except Exception as e:
        print(f"Error API. {e}")

    """