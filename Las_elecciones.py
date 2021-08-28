"""Realizar un programa en el cual se decida el ganador de unas elecciones.

El programa primero recibe un número  N , la cantidad de votos totales que se realizaron. 
Luego recibe  N  votos en formato string, cada uno consiste en el nombre del candidato seleccionado. 
El programa debe calcular el ganador e imprimir su nombre, para este ejemplo se asume que no hay empates. 
Los nombres y la cantidad de candidatos es desconocida.
"""
from statistics import mode 

cantidad_votos = int(input("Cantidad de votos: "))
votos = []

while cantidad_votos > len(votos):
    voto = input("Ingresa su voto: ")
    votos.append(voto)

print(mode(votos))


