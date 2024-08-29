#crear una clase fabrica que tengsa los atributos llantas, color y precio; lurgo qreardos mas que hereden las cuales son moto y autoque muestren la cantidad, color y precio de ambos transportes y por ultimo deberan mostrar.
class Fabrica:
    def __init__(self, llantas, color, precio):
        self.llantas = llantas
        self.color = color
        self.precio = precio

    def mostrar_datos(self):
        print("Transporte con", self.llantas, "llantas, color", self.color, "y precio ", self.precio)


class Moto(Fabrica):
    def __init__(self, color, precio):
        super().__init__(2, color, precio)


class Auto(Fabrica):
    def __init__(self, color, precio):
        super().__init__(4, color, precio)


moto = Moto("Rojo", 1500)
auto = Auto("Azul", 10000)

moto.mostrar_datos()
auto.mostrar_datos()
