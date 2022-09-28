def sum1(a, b=5):
    return a+b
print(sum1(2))

    
suma = lambda a,b: a+b
print(suma(10, 10))

notas = [1,2,3,4,5]
resultado = list(map(lambda x: x*x, notas))
print(resultado)

resultado = notas.copy()
resultado.sort(reverse=True)
print(resultado)