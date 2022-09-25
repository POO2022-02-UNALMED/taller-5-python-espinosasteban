from zooAnimales.animal import Animal

class Ave(Animal):
    _totalAnimales = 0
    _listado = []
    halcones = 0
    aguilas = 0
    def __init__(self, nombre, edad, habitat, genero, colorPlumas):
        super().__init__(nombre, edad, habitat, genero)

        self._nombre = nombre
        self._edad = edad
        self._habitat = habitat
        self._genero = genero
        self._colorPlumas = colorPlumas

        Ave._totalAnimales += 1

    @classmethod
    def cantidadAves(cls):
        return cls._totalAnimales

    def movimiento(self):
        return "volar"

    @classmethod
    def crearHalcon(cls, nombre, edad, genero):
        cls.halcones += 1
        return Ave(nombre,edad,genero,"montanas","cafe glorioso")

    @classmethod
    def crearAguila(cls, nombre, edad, genero):
        cls.aguilas += 1
        return Ave(nombre, edad, genero, "montanas", "blanco y amarillo")

    @classmethod
    def setListado(cls, listado):
        cls._listado = listado

    @classmethod
    def getListado(cls):
        return cls._listado

    def getColorPlumas(self):
        return self._colorPlumas

    def setColorPlumas(self, colorPlumas):
        self._colorPlumas = colorPlumas

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

    def toString(self):
        return f"Mi nombre es {self._nombre}, tengo una edad de {self._edad}, habito en {self._habitat} y mi genero es {self._genero}"