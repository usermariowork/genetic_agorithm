import numpy as np
import random
import secrets

popuNum = 5 #numero de personas que conformarán la poblacion

class Person:
  def __init__(self):
      self.chromosome = np.random.randint(2, size=8) #una persona tiene un cromosoma de 8 genes, aleatoriamente 0s y 1s
      self.fitness = self.fitnessFunction() #tiene fitness que se calcula con fitnessFFunction y depende del numero de 1s que tenga su cromosoma
      self.numberxd = 0 #

  def fitnessFunction(self):
      contador = 0
      i = 0
      while i < 8:
          if self.chromosome[i] == 1:
              contador = contador + 1
          i += 1
      return contador


def createPopulation(numPersonas):
    popu = []
    auxPersona = None

    uwu = 0
    while uwu < numPersonas:
        auxPersona = Person()
        auxPersona.numberxd = uwu
        popu.append(auxPersona)
        uwu += 1
    return popu

def printPopu(population):
    unu = 0
    while unu < popuNum:
        print(population[unu].chromosome)
        unu += 1

def rouletteWheel(population):
    roulette = []
    n = 0
    f = 0

    unu = 0
    while unu < popuNum:
        n = population[unu].numberxd
        f = population[unu].fitness
        aux = 0
        while aux < f:
            roulette.append(n)
            aux += 1
        unu += 1
    print(roulette)
    random.shuffle(roulette) #reacomodamos la lista aleatoriamente
    print(roulette)
    print(secrets.choice(roulette)) #secrets.choice elige un elemento aleatorio de la lista


def mainuwu():
    population = createPopulation(popuNum)
    printPopu(population)
    rouletteWheel(population)

mainuwu()

#print(population[0].chromosome)
#print(population[0].chromosome[0])


'''
c = Person()
c2 = Person()
'''


'''
numPersonas = 10
popu = []
auxPersona = None

uwu = 0
while uwu < numPersonas:
    auxPersona = Person()
    popu.append(auxPersona)
    uwu += 1

print(popu[0].chromosome)
print(popu[0].chromosome[0])

'''



#c = Person()
#population = createPopulation()
#population.append(c)

#print(population[0].chromosome)
#print(population[0].chromosome[0])




'''
print(c.chromosome)
print(c2.chromosome)
print(c2.fitness)
'''



