class Vehiculo:
    def __init__(self, llantas, color, precio):
        self.llantas = llantas
        self.color = color
        self.precio = precio

    def mostrar_atributos(self):
        print("Llantas:", self.llantas, ", Color:", self.color, ", Precio:", self.precio, "pesos")

    def aplicar_descuento(self):
        if self.precio > 100000:
            descuento = self.precio * 0.1
            self.precio -= descuento
            print("Descuento aplicado. Nuevo precio:", self.precio, "pesos")
        else:
            print("No se aplica descuento")

class Moto(Vehiculo):
    def __init__(self, color, precio):
        super().__init__(llantas=2, color=color, precio=precio)

class Auto(Vehiculo):
    def __init__(self, color, precio):
        super().__init__(llantas=4, color=color, precio=precio)

moto1 = Moto("Verde", 150000)
auto1 = Auto("Negro", 99000)

moto1.mostrar_atributos()
moto1.aplicar_descuento()

auto1.mostrar_atributos()
auto1.aplicar_descuento()
