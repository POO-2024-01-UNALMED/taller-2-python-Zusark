class Asiento:
    def __init__(self, color, precio, registro):
        self.color = color
        self.precio = precio
        self.registro = registro
    
    def cambiarColor(self, color):
        if color in ("amarillo", "rojo","verde","negro","blanco"):
            self.color = color

class Motor:
    def __init__(self, numeroCilindros,tipo,registro):
        self.numeroCilindros = numeroCilindros
        self.tipo = tipo
        self.registro = registro
    
    def cambiarRegistro(self,registro):
        self.registro = registro
    
    def asignarTipo(self, tipo):
        if tipo in ("gasolina","electrico"):
            self.tipo = tipo
class Auto:
    cantidadCreados = 0
    def __init__(self,modelo,precio,asientos,marca,motor,registro):
        self.modelo = modelo
        self.precio = precio        
        self.asientos = asientos
        self.marca = marca
        self.motor = motor
        self.registro = registro

    def cantidadAsientos(self):
        k = 0
        for i in self.asientos:
            if i != None and isinstance(i, Asiento):
                k+=1
        return k
    
    def verificarIntegridad(self):
        if self.registro == self.motor.registro:
            for j in self.asientos:  
                if isinstance(j, Asiento) and j != None:
                    if j.registro != self.registro:
                        return "Las piezas no son originales"
                return "Auto original"
                
        else:
            return "Las piezas no son originales"