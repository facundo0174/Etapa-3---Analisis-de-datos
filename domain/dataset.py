from abc import ABC,abstractmethod

class Dataset(ABC):
    def __init__(self, source):# clase abstracta que es el nexo de la comunicacion con el archivo a analizar(filePath=source)
        self.__source=source
        self.__data=None
        pass
    
    @property
    def datos(self):
        #getter
        return(self.__datos)

    @datos.setter
    def datos(self, value):
        #validaciones
        self.__datos=value

    @abstractmethod
    def cargar_datos(self):
        pass

    def definir_datos(self):
        pass

    def validar_datos(self):
        pass

    def transformar_datos(self):
        pass

    def mostrar_resumen(self):
        pass

    
