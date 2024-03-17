from abc import ABC, abstractmethod
from error import SubTipoInvalidoError  # Importamos la excepción desde error.py

class Anuncio(ABC):
    """
    Clase abstracta que define la estructura base de un anuncio.
    """
    def __init__(self, ancho: int, alto: int, url_archivo: str, url_click: str, sub_tipo: str) -> None:
        """
        Inicializa un anuncio con sus atributos básicos.

        Args:
            ancho (int): Ancho del anuncio.
            alto (int): Alto del anuncio.
            url_archivo (str): URL del archivo del anuncio.
            url_click (str): URL para redirigir al hacer clic en el anuncio.
            sub_tipo (str): Subtipo del anuncio.
        """
        self._ancho = max(1, ancho)
        self._alto = max(1, alto)
        self._url_archivo = url_archivo
        self._url_click = url_click
        self._sub_tipo = sub_tipo

    @property
    def ancho(self):
        return self._ancho

    @ancho.setter
    def ancho(self, valor: int):
        self._ancho = max(1, valor)

    @property
    def alto(self):
        return self._alto

    @alto.setter
    def alto(self, valor: int):
        self._alto = max(1, valor)

    @property
    def url_archivo(self):
        return self._url_archivo

    @url_archivo.setter
    def url_archivo(self, valor: str):
        self._url_archivo = valor

    @property
    def url_click(self):
        return self._url_click

    @url_click.setter
    def url_click(self, valor: str):
        self._url_click = valor

    @property
    def sub_tipo(self):
        return self._sub_tipo

    @sub_tipo.setter
    def sub_tipo(self, valor: str):
        if valor in self.SUB_TIPOS:
            self._sub_tipo = valor
        else:
            raise SubTipoInvalidoError("El subtipo de formato introducido no es válido")

    @classmethod
    @abstractmethod
    def mostrar_formatos(cls):
        """
        Método abstracto para mostrar los formatos disponibles.
        """
        pass

    @abstractmethod
    def comprimir_anuncio(self):
        """
        Método abstracto para comprimir el anuncio.
        """
        pass

    @abstractmethod
    def redimensionar_anuncio(self):
        """
        Método abstracto para redimensionar el anuncio.
        """
        pass
