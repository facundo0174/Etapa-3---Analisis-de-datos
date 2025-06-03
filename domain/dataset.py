from abc import ABC,abstractmethod

class Dataset(ABC):
    def __init__(self, source):# clase abstracta que es el nexo de la comunicacion con el archivo a analizar(filePath=source)
        self.__source=source
        self.__data=None
        pass
    
    @property
    def data(self):
        #getter y procesar
        return(self.__data)
    @property
    def source(self):
        return (self.__source)

    @data.setter
    def data(self, value):
        #validaciones
        self.__data=value

    @abstractmethod
    def cargar_datos(self):
        pass

    def definir_datos(self):
        pass

    def validar_datos(self):
        if self.data is None:
            raise ValueError("datos no cargados")
        if self.data.isnull().sum().sum()>0:
            print("datos  faltantes detectados")
        if self.data.duplicated().sum()>0:
            print("filas duplicadas detectadas")
        return True


    def transformar_datos(self):
        pass

    def mostrar_resumen(self):
        pass

    
