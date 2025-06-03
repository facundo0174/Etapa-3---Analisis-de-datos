from os import path
from domain.dataset_csv import DatasetCSV
from domain.dataset_exel import DatasetEXEL
from domain.dataset_api import DatasetAPI
from data.data_saver import DataSaver



#ruta del archivo a analizar
csv_path=path.join(path.dirname(__file__),"files/w_mean_prod.csv")
exel_path=path.join(path.dirname(__file__),"files/ventas.xlsx")
#carga y transformacion de informacion
csv = DatasetCSV(csv_path)
csv.cargar_datos()

exel = DatasetEXEL(exel_path)
exel.cargar_datos()

api = DatasetAPI("https://apis.datos.gob.ar/georef/api/provincias")

#resguardo de datos en alguna db o disco
db=DataSaver()
db.save_df(csv.data, "w_mean_prod_csv")
db.save_df(exel.data,"ventas")