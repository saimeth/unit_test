from libro import Libro

class Biblioteca:
    def __init__(self, nombre):
        self.nombre = nombre
        self.libros = []  # lista vacía de libros

    def agregar_libro(self, libro):
        self.libros.append(libro)

    def mostrar_libros(self):
        return [str(libro) for libro in self.libros]
