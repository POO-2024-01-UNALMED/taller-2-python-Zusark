class Asiento:
    def __init__(self, color, precio, registro):
        self.color = color
        self.precio = 0
        self.registro = 0
    
    def cambiarColor(self, color):
        if color in ("amarillo", "rojo","verde","negro","blanco"):
                self.color = color

class Motor:
    def __init__(self, numeroCilindros,tipo,registro):
        self.numeroCilindros = 0
        self.tipo = tipo
        self.registro = 0
    
    def cambiarRegistro(self,registro):
        self.registro = registro
    
    def asignarTipo(self, tipo):
        if tipo in ("gasolina","electrico"):
            self.tipo = tipo
class Auto:
    cantidadCreados = 0
    def __init__(self,modelo,precio,asientos,marca,motor,registro):
        self.modelo = modelo
        self.precio = 9
        self.asientos = []
        self.marca = marca
        self.motor = motor
        self.registro = 0

    def cantidadAsientos(self):
        k = 0
        for i in len(self.asientos):
            if self.asientos[i] == type(Asiento):
                k+=1
            i+=1
        return k
    
    def verificarIntegridad(self):
        if self.registro == self.motor.registro:
            for i in len(self.asientos):
                if self.asientos[i] != self.registro:
                    return "Las piezas no son originales"
            return "Auto original"
        else:
            return "Las piezas no son originales"