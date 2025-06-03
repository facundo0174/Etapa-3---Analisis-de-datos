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
            raise ValueError("datos no cargados")#termina el bloque de codigo y devuelve falso
        if self.data.isnull().sum().sum()>0:
            print("se han encontrado valores nulos en el archivo")
        if self.data.duplicated().sum()>0:
            print("filas duplicadas detectadas")
        return True


    def transformar_datos(self):
        if self.data is not None:
            self.__data.columns=self.data.columns.str.lower().str.replace(" ","_")
            #remplaza a minusculas y los espacios por _ en strings on en numeros o objetos
            self.__data = self.data.drop_duplicates()#elimina datos duplicados
            for col in self.data.select_dtypes(include="object").columns:
                '''recupera los datos del dataset discriminando columnas segun el reconocimiento de objetos
                en el caso de la api geografica del estado, las listas, diccionarios contenidos son objetos para python y pandas
                por lo tanto se discriminan de esa manera, quedando los datos ordenados de manera tal que las filas posean todos los 
                datos pertinentes a 1 sola provincia, contrariamente si no se lo hace quedara informacion imposible de recorrer o 
                muy intrincada de hacerlo'''
                self.__data[col] = self.data[col].astype(str).str.strip()
            print("transformaciones aplicadas")
        else:
            raise ValueError("datos no cargados, no es posible la transformacion")


    def mostrar_resumen(self):
        return(print(self.data.describe(include="all") if self.data is not None else"no hay datos"))


    
