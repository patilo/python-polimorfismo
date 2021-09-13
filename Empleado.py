class Empleado:

    def __init__(self, nombre, sueldo):
        self.nombre = nombre
        self.sueldo = sueldo

    def __str__(self):
        return f'Empleado: nombre: {self.nombre}, sueldo: {self.sueldo}'

    def mostrar_detalles(self):
        return self.__str__()  #esto lo heredan las clases hijas