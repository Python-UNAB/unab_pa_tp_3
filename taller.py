# Ejercicio 2

class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __str__(self):
        return f"({self.x}, {self.y})"
    
    def ejex(self):
        return self.x
    
    def ejey(self):
        return self.y

    def impresion(self):
        return f"({self.x}, {self.y})"
    
    def opuesto(self):
        return Punto(-self.x, -self.y)



# Ejercicio 3

class Linea:
    def __init__(self, punto_a, punto_b):
        self._punto_a = punto_a
        self._punto_b = punto_b
    
    def mueve_derecha(self, distancia):
        self._punto_a.x += distancia
        self._punto_b.x += distancia
    
    def mueve_izquierda(self, distancia):
        self._punto_a.x -= distancia
        self._punto_b.x -= distancia

    def mueve_arriba(self, distancia):
        self._punto_a.y += distancia
        self._punto_b.y += distancia
    
    def mueve_abajo(self, distancia):
        self._punto_a.y -= distancia
        self._punto_b.y -= distancia


linea1 = Linea(Punto(0, 0), Punto(1, 1))

print(linea1._punto_a)
print(linea1.mueve_arriba(2))
print(linea1.mueve_derecha(3))  

# Ejercicio 4

class Cancion:
    def __init__(self, titulo:str, autor:str):
        self.titulo = titulo
        self.autor = autor

    def get_titulo(self):
        return self.titulo 
    
    def get_autor(self):
        return self.autor
    
    def set_titulo(self, titulo):
        self.titulo = titulo

    def set_autor(self, autor):
        self.autor = autor


Cancion1 = Cancion("Bohemian Rhapsody", "Queen") 


#Ejercicio 5

class Libro:
    def __init__(self, titulo:str, autor:str, paginas:int, edicion:str, editorial:str, lugar:str, isbn:str, fecha_de_edicion:str):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas
        self.edicion = edicion
        self.editorial = editorial
        self.lugar = lugar
        self.isbn = isbn
        self.fecha_de_edicion = fecha_de_edicion

    def get_titulo(self):
        return self.titulo
    
    def get_autor(self):
        return self.autor
    
    def get_paginas(self):
        return self.paginas
    
    def get_edicion(self):
        return self.edicion
    
    def get_editorial(self):
        return self.editorial
    
    def get_lugar(self):
        return self.lugar
    
    def get_isbn(self):
        return self.isbn
    
    def get_fecha_de_edicion(self):
        return self.fecha_de_edicion
    
    def set_titulo(self, titulo):
        self.titulo = titulo

    def set_autor(self, autor):
        self.autor = autor

    def set_paginas(self, paginas):
        self.paginas = paginas

    def set_edicion(self, edicion):
        self.edicion = edicion

    def set_editorial(self, editorial):
        self.editorial = editorial

    def set_lugar(self, lugar):
        self.lugar = lugar

    def set_isbn(self, isbn):
        self.isbn = isbn

    def set_fecha_de_edicion(self, fecha_de_edicion):
        self.fecha_de_edicion = fecha_de_edicion

    def leer(self):
        return f" Titutlo: {self.titulo} \n Autor: {self.autor} \n ISBN: {self.isbn} \n {self.lugar} \n {self.fecha_de_edicion} \n {self.edicion} \n {self.paginas} paginas"