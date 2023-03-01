def sumar_Numeros(numeros):
    suma = 0
    for numero in numeros:
        suma += numero
    return suma

numeros = [1, 2, 3, 4, 5]

print("El resultado de la suma es: ")
print(sumar_Numeros(numeros))