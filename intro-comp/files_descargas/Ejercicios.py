#!/usr/bin/python3

#Ejercicio1: dar un algoritmo que, dada una lista de enteros A y un entero x, devuelva el índice del elemento de la lista más cercano a x. Resolverlo para los casos en que A está ordenada y en que no lo está.

#Ejercicio2: dar un algoritmo que, dada una lista ordenada A y dos enteros x e y, devuelva la cantidad de elementos de A que están entre x e y ( cantidad de i tal que x<=A[i]<=y )

#Ejercicio1:
def masCercano (A,x):
    i = 1
    dif = abs(A[0]-x)
    aux = 0
    while i<len(A):
        if dif>abs(A[i]-x):
            dif = abs(A[i]-x)
            aux = i
        i += 1
    return aux

def masCercanoOrd (A,x):
    #Dada una lista ordenada A y un entero x, devuelve el lugar del elemento de A más cercano a x.
    
    izq = 0
    der = len(A)-1
    med = 0
    while (der-izq) > 1:
        med = (izq+der)//2
        if A[med]>x:
            der = med
        else:
            izq = med
    if abs(A[izq]-x)>=abs(A[der]-x):
        return der
    else:
        return izq

#Ejercicio2: voy a definir dos funciones auxiliares:

def minimoMayor (A,x):
    #Dada una lista ordenada A, devuelve el mínimo lugar en el que A es por lo menos x. Si son todos menores, devuelve |A|.

    if A[len(A)-1] < x:
        return len(A)
    #Me deshago del caso en que toda la lista es menor a x.
    
    izq = 0
    der = len(A)-1
    med =  (izq+der)//2
    while (der-izq)>1:
        med = (izq+der)//2
        if A[med]>=x:
            der = med
        else:
            izq = med
    if A[izq] >= x:
        return izq
    else:
        return der         
    
def maximoMenor (A,y):
    #Dada una lista ordenada A, devuelve el máximo lugar en el que A es a lo sumo y. Si son todos mayores, devuelve -1.

    if (A[0] > y):
        return -1
    #Me deshago del caso en que toda la lista es mayor a y.
    
    return minimoMayor(A,y+1)-1

def cuantosHayEntre (A,x,y):
    izq = minimoMayor(A,x)
    der = maximoMenor(A,y)
    return max(der-izq+1,0)

################TESTS#################

def testMasCercanoOrd():
    L = range(0,11)
    print("El elemento más cercano a 5 en [0..10] es: ", masCercanoOrd(L,5))
    L = [0,0,0,1,1,1]
    print("El elemento más cercano a 0 en [0,0,0,1,1,1] es: ", masCercanoOrd(L,0),'.\n',
          "El elemento más cercano a -1 es: ", masCercanoOrd(L,-1), '.\n',
          "El elemento más cercano a 1 es: ", masCercanoOrd(L,1), '.\n',
          "El elemento más cercano a 2 es: ", masCercanoOrd(L,2)
          )
    
def testMaximoMenor():
    L = range(0,11)
    print("El máximo elemento menor a 5 en [0..10] es: ", maximoMenor(L,5))
    L = [0,0,0,1,1,1]
    print("El máximo elemento menor a 0 en [0,0,0,1,1,1] es: ", maximoMenor(L,0),'.\n',
          "El máximo elemento menor a -1 es: ", maximoMenor(L,-1), '.\n',
          "El máximo elemento menor a 1 es: ", maximoMenor(L,1), '.\n',
          "El máximo elemento menor a 2 es: ", maximoMenor(L,2)
          )
    
def testMinimoMayor():
    L = range(0,11)
    print("El mínimo elemento mayor a 5 en [0..10] es: ", minimoMayor(L,5))
    L = [0,0,0,1,1,1]
    print("El mínimo elemento mayor a 0 en [0,0,0,1,1,1] es: ", minimoMayor(L,0),'.\n',
          "El mínimo elemento mayor a -1 es: ", minimoMayor(L,-1), '.\n',
          "El mínimo elemento mayor a 1 es: ", minimoMayor(L,1), '.\n',
          "El mínimo elemento mayor a 2 es: ", minimoMayor(L,2)
          )

def testCuantosHayEntre():
    L=range(0,11)
    print("La cantidad de elementos que hay entre 0 y 10 en [0..10] es: ", cuantosHayEntre(L,0,10))
    L = [0,0,1,1,2,3,3,4]
    print("La cantidad de elementos en [0,0,1,1,2,3,3,4] entre 0 y 1 es: ", cuantosHayEntre(L,0,1), '.\n',
          "La cantidad que hay entre -1 y 0 es: ", cuantosHayEntre(L,-1,0), '.\n',
          "La cantidad que hay entre 1 y 3 es: ", cuantosHayEntre(L,1,3), '.\n',
          "La cantidad que hay entre 3 y 5 es: ", cuantosHayEntre(L,3,5), '.\n',
          "La cantidad que hay entre 7 y 9 es: ", cuantosHayEntre(L,7,9), '.\n',
          "La cantidad que hay entre -1 y 9 es: ", cuantosHayEntre(L,-1,9), '.\n',
          "La cantidad que hay entre -6 y -2 es: ", cuantosHayEntre(L,-6,-2), '.\n',
          "La cantidad que hay entre 3 y 1 es: ", cuantosHayEntre(L,3,1), '.\n'
          )

def test():
    testMasCercanoOrd()
    testMinimoMayor()
    testMaximoMenor()
    testCuantosHayEntre()


#################FIN-TESTS#################
    
test()
