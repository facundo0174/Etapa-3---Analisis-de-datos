from os import path
from domain.dataset_csv import DatasetCSV
from domain.dataset_exel import DatasetEXEL
from data.data_saver import DataSaver
from domain.dataset_api import DatasetAPI

#ruta del archivo a analizar
csv_path=path.join(path.dirname(__file__),"files/w_mean_prod.csv")
exel_path=path.join(path.dirname(__file__),"files/ventas.xlsx")
#carga y transformacion de informacion
csv = DatasetCSV(csv_path)
csv.cargar_datos()

exel = DatasetEXEL()
exel.cargar_datos()


#api=DatasetAPI(url)


#resguardo de datos en alguna db o disco
db=DataSaver()
db.guardar_dataframe(exel.data,"ventas exel")
db.guardar_dataframe(csv.data,"datosCSV")
