# Evitar constantes mágicas
ANCIENT_YEAR = 1980
BASE_POPULARITY = 10

GENRE_STATS = {
    'novela': (50, 10),
    'ciencia': (70, 5),
    'historia': (40, 8),
}

class Libro:
    def __init__(self, titulo, autor, genero, paginas, anio_publicacion, disponible=True):
        self.titulo = titulo
        self.autor = autor
        self.genero = genero # 'novela', 'ciencia', 'historia'
        self.paginas = paginas
        self.anio_publicacion = anio_publicacion
        self.disponible = disponible

    # Open/Closed Principle, para añadir nuevos géneros no hay que modificar el método
    def calcular_popularidad(self):
        base, divisor = GENRE_STATS.get(self.genero, (BASE_POPULARITY, None))
        extra = self.paginas / divisor if divisor else 0
        return base + extra

    # El if sobraba
    def es_antiguo(self):
        return self.anio_publicacion < ANCIENT_YEAR

    # SRP, la clase no debería encargarse de imprimirse a sí misma
    def __str__(self) -> str:
        return (
            f"Título: {self.titulo}\n"
            f"Autor: {self.autor}\n"
            f"Género: {self.genero}\n"
            f"Páginas: {self.paginas}\n"
            f"Año: {self.anio_publicacion}\n"
            f"Disponible: {'Sí' if self.disponible else 'No'}\n"
            f"Popularidad: {self.calcular_popularidad()}\n"
            f"Es antiguo: {'Sí' if self.es_antiguo() else 'No'}\n"
            "------------------------"
        )
