from abc import ABC, abstractmethod, abstractproperty


class Vehiculo(ABC):
    def __init__(
            self,
            color='undefined',
            marca='undefined',
            modelo='undefined'
    ):
        self.__color = color
        self.__marca = marca
        self.__modelo = modelo

    @property
    def color(self) -> str:
        return self.__color

    @color.setter
    def color(self, color: str) -> None:
        self.__color = color

    @property
    def marca(self) -> str:
        return self.__marca

    @marca.setter
    def marca(self, marca: str) -> None:
        self.__marca = marca

    @property
    @abstractmethod
    def modelo(self):
        pass

    @modelo.setter
    @abstractmethod
    def modelo(self, modelo):
        pass

    @abstractmethod
    def arrancar(self, value: int) -> bool:
        pass

    @abstractmethod
    def acelerar(self, value: int) -> bool:
        pass

    @abstractmethod
    def frenar(self, value: int) -> bool:
        pass

    @abstractmethod
    def apagar(self, value: int) -> bool:
        pass
