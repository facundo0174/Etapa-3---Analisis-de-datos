from os import path
from domain.dataset_csv import DatasetCSV
from domain.dataset_exel import DatasetEXEL

#ruta del archivo a analizar
csv_path=path.join(path.dirname(__file__),"files/w_mean_prod.csv")
exel_path=path.join(path.dirname(__file__),"files/ventas.xlsx")
#carga y transformacion de informacion
csv = DatasetCSV(csv_path)
csv.cargar_datos()

exel = DatasetEXEL()


#resguardo de datos en alguna db o disco

