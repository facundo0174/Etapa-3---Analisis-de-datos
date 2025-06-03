import pandas as pd
from domain.dataset import Dataset
import requests
class DatasetAPI(Dataset):
    def __init__(self, source):
        super().__init__(source)

    def cargar_datos(self):
        try:
            response=requests.get(self.source)
            if response.status_code==200:
                df=pd.json_normalize(response.json())
                def es_lista(x):
                    return isinstance(x,list)
                def lista_a_string(x):
                    if isinstance(x, list):
                        return (','.join(map(str,x)))
                for col in df.columns:
                    if df[col].apply(es_lista).any():
                        df[col]=df[col].apply(lista_a_string)
                self.data=df
                print ("api cargada")
                if self.validar_datos():
                    self.transformar_datos()
            else:
                print("error cargar api de response")
        except Exception as e:
            print(f"error de api : {e}")