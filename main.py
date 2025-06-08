from os import path
from data.data_saver import DataSaver
from domain.dataset_csv import DatasetCSV
from domain.dataset_json import DatasetJSON


# Ruta de los datasets
csv_path = path.join(path.dirname(__file__), "files/.csv")
json_path = path.join(path.dirname(__file__), "files/.json")

# Cargar los datasets y transformar los datos
csv = DatasetCSV(csv_path)
csv.cargar_datos()

json = DatasetJSON(json_path)
json.cargar_datos()

# Guardar en la base de datos
db = DataSaver()
db.guardar_dataframe(csv.datos, "")
db.guardar_dataframe(json.datos, "")