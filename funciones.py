#Funcion que retorna el listado de divisores propios de un numero n
def divisores_propios_de_n(n : int):
    lista = []
    for elemento in range (1,n):
        if n % elemento == 0:
            lista.append(elemento)
    return lista

#Funcion que retorna True en caso de que un numero n sea primo, False en caso contrario
def es_primo(n : int):
    return len(divisores_propios_de_n(n)) == 1

#Funcion que retorna un listado con los primeros N numeros perfectos
def primeros_N_numeros_perfectos(N:int):
    lista_de_perfectos = []
    contador = 1
    while len(lista_de_perfectos) < N:
        lista_divisores = divisores_propios_de_n(contador)
        if sum(lista_divisores) == contador:
            lista_de_perfectos.append(contador)
        contador = contador + 1
    return lista_de_perfectos

#Funcion que retorna un listado con las primeras N parejas de numeros amigos
def primeros_N_numeros_amigos(N:int):
    lista_de_amigos = []
    contador = 2
    while len(lista_de_amigos) < N:
        p = 3 * (2**(contador-1)) - 1
        q = 3 * (2**(contador)) - 1
        r = 9 * (2**(2*contador-1)) - 1
        if es_primo(p) and es_primo(q) and es_primo(r):
            num1 = (2**contador) * p * q
            num2 = (2**contador) * r
            lista_de_amigos.append((num1,num2))
        contador = contador + 1
    return lista_de_amigos


#Menu de seleccion 
seleccion = 1
while  seleccion != 0:
    print()
    print()
    print('------ Escoja opcion-------')
    print('1. Primeros N números perfectos')
    print('2. Primeros N números amigos')
    print('0. Salir.')
    seleccion = int(input('Opcion: '))
    print(seleccion)
    if seleccion == 1:
        N = int(input('Valor de N: '))
        print("Los primeros "+ str(N) + " Numeros perfectos son",primeros_N_numeros_perfectos(N))
    elif seleccion == 2:
        N = int(input('Valor de N: '))
        print("Los primeros "+ str(N) + " Numeros amigos son",primeros_N_numeros_amigos(N))