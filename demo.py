from campaña import Campaña
from error import LargoExcedidoError, SubTipoInvalidoError
from datetime import datetime

# Crear una nueva campaña
nueva_campaña = Campaña("Nueva Campaña", "20/03/2024", "30/03/2024")
nuevo_anuncio = nueva_campaña.crear_anuncio()

# Inicializar variable para el registro de errores
registro_errores = None

try:
    # Modificar la campaña
    nuevo_nombre = input("Ingrese el nuevo nombre de la campaña:\n")
    nuevo_subtipo = input("Ingrese el nuevo subtipo para el anuncio:\n")
    nueva_campaña.nombre = nuevo_nombre
    # Intentar modificar el subtipo del anuncio
    nueva_campaña.listado_anuncios[nueva_campaña.listado_anuncios.index(nuevo_anuncio)].sub_tipo = nuevo_subtipo

except LargoExcedidoError as e:
    print(e)
    # Registrar el error en el archivo de registro
    fecha_actual = datetime.now()
    with open(f'{str(fecha_actual).split(" ")[0]}.log', 'a') as registro_errores:
        registro_errores.write(f'{fecha_actual} - [ERROR]: {e}\n')

except SubTipoInvalidoError as e:
    print(e)
    # Registrar el error en el archivo de registro
    fecha_actual = datetime.now()
    with open(f'{str(fecha_actual).split(" ")[0]}.log', 'a') as registro_errores:
        registro_errores.write(f'{fecha_actual} - [ERROR]: {e}\n')

except Exception as e:
    print(e)
    # Registrar el error en el archivo de registro
    fecha_actual = datetime.now()
    with open(f'{str(fecha_actual).split(" ")[0]}.log', 'a') as registro_errores:
        registro_errores.write(f'{fecha_actual} - [ERROR]: {e}\n')

finally:
    # Cerrar el archivo de registro si está abierto
    if registro_errores is not None:
        registro_errores.close()

# Imprimir el subtipo del anuncio
print(nuevo_anuncio.sub_tipo)
