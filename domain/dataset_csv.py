from domain.dataset import Dataset
import pandas as pd


class DatasetCSV(Dataset):
    def __init__(self, ruta_archivo, schema: dict = None):
        super().__init__(ruta_archivo, schema)


    def cargar_datos(self):
        try:
            df = pd.read_csv(self.ruta_archivo)
            print("Se cargo el archivo CSV")
            self.datos = df
            if self.validar_datos():
                self.transformar_datos()
        except Exception as error:
            print(f"Error cargando archivo CSV: {error}")
    