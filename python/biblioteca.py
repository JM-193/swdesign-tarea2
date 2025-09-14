from libro import Libro

class Biblioteca:
    def __init__(self):
        self.libros = []

    # SRP, la clase o debería hacer I/O directamente, recibe los parámetros
    # Nombre más descriptivo para la variable
    def agregar(self, libro: Libro) -> Libro:
        self.libros.append(libro)
        return libro

    # Se agrega un método para recibir el libro completo y otro para recibir los parámetros
    def agregar_libro(self, titulo, autor, genero, paginas, anio, disponible=True) -> Libro:
        return self.agregar(Libro(titulo, autor, genero, paginas, anio, disponible))

    # SRP, la clase no debería hacer I/O directamente, devuelve un string
    def generar_reporte(self) -> str:
        total = len(self.libros)
        antiguos = 0
        disponibles = 0
        popularidad_total = 0.0
        detalles = []

        for libro in self.libros:
            if libro.es_antiguo():
                antiguos += 1
            if libro.disponible:
                disponibles += 1
            popularidad_total += libro.calcular_popularidad()
            # Reemplazo el print por el __str__ de Libro
            detalles.append(str(libro))

        promedio = popularidad_total / total if total > 0 else 0

        resumen = (
            "\nREPORTE BIBLIOTECA:\n"
            f"Total libros: {total}\n"
            f"Disponibles: {disponibles}\n"
            f"Antiguos: {antiguos}\n"
            f"Promedio de popularidad: {promedio}\n"
        )

        return ("\n".join(detalles) + ("\n" if detalles else "") + resumen)