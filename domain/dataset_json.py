from dataset import Dataset
import pandas as pd


class DatasetJSON(Dataset):
    def __init__(self, ruta_archivo):
        super().__init__(ruta_archivo)


    def cargar_datos(self):
        try:
            df = pd.read_json(self.ruta_archivo)
            print("Se cargo el JSON")
            self.datos = df
            if self.validar_datos():
                self.transformar_datos()
            print(self.datos)
        except Exception as error:
            print(f"Error cargando JSON: {error}")

    def almacenar_datos_en_db(self):
        """Guardar los datos en una base de datos."""
        pass
    
"""
Ejemplo de uso:

dataset_json = DatasetJSON(ruta_archivo="files/ejemplo.json")

dataset_json.cargar_datos()
"""
