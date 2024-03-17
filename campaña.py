from anuncio import Video, Display, Social
from error import LargoExcedidoError

class Campaña:

    def __init__(self, nombre: str, fecha_inicio: str, fecha_termino: str) -> None:
        """
        Inicializa una nueva campaña con su nombre, fecha de inicio y fecha de término.

        Args:
            nombre (str): Nombre de la campaña.
            fecha_inicio (str): Fecha de inicio de la campaña.
            fecha_termino (str): Fecha de término de la campaña.
        """
        self.__nombre = nombre
        self.__fecha_inicio = fecha_inicio
        self.__fecha_termino = fecha_termino
        self.__anuncios = []
        self.formatos_anuncios = ["Video", "Display", "Social"]

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, valor: str):
        """
        Setter para el nombre de la campaña. Verifica que el nombre no exceda los 250 caracteres.

        Args:
            valor (str): Nuevo nombre para la campaña.

        Raises:
            LargoExcedidoError: Si el nombre excede los 250 caracteres.
        """
        if len(valor) <= 250:
            self.__nombre = valor
        else:
            raise LargoExcedidoError("El nombre excede los 250 caracteres")

    @property
    def fecha_inicio(self):
        return self.__fecha_inicio

    @fecha_inicio.setter
    def fecha_inicio(self, valor: str):
        self.__fecha_inicio = valor

    @property
    def fecha_termino(self):
        return self.__fecha_termino

    @fecha_termino.setter
    def fecha_termino(self, valor: str):
        self.__fecha_termino = valor

    @property
    def anuncios(self):
        return self.__anuncios
    
    def crear_anuncio(self):
        """
        Crea un nuevo anuncio según el tipo ingresado por el usuario y lo agrega a la lista de anuncios de la campaña.
        """
        tipo_anuncio = input("Ingrese el tipo de anuncio que desea crear ('Video', 'Display' o 'Social'):\n")
        while tipo_anuncio not in self.formatos_anuncios:
            tipo_anuncio = input("Ingrese una opción válida ('Video', 'Display' o 'Social'):\n")

        if tipo_anuncio == "Video":
            Video.mostrar_formatos()
            url_archivo = input("Ingrese la URL del archivo:\n")
            url_clic = input("Ingrese la URL del clic:\n")
            sub_tipo = input("Ingrese el subtipo del anuncio:\n")
            duracion = int(input("Ingrese la duración del video:\n"))

            nuevo_anuncio = Video(url_archivo, url_clic, sub_tipo, duracion)
  
        elif tipo_anuncio == "Display":
            Display.mostrar_formatos()
            ancho = int(input("Ingrese el ancho del anuncio:\n"))
            alto = int(input("Ingrese el alto del archivo:\n"))
            url_archivo = input("Ingrese la URL del archivo:\n")
            url_clic = input("Ingrese la URL del clic:\n")
            sub_tipo = input("Ingrese el subtipo del anuncio:\n")

            nuevo_anuncio = Display(ancho, alto, url_archivo, url_clic, sub_tipo)

        else:
            Social.mostrar_formatos()
            ancho = int(input("Ingrese el ancho del anuncio:\n"))
            alto = int(input("Ingrese el alto del archivo:\n"))
            url_archivo = input("Ingrese la URL del archivo:\n")
            url_clic = input("Ingrese la URL del clic:\n")
            sub_tipo = input("Ingrese el subtipo del anuncio:\n")

            nuevo_anuncio = Social(ancho, alto, url_archivo, url_clic, sub_tipo)

        self.anuncios.append(nuevo_anuncio)
        return nuevo_anuncio

    def __str__(self) -> str:
        """
        Representación en cadena de la campaña, mostrando la cantidad de anuncios por tipo.

        Returns:
            str: Cadena que representa la campaña.
        """
        num_videos = sum(1 for anuncio in self.anuncios if isinstance(anuncio, Video))
        num_display = sum(1 for anuncio in self.anuncios if isinstance(anuncio, Display))
        num_social = sum(1 for anuncio in self.anuncios if isinstance(anuncio, Social))

        return f"""
        Nombre de la campaña: {self.nombre}
        Anuncios: {num_videos} Video, {num_display} Display, {num_social} Social
        """

if __name__ == "__main__":
    print("CREACIÓN DE CAMPAÑA")
    campaña = Campaña("Nombre de la Campaña", "2024-01-01", "2024-12-31")
    campaña.crear_anuncio()

    print(f"Número de anuncios: {len(campaña.anuncios)}")
    print(campaña)

    campaña.crear_anuncio()

    print(f"Número de anuncios: {len(campaña.anuncios)}")
    print(campaña)

    campaña.crear_anuncio()

    print(f"Número de anuncios: {len(campaña.anuncios)}")
    print(campaña)
