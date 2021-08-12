"""
La conjetura del Dr. Lothar
Escriba un programa que reciba un numero del usuario y repita el siguiente proceso usando un while:

Si el numero es par, se debe dividir por  .
Si el numero es impar, se debe multiplicar por  y sumar .
Este proceso se repite hasta llegar al numero 1 y luego muestra en pantalla la cantidad de pasos que tardó en llegar.

El input se recibe utilizando el comando input() sin ningún mensaje dentro de los paréntesis. El output se muestra usando print() y mostrándo ÚNICAMENTE el resultado, sin ningún texto adicional.

Input Format

El programa recibe un número entero .

Output Format

El programa imprime la cantidad de pasos usados para llegar al número ."""


n = int(input())
lista = []

while n > 1:

    if n % 2 == 0:
        n = n / 2
        lista.append(n)
          

    elif n % 2 != 0:
        n = (n * 3) + 1
        lista.append(n)
        

    elif n == 1:
        break

    
print(len(lista))