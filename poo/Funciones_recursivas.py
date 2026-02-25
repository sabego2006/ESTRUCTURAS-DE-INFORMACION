def sumatoria(num):
    if num==1:
        return 1
    else:
        return num + sumatoria(num-1)
    
num=int(input("Ingrese un numero: "))
print(sumatoria(num))

def factorial(num):
    if num==1:
        return 1
    else:
        return num * factorial(num-1)
    
print(factorial(num))