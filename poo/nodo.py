class Nodo:
    def __init_(self, dato):
        self.dato=dato
        self.siguiente=None

a= Nodo(100)
b= Nodo(1000)
c= Nodo(1)
d= Nodo(10)

a.siguiente=b
b.siguiente=c
a.siguiente=d
a.siguiente=None

 