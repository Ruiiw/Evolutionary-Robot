from solution import SOLUTION
import constants as c
import copy
import os

class PARALLEL_HILL_CLIMBER:

    def __init__(self):
        self.nextAvailableID = 0
        self.parents = {}
        for i in range(c.populationSize):
            self.parents[i] = SOLUTION(self.nextAvailableID)
            self.nextAvailableID += 1
        
        os.system("rm brain*.nndf")
        os.system("rm fitness*.txt")

    def Evolve(self):
        self.Evaluate(self.parents)
        
        for currentGeneration in range(c.numberOfGenerations):
            self.Evolve_For_One_Generation()

    def Evolve_For_One_Generation(self):
        self.Spawn()
        self.Mutate()
        self.Evaluate(self.children)
        self.Print()
        self.Select()

    def Spawn(self):
        self.children = {}
        for i in self.parents:
            self.children[i] = copy.deepcopy(self.parents[i])
            self.children[i].Set_ID(self.nextAvailableID)
            self.nextAvailableID += 1

    def Mutate(self):
        for child in self.children:
            self.children[child].Mutate()

    def Select(self):
        for i in self.parents:
            if self.parents[i].fitness < self.children[i].fitness:
                self.parents[i] = self.children[i]

    def Print(self):
        print("\n")
        for i in self.parents:
            print("parent fitness: ", self.parents[i].fitness, "child fitness:", self.children[i].fitness)
        print("\n")
       

    def Show_Best(self):
        maxFit = self.parents[0].fitness
        for i in self.parents:
            maxFit = max(self.parents[i].fitness, maxFit)

        for i in self.parents:
            if self.parents[i].fitness == maxFit:
                self.parents[i].Start_Simulation(' GUI')

    def Evaluate(self, solutions):
        for parent in solutions:
            solutions[parent].Start_Simulation(" DIRECT")

        for parent in solutions:
            solutions[parent].Wait_For_Simulation_To_End()

    

