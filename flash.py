#########################################################################################
def ejercicio_1():
    suma_del_cuadrado = []
    suma_normal = []
    for i in range(0,11):
        suma_del_cuadrado.append(i**2) #Lista con todos los cuadrados
        suma_normal.append(i) #Lista con el numero natural

    total = (sum(suma_normal)**2) - sum(suma_del_cuadrado) #Hace la diferencia
    return total #Envia la diferencia

############################################################################################
#Funcion que determina si un numero N es primo o no
def es_primo(N):
    contador = 0
    #Encuentra los divisores
    for i in range(1,N):
        if N % i == 0:
            contador = contador + 1
    if contador > 1:  #si el numero tiene mas de un divisor no es primo
        return False
    else:
        return True

def ejercicio_2(N):
    lista = []
    for i in range(2,N):
        if es_primo(i): #Si el numero es primo lo agrega a la sumatoria
            lista.append(i)
    return sum(lista) #Envia el resultado

###################################################################################
def ejercicio_3():
    lista = []
    i = len(lista)
    n = 2
    while i < 702:
        if es_primo(n): #Si el numero es primo lo agrega a la sumatoria
            lista.append(n)
            i = len(lista)
        n = n + 1
    return  lista[700]#Envia el resultado

###########################################################################################
def es_abundante(N):
    lista_divisores = []
    for i in range (1,N):
        if N % i == 0:
            lista_divisores.append(i)
    if(sum(lista_divisores) > N): #Si la suma de divisores > N
        return True
    else:
        return False


def ejercicio_4():
    lista_abundantes = []
    i = len(lista_abundantes)
    n = 2    
    while i < 778:
        if es_abundante(n):
            lista_abundantes.append(n) # Si es abundante lo agrega a la lista
            i = len(lista_abundantes)
        n = n + 1            
    return lista_abundantes[776] #El 777 es el indice 776

###########################################################################################
def es_perfecto(N):
    lista_divisores = []
    for i in range (1,N):
        if N % i == 0:
            lista_divisores.append(i)
    if(sum(lista_divisores) == N): #Perfecto si sumatoria de divisores = N
        return True
    else:
        return False

def ejercicio_5():
    lista_perfectos = []
    for i in range (1,7944):
        if es_perfecto(i): #si es perfecto lo agrega a la lista
            lista_perfectos.append(i)   
    return sum(lista_perfectos) #Envia la sumatoria


print('La diferencia para los primeros 144 numeros naturales es ',ejercicio_1())
print('La sumatoria de los numeros primos debajo de 7106 son  ',ejercicio_2(7106))
print('El 701-ésimo numero primo es  ',ejercicio_3())
print('El 777-ésimo numero abundante es  ',ejercicio_4())
print('La sumatoria de todos los números perfectos debajo de 7944 es ',ejercicio_5())