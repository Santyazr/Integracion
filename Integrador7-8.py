
class Persona:
    def __init__(self, nombre, edad, telefono):
        self.nombre = nombre
        self.edad = edad
        self.telefono = telefono

class Cuenta:
    def __init__(self, titular, cantidad=0):
        self.titular = titular
        self.cantidad = cantidad

    def ingresar(self, cantidad):
        if cantidad > 0:
            self.cantidad += cantidad

    def retirar(self, cantidad):
        self.cantidad -= cantidad

    def mostrar(self):
        print(f"Titular: {self.titular.nombre}\nCantidad: {self.cantidad}")

    def get_titular(self):
        return self.titular

    def set_titular(self, titular):
        self.titular = titular

    def get_cantidad(self):
        return self.cantidad

    def set_cantidad(self, cantidad):
        self.cantidad = cantidad


class CuentaJoven(Cuenta):  
    def __init__(self, titular, bonificacion=0, cantidad=0):
        super().__init__(titular, cantidad)
        self.bonificacion = bonificacion

    def es_titular_valido(self):
        return self.titular.edad >= 18 and self.titular.edad < 25

    def retirar(self, cantidad):
        if self.es_titular_valido():
            super().retirar(cantidad)

    def mostrar(self):
        print(f"Cuenta Joven_titular: {self.titular.nombre}\nCantidad: {self.cantidad}\nBonificación: {self.bonificacion}")

    def get_bonificacion(self):
        return self.bonificacion

    def set_bonificacion(self, bonificacion):
        self.bonificacion = bonificacion

