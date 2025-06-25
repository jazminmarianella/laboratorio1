from os import path, listdir
from data.data_saver import DataSaver
from domain.dataset_csv import DatasetCSV
from domain.dataset_json import DatasetJSON
from domain.dataset_xlsx import DatasetXLSX

# Cargar los datasets y transformar los datos
db_saver = DataSaver()

#Por cada archivo del directorio files, se crea un objeto segun la extension del archivo
for file in listdir("files/"):
    file_path = path.join("files", file)
    if file.endswith('.csv'):
        dataset = DatasetCSV(file_path)
    elif file.endswith('.json'):
        # Se define un esquema para el JSON, a modo de ejemplo
        dataset = DatasetJSON(file_path,
                              schema={"nombre": "object",
                                       "edad": "int64",
                                        "ciudad": "object"}
                            )
    elif file.endswith('.xlsx'):
        dataset = DatasetXLSX(file_path)
    else:
        print(f"Archivo {file} no soportado")
        continue
    
    # Cargar los datos
    dataset.cargar_datos()
    #Guardar los datos en la base de datos
    nombre_tabla = file.split('.')[0].lower()
    db_saver.guardar_dataframe(dataset.datos, nombre_tabla)
    print('------------------------------------------')