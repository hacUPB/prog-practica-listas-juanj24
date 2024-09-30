# Ejercicio 1: Suma de elementos en una lista de listas
def suma_matriz(matriz):
    suma = 0

    for filas in matriz:
        for dato in filas:
            suma+=dato
    return suma

# Ejercicio 2: Encontrar el valor máximo en una matriz
def maximo_matriz(matriz):
   
    if not matriz:
        return None
    
    
    maximo = matriz[0][0]
    

    for fila in matriz:
        for numero in fila:
            if numero > maximo:
                maximo = numero  
    return maximo  

    

# Ejercicio 3: Verificar si un número es primo
def es_primo(n):
   
   
   
    if n <= 1:  
        return False
   
    for i in range(2, n):  
        if n % i == 0:  
            return False
    return True

# Ejercicio 4: Transponer una matriz
def transponer_matriz(matriz):
    transpuesta = []
    
    # Recorremos por columnas
    for i in range(len(matriz[0])):  
        nueva_fila = []
        for fila in matriz:  
            nueva_fila.append(fila[i])  
        transpuesta.append(nueva_fila)  
    return transpuesta


# Ejercicio 5: Filtrar números pares
def filtrar_pares(lista):

    pares = []
    for elemento in lista:
        if elemento % 2 == 0:
            pares.append(elemento)
    return pares

     

# Ejercicio 6: Contar la cantidad de palabras en una frase

def contar_palabras(frase):

    palabras = frase.split()
    
   
    return len(palabras)




# Ejercicio 7: Crear una tabla de multiplicar
def tabla_multiplicar(n):

    tabla = []
    for i in range(1, 11):
        tabla.append(n * i)
    return tabla
   
   



    

# Ejercicio 8: Contar números negativos en una lista
def contar_negativos(lista):
 
    contador = 0
    for numero in lista:
        if numero < 0:
            contador += 1
    return contador


# Ejercicio 9: Determinar si una lista está ordenada
def lista_ordenada(lista):
  
   
    if len(lista) <= 1:
        return True
    
    
    for i in range(len(lista) - 1):
        if lista[i] > lista[i + 1]:
            return False
    
    return True


# Ejercicio 10: Cifrar un texto con el cifrado César
def cifrado_cesar(texto, desplazamiento):
    """
    Recibe un texto y un desplazamiento, y devuelve el texto cifrado usando el cifrado César.
    Incluir el código aquí para cifrar el texto con el cifrado César.
    """
    pass


#Aquí comienza el progrma principal. No modifiques el código debajo de esta línea.
def main():
    pass


if __name__ == "__main__":
    main()