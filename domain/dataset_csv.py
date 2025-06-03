import pandas as pd
from domain.dataset import Dataset

class DatasetCSV(Dataset):
    def __innit__(self,source):
        super().__init__(source)

    def cargar_datos(self):
        try:
            df=pd.read_csv(self.source)
            self.data=df
            print("CSV cargado")
            if self.validar_datos():
                print("datos correctamente validados")
                self.transformar_datos()                
                
        except Exception as e:
            print(f"error cargando csv: {e}")