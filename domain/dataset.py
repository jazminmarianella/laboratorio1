

from abc import ABC, abstractmethod


class Dataset(ABC):
    def __init__(self, ruta_archivo):
        self.__ruta_archivo =  ruta_archivo
        self.__datos = None

    @property
    def datos(self):
        # aca se puede hacer procesamiento del dato
        return self.__datos

    @datos.setter
    def datos(self, valor):
        # Aca se harian las validaciones antes de cargar el dato
        self.__datos = valor

    @property
    def ruta_archivo(self):
        return self.__ruta_archivo
    
    @abstractmethod
    def cargar_datos(self):
        """Cargar datos desde un archivo."""
        pass

    def validar_datos(self):
        """Validar los datos cargados."""
        if self.datos is None:
            raise ValueError("Datos no cargados")

        if self.datos.isnull().sum().sum() > 0:
            #Existen datos nulos
            print("Datos faltantes detectados")
        if self.datos.duplicated().sum() > 0:
            #Existen filas duplicados
            print("Datos duplicados detectados")
        #Retorna True si hay que 
        return True
    
    def transformar_datos(self):
        """Realiza transformaciones en base a validaciones previas"""
        if self.datos is not None:
            #Convierte columnas a minuscula y con _
            self.__datos.columns = self.datos.columns.str.lower().str.replace(" ", "_")
            self.__datos = self.__datos.drop_duplicates()
            for col in self.datos.select_dtypes(include='object').columns:
                #['detalles','direccion','hobbies']
                self.__datos[col] = self.datos[col].astype(str).str.strip()
            print("Transformaciones aplicadas")
        else:
            print("No hay datos para transformar")
    

    @abstractmethod
    def almacenar_datos_en_db(self):
        """Guardar los datos en una base de datos."""
        pass
    
