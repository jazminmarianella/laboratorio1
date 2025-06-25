

from abc import ABC, abstractmethod
import pandas as pd

class Dataset(ABC):
    def __init__(self, ruta_archivo, schema: dict = None):
        self.__ruta_archivo =  ruta_archivo
        self.__schema = schema
        self.__datos = None

    @property
    def datos(self):
        return self.__datos

    @datos.setter
    def datos(self, valor):
        self.__datos = valor

    @property
    def ruta_archivo(self):
        return self.__ruta_archivo
    
    @property
    def schema(self):
        return self.__schema
    
    @abstractmethod
    def cargar_datos(self):
        """Cargar datos desde un archivo."""
        pass

    def validar_datos(self):
        """Validar los datos cargados."""
        # Verifica si los datos han sido cargados
        if self.datos is None:
            raise ValueError("Datos no cargados")
               
        # Verifica si los datos tienen el tipo correcto
        if not isinstance(self.datos, pd.DataFrame):
            raise TypeError("Los datos deben ser un DataFrame de pandas")

        # Verifica si el DataFrame esta vacio
        if self.datos.empty:
            raise ValueError("El DataFrame esta vacio")
 
        if self.datos.isnull().sum().sum() > 0:
            #Existen datos nulos
            print("Datos faltantes detectados")
        if self.datos.duplicated().sum() > 0:
            #Existen filas duplicados
            print("Datos duplicados detectados")

        if self.schema is not None:
            #Validar el esquema de los datos
            for col, tipo in self.schema.items():
                if col not in self.datos.columns:
                    raise ValueError(f"La columna '{col}' no existe en los datos")
                if str(self.datos[col].dtype) != tipo:
                    raise TypeError(f"La columna '{col}' debe ser de tipo {tipo}")
        return True
    
    def transformar_datos(self):
        """Realiza transformaciones en base a validaciones previas"""
        if self.datos is not None:
            # Reemplaza espacios en los nombres de las columnas por guiones bajos y convierte a minúsculas
            self.__datos.columns = self.datos.columns.str.lower().str.replace(" ", "_")
            # Elimina filas duplicadas
            self.__datos.drop_duplicates(inplace=True)
            # Convierte todas las columnas de tipo object a str y elimina espacios en blanco al inicio y al final
            for col in self.datos.select_dtypes(include='object').columns:
                self.__datos[col] = self.datos[col].astype(str).str.strip()
            
            #Elimina filas con datos nulos
            self.__datos = self.datos.dropna(how='all')


            print("Transformaciones aplicadas")
        else:
            print("No hay datos para transformar")
