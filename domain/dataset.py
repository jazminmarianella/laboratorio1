


from abc import ABC, abstractmethod

class Dataset(ABC):
    def __init__(self, ruta_archivo):
        self.__ruta_archivo =  ruta_archivo
        self.__datos = None

    @property
    def datos(self):
        # aca se puede hacer procesamiento del dato
        return self.__datos

    @property
    def ruta_archivo(self):
        return self.__ruta_archivo

    """
    @abstractmethod
    def cargar_datos(self):
  
        pass

    @abstractmethod
    def validar_datos(self):

        pass

    @abstractmethod
    def almacenar_datos_en_db(self):

        pass
    """


mi_dataset = Dataset(ruta_archivo='ejemplo')


print(mi_dataset.ruta_archivo)