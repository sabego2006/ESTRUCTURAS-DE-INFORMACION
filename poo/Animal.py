
nombre="Jaimito"
def saludar(nombre):
    print("Hola " + nombre)
    
saludar(nombre)


class Animal:
    def__init__(self, nombre):
        self.nombre=nombre
    def setNombre(self,nombre):
        self.nombre=nombre
    def getNombre(self):
        return self.nombre
obj=animal("gato")
obj.setNombre(("Manchas"))
print(obj.getNombre())    