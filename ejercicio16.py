print("CARLOS ALBERTO GARCIA GUERRERO")
print("ejercicio 1: Contar Ocurrencias de Elementos")
print("")
def contar_ocurrencias(palabras):
    ocurrencias = {}
    for palabra in palabras:
        ocurrencias[palabra] = ocurrencias.get(palabra, 0) + 1
    return ocurrencias

palabras = ["python", "java", "python", "c++"]
print(contar_ocurrencias(palabras))
print("")
print("ejercicio 2: Combinar Diccionarios")
print("")
def combinar (diccionario1, diccionario2):
    combinacion = diccionario1.copy()
    for clave, valor in diccionario2.items():
        if clave in combinacion:
            combinacion[clave] += valor
        else:
            combinacion[clave] = valor
    return combinacion
diccionario1 = {'a': 1, 'b': 2}
diccionario2 = {'b': 3, 'c': 4}
resultado = combinar(diccionario1, diccionario2)
print(resultado)

print("")
print("ejercicio 3: Listas de Frecuencia")
print("")
def frecuencia_num(numeros):
    frecuencia = {}
    for numero in numeros:
        frecuencia[numero] = frecuencia.get(numero, 0) + 1
    return frecuencia

numeros = [1, 1, 2, 3, 3, 3]
print(frecuencia_num(numeros))

print("")
print("ejercicio 4: Contar Filtrar Palabras Largas")
print("")
def filtrar_palabras_largas(palabras, longitud):
    resultado = []
    for palabra in palabras:
        if len(palabra) > longitud:
            resultado.append(palabra)
    return resultado
palabras = ["hola", "mundo", "python", "programación"]
longitud = 5
print(filtrar_palabras_largas(palabras, longitud)) 

print("")
print("ejercicio 5: Inversión de Tuplas en Lista")
print("")
def invertir_tuplas(tuplas):
    resultado = []
    for a, b in tuplas:
        resultado.append((b, a))
    return resultado
tuplas = [(1, 2), (3, 4), (5, 6)]
print(invertir_tuplas(tuplas))
print("")
print("ejercicio 6: Encontrar el Valor Más Frecuente")
print("")
def valor_mas_frecuente(numeros):
    frecuencia = {}
    for numero in numeros:
        if numero in frecuencia:
            frecuencia[numero] += 1
        else:
            frecuencia[numero] = 1
    return max(frecuencia, key=frecuencia.get)
numeros = [1, 2, 3, 1, 2, 1]
print(valor_mas_frecuente(numeros))

print("")
print("ejercicio 7: Comprobar Subconjunto")
print("")
def subconjunto(conjunto1, conjunto2):
    return conjunto1.issubset(conjunto2)
conjunto1 = {1, 2, 3}
conjunto2 = {1, 2, 3, 4, 5}
print(subconjunto(conjunto1, conjunto2))

print("")
print("ejercicio 8: Agrupación por Clave")
print("")
def agrupar_edad(personas):
    agrupacion = {}
    for persona in personas:
        edad = persona['edad']
        nombre = persona['nombre']
        if edad not in agrupacion:
            agrupacion[edad] = []
        agrupacion[edad].append(nombre)
    return agrupacion
personas = [{"nombre": "Ana", "edad": 25}, {"nombre": "Luis", "edad": 25}, {"nombre": "Carlos", "edad": 30}]
print(agrupar_edad(personas))

print("")
print("ejercicio 9: Merge Sort utilizando Listas")
print("")
def merge_sort(lista):
    if len(lista) <= 1:
        return lista
    medio = len(lista) // 2
    izquierda = merge_sort(lista[:medio])
    derecha = merge_sort(lista[medio:])
    return merge(izquierda, derecha)

def merge(izquierda, derecha):
    resultado = []
    i = j = 0
    while i < len(izquierda) and j < len(derecha):
        if izquierda[i] < derecha[j]:
            resultado.append(izquierda[i])
            i += 1
        else:
            resultado.append(derecha[j])
            j += 1
    resultado.extend(izquierda[i:])
    resultado.extend(derecha[j:])
    return resultado

numeros = [5, 3, 8, 6, 2]
print(merge_sort(numeros))
print("")
print("ejercicio 10: Eliminar Elementos por Condición")
print("")
def eliminar_menores(numeros, limite):
    resultado = []
    for num in numeros:
        if num >= limite:
            resultado.append(num)
    return resultado
numeros = [1, 2, 3, 4, 5]
limite = 3
print(eliminar_menores(numeros, limite))
print("")
print("ejercicio 11: Flatten List of Lists")
print("")
def flatten_list(lista_de_listas):
    resultado = []
    for sublista in lista_de_listas:
        for item in sublista:
            resultado.append(item)
    return resultado
lista_de_listas = [[1, 2], [3, 4], [5]]
print(flatten_list(lista_de_listas))

print("")
print("ejercicio 12: Cálculo de Mediana")
print("")
def cal_mediana(numeros):
    numeros.sort()
    n = len(numeros)
    medio = n // 2
    if n % 2 == 0:
        return (numeros[medio - 1] + numeros[medio]) / 2
    else:
        return numeros[medio]
numeros = [1, 3, 2, 4, 5]
print(cal_mediana(numeros)) 

print("")
print("ejercicio 13: Duplicar Elementos en una Lista")
print("")
def duplicar_elementos(numeros):
    resultado = []
    for numero in numeros:
        for _ in range(2):
            resultado.append(numero)
    return resultado
numeros = [1, 2, 3]
print(duplicar_elementos(numeros))

print("")
print("ejercicio 14: Contar Palabras en Frases")
print("")
def contar_palabras(frases):
    conteo = {}
    for i, frase in enumerate(frases):
        palabras = frase.split()
        conteo[i] = len(palabras)
    return conteo
frases = ["Hola mundo", "Python es genial", "Me gusta programar"]
print(contar_palabras(frases))

print("")
print("ejercicio 15: Encontrar Clave Máxima en Diccionario")
def clave_maxima(diccionario):
    return max(diccionario, key=diccionario.get)
diccionario = {'a': 10, 'b': 20, 'c': 5}
print(clave_maxima(diccionario)) 


print("")
print("ejercicio 16: Palíndromos en una Lista")
def palindromos(palabras):
    palindromos = []
    for palabra in palabras:
        if palabra == palabra[::-1]:
            palindromos.append(palabra)
    return palindromos
palabras = ["ana", "oso", "hola", "level"]
print(palindromos(palabras)) 