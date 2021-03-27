import numpy as np
import random
import secrets

popuNum = 5 #numero de personas que conformarán la poblacion

class Person:
  def __init__(self):
      self.chromosome = np.random.randint(2, size=8) #una persona tiene un cromosoma de 8 genes, aleatoriamente 0s y 1s
      self.fitness = self.fitnessFunction() #tiene fitness que se calcula con fitnessFFunction y depende del numero de 1s que tenga su cromosoma
      self.numberxd = 0 #numero de persona, se definirá cuando se inicialice la poblacion

  def fitnessFunction(self): #funcion para obtener el fitness de una persona
      contador = 0
      i = 0
      while i < 8:
          if self.chromosome[i] == 1:
              contador = contador + 1
          i += 1
      return contador


def createPopulation(numPersonas): #creamos la poblacion
    popu = [] #lista que almacenará la poblacion
    auxPersona = None #auxiliar que ayudará a meter a cada pesona a la poblacion

    uwu = 0 #contador del ciclo while
    while uwu < numPersonas:
        auxPersona = Person()
        auxPersona.numberxd = uwu
        popu.append(auxPersona) #añadimos a la persona a la poblacion
        uwu += 1
    return popu #retornamos a la población generada

def printPopu(population): #imprimimos a la poblacion
    unu = 0
    while unu < popuNum:
        print(population[unu].chromosome)
        unu += 1

def rouletteWheel(population): #usamos la roulette wheel en la poblacion
    roulette = [] #esta lista contendrá el numero de persona n veces dependiendo de su fitness
    #por ejemplo, una persona con un fitness de 6 aparecerá su número de persona 6 veces en esta lista
    n = 0 #auxiliar para el numero de la persona
    f = 0 #auxiliar para el fitness de la persona

    unu = 0
    while unu < popuNum:
        n = population[unu].numberxd
        f = population[unu].fitness
        aux = 0
        while aux < f:
            roulette.append(n)
            aux += 1
        unu += 1
    #print(roulette)
    random.shuffle(roulette) #reacomodamos la lista aleatoriamente
    #print(roulette)
    return roulette

def crossover(population, roulette):
    newPopulation = []
    hijo = Person()

    person1 = secrets.choice(roulette)
    #ahora hacemos un ciclo while para quitar a la persona 1 de la ruleta, lo hacemos en un ciclo ya que puede aparecer varias veces
    posicion = 0
    while posicion < len(roulette):
        if roulette[posicion] == person1:
            roulette.pop(posicion)
        else:
            posicion = posicion + 1

    #ahora si podemos encontrar a la persona 2 con quien aparearse
    person2 = secrets.choice(roulette)

    #tambien eliminamos a la persona 2 de la ruleta
    posicion = 0
    while posicion < len(roulette):
        if roulette[posicion] == person2:
            roulette.pop(posicion)
        else:
            posicion = posicion + 1

    #HIJO 1
    aux0 = 0  # auxiliar del ciclo while 1
    aux1 = 4  # auxiliar del ciclo while 2
    while aux0 < 4:
        hijo[aux0] = population[person1].chromosome[aux0]
        aux0 += 1
    while aux1 < 8:
        hijo[aux1] = population[person2].chromosome[aux1]
        aux1 += 1

    newPopulation.append(hijo)

    print("persona 1")
    print(person1)

    print("persona 2")
    print(person1)

    print("hijo 1")
    print(hijo)

    #HIJO 2
    aux2 = 4
    aux3 = 0
    while aux2 < 8:
        hijo[aux2] = population[person1].chromosome[aux2]
        aux2 += 1
    while aux3 < 4:
        hijo[aux3] = population[person2].chromosome[aux3]
        aux3 += 1

    newPopulation.append(hijo)

    print("hijo 2")
    print(hijo)

    print()
    print("nueva poblacion")
    printPopu(newPopulation)








def mainuwu():
    population = createPopulation(popuNum)
    printPopu(population)
    r = rouletteWheel(population)
    crossover(population, r)

mainuwu()

#print(population[0].chromosome)
#print(population[0].chromosome[0])

