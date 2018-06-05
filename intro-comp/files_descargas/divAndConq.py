# def potencia(a, n):
#     res = 1
#     for i in range(n):
#         res *= a
#     return res
#
# print(potencia(2,4))
#
# # potencia con divide and conquer a^10 = a^5 * a^5
# # a^2 * a^3
# # a^1 * a^1
#
# def potenciaDC(a, n):
#     if n==0 or n==1:
#         return a
#     x = potencia(a, n//2)
#     if n%2 == 0:
#         return x * x
#     else:
#         return x * x * a
#
# print(potencia(2,7))
#
# def maximo(a):
#     med = len(a)//2
#     x = a[med]
#     if a[med-1] > x:
#         return maximo(a[:med+1])
#     elif a[med+1] > x:
#         return maximo(a[med:])
#     else:
#         return x
#
# print(maximo([-1,3,8,22,30,20,9,4,2,1]))
# print(maximo([1,3,2]))

def sumaMax(a):
    if len(a)==1:
        x = a[0]
        return max(0, x)

    med = len(a)//2
    sumaIzq = sumaMax(a[:med])
    sumaDer = sumaMax(a[med:])
    sumaMed = calcularSumaMedio(a)
    return max(sumaIzq, sumaDer, sumaMed)

def calcularSumaMedio(a):
    med = len(a)//2
    res = a[med] + a[med-1]
    temp = res
    for x in a[med+1:]:
        temp += x
        if temp > res:
            res = temp
    temp = res
    if med == 1:
        return res
    for x in a[med-2::-1]:
        temp += x
        if temp > res:
            res = temp
    return res

print(sumaMax([3,-1,4,8,-2,2,-7,5]))