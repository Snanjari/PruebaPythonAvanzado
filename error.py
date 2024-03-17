class Error(Exception):
    """Clase base para excepciones en este módulo."""
    pass

class LargoExcedidoError(Error):
    """Excepción lanzada cuando el nombre de la campaña excede el límite de caracteres."""
    pass

class SubTipoInvalidoError(Error):
    """Excepción lanzada cuando se ingresa un subtipo inválido para un anuncio."""
    pass
