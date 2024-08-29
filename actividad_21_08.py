class Fabrica: # Crea la clase
    def _init_(self, llantas, color, precio):
        self.llantas = llantas
        self.color = color
        self.precio = precio

    def mostrar_datos(self):# Muestra los datos
        if self.precio > 100000: # Si el precio es mayor de 100000 le da el descuento
            self.precio *= 0.9  # Aplica el descuento del 10%
        print("Transporte con", self.llantas, "llantas, color", self.color, "y precio", self.precio)


class Moto(Fabrica): # Crea la clase hija Moto
    def _init_(self, color, precio):
        super()._init_(2, color, precio)


class Auto(Fabrica): #crea la clase hija Auto
    def _init_(self, color, precio):
        super()._init_(4, color, precio)


mi_moto = Moto("Rojo", 15000)
mi_auto = Auto("Azul", 160000)

mi_moto.mostrar_datos() # Muestra los datos de moto
mi_auto.mostrar_datos() # Muestra los datos de auto