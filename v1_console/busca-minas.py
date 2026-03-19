#Importando modulos para clases abstractas y biblioteca random
from abc import ABC, abstractmethod
import random

#Clase para obtener número entero para la variable multiplicador
class NumeroEntero:
    def obtener_entero(self, min, max):
        while True:
            try:
                multiplicador = int(input(f"Ingresar número entero ({min}-{max}):  "))
                if multiplicador < min or multiplicador > max:
                    raise Exception
                break
            except Exception as e:
                print("Ingresar un número entero válido⚠")
        return multiplicador

num_entero = NumeroEntero()
multiplicador = num_entero.obtener_entero(2,9)

#Interfaz para las casillas
class CasillaMolde(ABC):
    def __init__(self, numero):
        self.numero = numero
        
    @abstractmethod
    def revelar(self):
        pass
    
    @abstractmethod
    def es_bomba(self):
        pass
        
    def __str__(self):
        return f"Número: {self.numero}| {self.revelar()}"

#Casilla sin bomba
class CasillaNormal(CasillaMolde):
    def revelar(self):
        return "Limpio✅"
    
    def es_bomba(self):
        return False

#Casilla con bomba
class CasillaBomba(CasillaMolde):
    def revelar(self):
        return "Bomba💥"
    
    def es_bomba(self):
        return True

#Clase para crear bombas
class Bombas:
    def crear_bombas(self, multiplicador):
        bombas = set()
        cantidad =  multiplicador * multiplicador
        while len(bombas) < cantidad//3:
            bomba = random.randint(1,cantidad)
            bombas.add(bomba)
        return bombas

#Clase para armar casillas interactivas
class Casillas:
    def crear_casillas(self, multiplicador, bombas_lista):
        casillas_lista = list()
        cantidad =  multiplicador * multiplicador
        for num in range(1, cantidad+1):
            if num in bombas_lista:
                casilla = CasillaBomba(num)
                casillas_lista.append(casilla)
            else:
                casilla = CasillaNormal(num)
                casillas_lista.append(casilla)
        return casillas_lista

#Clase de alto nivel para gestionar la creación de bombas y casillas
class ArmadorCasillas:
    def __init__(self, multiplicador, bombas, casillas):
        self.multiplicador = multiplicador
        self.bombas = bombas
        self.casillas = casillas
        
    def armar_casillas(self):
        bombas_lista = self.bombas.crear_bombas(self.multiplicador)
        casillas_lista = self.casillas.crear_casillas(self.multiplicador, bombas_lista)
        return casillas_lista

#Creacion de objetos y armado de las casillas
bombas = Bombas()
casillas = Casillas()
armador_casillas = ArmadorCasillas(multiplicador, bombas, casillas)
casillas_lista = armador_casillas.armar_casillas()

#Clase para crear tablero de casillas
class Tablero:
    def crear_tablero(self, multiplicador, casillas_lista):
        for casilla in casillas_lista:
            if casilla.numero % multiplicador == 0:
                print(casilla.numero, end="\n")
            else:
                print(casilla.numero, end=" ")
        return f"Tablero creado✅"

tablero = Tablero()
print(tablero.crear_tablero(multiplicador, casillas_lista))

#Llamada al objeto tipo NumeroEntero para obtener la casilla elegida por el usuario
respuesta = num_entero.obtener_entero(1,multiplicador*multiplicador)

#Clase para comprobar respuesta
class Responder:
    def comprobar_respuesta(self, respuesta, casillas_lista):
        for c in casillas_lista:
            if c.numero == respuesta:
                print(c.revelar())
                if c.es_bomba():
                    return "Game-Over❌"
                else:
                    return "Winner✅"

responder = Responder()
print(responder.comprobar_respuesta(respuesta, casillas_lista))
