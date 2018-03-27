#   File: Growth_1D.py
#   Author: Nawaf Abdullah
#   Creation Date: 22/Mar/2018
#   Description:
import random


class Producer:

    def __init__(self):
        self.geneticCode = []
        self.growth = []
        for i in range(10):
            r = random.randint(0, 100)
            if r < 50:
                self.geneticCode.append(True)
            else:
                self.geneticCode.append(False)

#   Phenotypes available
    def phenotype_0(self, x):
        y = x
        self.growth.append(y)

    def phenotype_1(self, x):
        y = x*2
        self.growth.append(y)

    def phenotype_2(self, x):
        y = x + 8
        self.growth.append(y)

    def phenotype_3(self, x):
        y = x*x*-x
        self.growth.append(y)

    def phenotype_4(self, x):
        y = x**0.5
        self.growth.append(y)

    def phenotype_5(self, x):
        y = x - 1
        self.growth.append(y)

    def phenotype_6(self, x):
        y = x*0
        self.growth.append(y)

    def phenotype_7(self, x):
        y = x*x+2
        self.growth.append(y)

    def phenotype_8(self, x):
        y = x*9
        self.growth.append(y)

    def phenotype_9(self, x):
        y = x+5*x
        self.growth.append(y)

    phenotypes = {0: phenotype_0, 1: phenotype_1, 2: phenotype_2,
                  3: phenotype_3, 4: phenotype_4, 5: phenotype_5,
                  6: phenotype_6, 7: phenotype_7, 8: phenotype_8,
                  9: phenotype_9}

#   input
    def feed(self, someNum):
        for i in range(len(self.phenotypes)):
            if self.geneticCode[i] is True:
                self.phenotypes[i](self, someNum)
            else:
                continue

    def get_growth(self):
        gross = 0
        for i in range(len(self.growth)):
            gross += self.growth[i]
        return gross


class Environment(Producer):

    def __init__(self, num_p):
        Producer.__init__(self)
        self.population = [Producer() for i in range(num_p)]

    def give_resources_all(self):
        r = random.randint(0, 100)
        for i in range(len(self.population)):
            self.population[i].feed(r)

    def give_resources_each(self):
        for i in range(len(self.population)):
            self.population[i].feed(random.randint(0, 100))

    def growth_select(self):
        self.population = sorted(self.population, key=lambda x: x.get_growth(), reverse=True)


env1 = Environment(5)
env1.give_resources_all()
env1.growth_select()
print(env1.population)
