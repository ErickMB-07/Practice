def sumar_digitos(n):
    if n <= 10:
        return n
    return n%10 + sumar_digitos(n//10)

def potencia(a, b):
    if b == 0:
        return 1
    return a*potencia(a, b-1)

def dividir_restas(n, m):
    if n >= m:
        return 1 + dividir_restas(n-m, m)
    return 0
print(dividir_restas(150,50))

def reves(n):
    if n<10:
        print(n, end ="")
    else:
        print(n%10, end="")
        reves(n//10)
reves(1234)