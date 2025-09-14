# swdesign-tarea2

[Enlace al repo](https://github.com/JM-193/swdesign-tarea2)

## Información Personal

* José Manuel Mora Z - C35280
* Diseño de Software - CI-0136
* Escuela de las Ciencias de la Computación e Informática (ECCI)
* Universidad de Costa Rica (UCR)

## Problemas identificados y soluciones

### `If` innecesario (clase `Libro`)

El siguiente código contiene un `if` innecesario, pues el valor de retorno es el mismo que el resultado de la expresión booleana.

```python
def es_antiguo(self):
    if self.anio_publicacion < 1980:
        return True
    else:
        return False
```

Como resultado, la función puede reducirse a esto:

```python
def es_antiguo(self):
    return self.anio_publicacion < ANCIENT_YEAR
```

### Constantes mágicas (clase `Libro`)

El código original contenía unas cuantas constantes mágicas, para esto definimos constantes nombradas.

```python
ANCIENT_YEAR = 1980
BASE_POPULARITY = 10
```

Los otros números relacionados a la popularidad se resuelven con la siguiente corrección.

### Open/Closed Principle (clase `Libro`)

El `if` contenido en la función `calcular_popularidad()` representa un problema, pues para agregar más géneros es necesario modificar el método.

```python
def calcular_popularidad(self):
    if self.genero == 'novela':
        base = 50
        extra = self.paginas / 10
    elif self.genero == 'ciencia':
        base = 70
        extra = self.paginas / 5
    elif self.genero == 'historia':
        base = 40
        extra = self.paginas / 8
    else:
        base = 10
        extra = 0
    return base + extra
```

Para esto se extrajeron las opciones a este diccionario

```python
GENRE_STATS = {
    'novela': (50, 10),
    'ciencia': (70, 5),
    'historia': (40, 8),
}

...

def calcular_popularidad(self):
    base, divisor = GENRE_STATS.get(self.genero, (BASE_POPULARITY, None))
    extra = self.paginas / divisor if divisor else 0
    return base + extra
```

### Single Responsibility Principle (clase `Libro`)

La clase no debería responsabilizarse por imprimir, por lo que la secuencia de prints se convierte en un solo `string` que se retorna.

```python
def __str__(self) -> str:
    return {
        f"Título: {self.titulo}\n"
        f"Autor: {self.autor}\n"
        f"Género: {self.genero}\n"
        f"Páginas: {self.paginas}\n"
        f"Año: {self.anio_publicacion}\n"
        f"Disponible: {'Sí' if self.disponible else 'No'}\n"
        f"Popularidad: {self.calcular_popularidad()}\n"
        f"Es antiguo: {'Sí' if self.es_antiguo() else 'No'}\n"
        "------------------------"
    }
```

### Single Responsibility Principle (clase `Biblioteca`)

La clase no debería hacer I/O, por lo que se modificaron sus métodos de acuerdo a esto.

Empezando por `agregar_libro()`, que ahora recibe los parámetros para armar el libro en lugar de pedírselos al usuario y la implementación de un segundo método `agregar()` que recibe el `Libro` ya armado.

```py
def agregar(self, libro: Libro) -> Libro:
    self.libros.append(libro)
    return libro

def agregar_libro(self, titulo, autor, genero, paginas, anio, disponible=True) -> Libro:
    return self.agregar(Libro(titulo, autor, genero, paginas, anio, disponible))
```

Luego, el método `generar_reporte()` ahora devuelve un string en lugar de imprimir, y hace uso del método `__str__` de `Libro`

```py
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
```

### Nombres significativos de variables

A lo largo de las correcciones se reemplazaron nombres de variables que no fueran lo suficientemente claros.

Principalmente se cambiaron las variables `l` por `libro`.
