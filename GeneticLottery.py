#   File: Growth_1D.py
#   Author: Nawaf Abdullah
#   Creation Date: 22/Mar/2018
#   Description:
import random


class Producer:
    growth = []

#   genotype, or a list of phenotype switches.
    geneticCode = []

#   genetic lottery
    def __init__(self):
        for i in range(9):
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
        y = x*x*x
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
    def input(self, someNum):
        for i in range(len(self.phenotypes)):
            if self.geneticCode[i] is True:
                self.phenotypes[i](someNum)
            else:
                continue

    def get_growth(self):
        gross = 0
        for i in range(len(self.growth)):
            gross += self.growth[i]
        return gross



