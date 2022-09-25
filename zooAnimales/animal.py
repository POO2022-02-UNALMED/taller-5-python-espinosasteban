




class Animal:
    _totalAnimales = 0
    _zona = []
    def __init__(self, nombre = "", edad = 0, habitat = "", genero = ""):
        self._nombre = nombre
        self._edad = edad
        self._habitat = habitat
        self._genero = genero
        Animal._totalAnimales += 1

    def movimiento(self):
        return "desplazarse"

    @classmethod
    def totalPorTipo(cls):
        from zooAnimales.anfibio import Anfibio
        from zooAnimales.ave import Ave
        from zooAnimales.mamifero import Mamifero
        from zooAnimales.pez import Pez
        from zooAnimales.reptil import Reptil
        mamiferos = Mamifero.cantidadMamiferos()
        aves = Ave.cantidadAves()
        reptiles = Reptil.cantidadReptiles()
        peces = Pez.cantidadPeces()
        anfibios = Anfibio.cantidadAnfibios()
        mensaje = f"Mamiferos : {mamiferos}\n" \
                  f"Aves : {aves}\n" \
                  f"Reptiles : {reptiles}" \
                  f"Peces : {peces}" \
                  f"Anfibios : {anfibios}"

        return mensaje

    def __str__(self):
        return f"Mi nombre es {self._nombre}, tengo una edad de {self._edad}, habito en {self._habitat} y mi genero es {self._genero}"

    @classmethod
    def getTotalAnimales(cls):
        return cls._totalAnimales

    @classmethod
    def setTotalAnimales(cls, animales):
        cls.totalAnimales = animales

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

    @classmethod
    def getZona(cls):
        return cls._zona

    @classmethod
    def setZona(cls, zona):
        cls._zona = zona