class Pais :
    def __init__(self, capital,cantidad_de_poblacion, idioma , moneda  ):
        self.capital= capital
        self.cantidad_de_poblacion=cantidad_de_poblacion
        self.idioma = idioma 
        self.moneda = moneda 
Colombia = Pais ( "Bogota", "51.607.000", "castellano", "peso" )
Brasil = Pais ( "Brasilia ", "203.063.000", "portugues", "real ")
print (type(Colombia))
print (type(Brasil))
print ( Colombia.__dict__)
print (Brasil.__dict__)