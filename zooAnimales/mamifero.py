from zooAnimales.animal import Animal

class Mamifero(Animal):
    _totalAnimales = 0
    _listado = []
    caballos = 0
    leones = 0
    def __init__(self, nombre, edad, habitat, genero, pelaje,patas):
        super().__init__(nombre, edad, habitat, genero)

        self._nombre = nombre
        self._edad = edad
        self._habitat = habitat
        self._genero = genero
        self._pelaje = pelaje
        self._patas = patas

        Mamifero._totalAnimales += 1

    @classmethod
    def cantidadMamiferos(cls):
        return cls._totalAnimales


    @classmethod
    def crearCaballo(cls, nombre, edad, genero):
        cls.caballos += 1
        return Mamifero(nombre,edad,genero,"padrera",True,4)

    @classmethod
    def crearLeon(cls, nombre, edad, genero):
        cls.leones += 1
        return Mamifero(nombre, edad, genero, "selva", True, 4)

    @classmethod
    def setListado(cls, listado):
        cls._listado = listado

    @classmethod
    def getListado(cls):
        return cls._listado

    def isPelaje(self):
        return self._pelaje

    def setPelaje(self, pelaje):
        self._pelaje = pelaje

    def getPatas(self):
        return self._patas

    def setPatas(self, patas):
        self._patas = patas

    def getNombre(self):
        return self._nombre

    def setNombre(self, nombre):
        self._nombre = nombre

    def getEdad(self):
        return self._edad

    def setEdad(self, edad):
        self._edad = edad

    def getHabitat(self):
        return self._habitat

    def setHabitat(self, habitat):
        self._habitat = habitat

    def getGenero(self):
        return self._genero

    def setGenero(self, genero):
        self._genero = genero

    def __str__(self):
        return f"Mi nombre es {self._nombre}, tengo una edad de {self._edad}, habito en {self._habitat} y mi genero es {self._genero}"