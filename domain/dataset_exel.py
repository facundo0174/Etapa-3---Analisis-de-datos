import pandas as pd
from domain.dataset import Dataset

class DatasetEXEL(Dataset):
    def __innit__(self,source):
        super().__init__(source)

    def cargar_datos(self):
        try:
            df=pd.read_excel(self.source)
            self.data=df
            print("EXEL cargado")
            if self.validar_datos():
                print("datos correctamente validados")
                
                
        except Exception as e:
            print(f"error cargando EXEL: {e}")