
class Jugador :
    def __init__(self, nombre, pais, dorsal, posicion ):
        self.nombre = nombre 
        self.pais = pais 
        self.dorsal = dorsal 
        self.posicion = posicion 
jugador1 = Jugador ("messi", "argentina",10,"centro"  )
jugador2 = Jugador (" Neymar", "Brasil", 11, "Delantero")
print (type (jugador1))
print (type (jugador2))
print (jugador1.__dict__)
print (jugador2.__dict__)