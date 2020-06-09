def divisores_propios_de_n(n : int):
    lista = []
    for elemento in range (1,n):
        if n % elemento == 0:
            lista.append(elemento)
    return lista


def primeros_N_numeros_perfectos(N:int):
    lista_de_perfectos = []
    contador = 1
    while len(lista_de_perfectos) < N:
        lista_divisores = divisores_propios_de_n(contador)
        if sum(lista_divisores) == contador:
            lista_de_perfectos.append(contador)
        contador = contador + 1
    return lista_de_perfectos


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