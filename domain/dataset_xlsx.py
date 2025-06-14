from domain.dataset import Dataset
import pandas as pd


class DatasetXLSX(Dataset):
    def __init__(self, ruta_archivo):
        super().__init__(ruta_archivo)


    def cargar_datos(self):
        try:
            df = pd.read_excel(self.ruta_archivo)
            print("Se cargo el archivo XLSX")
            self.datos = df
            if self.validar_datos():
                self.transformar_datos()
        except Exception as error:
            print(f"Error cargando archivo XLSX: {error}")