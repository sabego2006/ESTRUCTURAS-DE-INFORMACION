class Nodo:
    def __init__(self,dato):
        self.dato=dato
        self.siguiente=None

class Lista:
    def __init__(self):
        self.primero=None
            
    def adicionar(self,dato):
        nuevo=Nodo(dato)
        if self.primero==None:
            self.primero=nuevo
        else:
           actual=self.primero
           while actual.siguiente:
               actual=actual.siguiente
           actual.siguiente=nuevo
    
    def mostrar(self):
        actual=self.primero
        while actual:
            print(actual.dato)
            actual=actual.siguiente      
            
#FUNCION CREADA CON GEMINI AI
    def eliminar(self, dato):
        actual = self.primero
        anterior = None
    
    # 1. Buscar el nodo y mantener rastro del anterior
        while actual is not None and actual.dato != dato:
            anterior = actual
            actual = actual.siguiente
        
    # 2. Si no se encontró el dato
        if actual is None:
            return 
        
    # 3. Si el dato es el primer nodo
        if anterior is None:
            self.primero = actual.siguiente
        else:
            # 4. "Saltar" el nodo actual
            anterior.siguiente = actual.siguiente
listado=Lista()
listado.adicionar(24)
listado.adicionar(11)
listado.adicionar(2)
listado.adicionar(9)
listado.mostrar()
print(" ")
listado.eliminar(24)
listado.mostrar()