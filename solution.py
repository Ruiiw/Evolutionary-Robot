import numpy
import pyrosim.pyrosim as pyrosim
import random
import os
import time
import constants as c

class SOLUTION:

    def __init__(self, nextAvailableID):
        self.weights = numpy.random.rand(c.numSensorneurons, c.numMotorneurons) * 2 -1
        self.myID = nextAvailableID

    def Start_Simulation(self, directOrGUI):
        self.Create_World()
        self.Create_Body()
        self.Create_Brain()
        os.system("python3 simulate.py" + directOrGUI + " " + str(self.myID) + " &")

    def Wait_For_Simulation_To_End(self):
        while not os.path.exists("fitness" + str(self.myID) + ".txt"):
            time.sleep(0.01)
        f = open("fitness" + str(self.myID) + ".txt", "r")
        fitVal = f.read()
        self.fitness = float(fitVal)
        f.close()
        os.system("rm fitness" + str(self.myID) + ".txt")

    def Create_World(self):
        pyrosim.Start_URDF("box.urdf")
        pyrosim.Send_Cube(name="box", pos=[-20, 20, 0.5] , size=[1, 1, 1])
        pyrosim.End()

    def Create_Body(self):
        pyrosim.Start_URDF("body.urdf")
        pyrosim.Send_Cube(name="Torso", pos=[0, 0, 1] , size=[1, 1, 0.5])
        pyrosim.Send_Joint(name = "Torso_FrontLeftLeg" , parent= "Torso" , child = "FrontLeftLeg" , type = "revolute", position = [0, -0.5, 1], jointAxis = "1 0 0")
        pyrosim.Send_Cube(name="FrontLeftLeg", pos=[-0.5, 0, -0.5] , size=[0.2, 0.2, 1])
        pyrosim.Send_Joint(name = "Torso_FrontRightLeg" , parent= "Torso" , child = "FrontRightLeg" , type = "revolute", position = [0, 0.5, 1], jointAxis = "1 0 0")
        pyrosim.Send_Cube(name="FrontRightLeg", pos=[-0.5, 0, -0.5] , size=[0.2, 0.2, 1])
        pyrosim.Send_Joint(name = "Torso_BackLeftLeg" , parent= "Torso" , child = "BackLeftLeg" , type = "revolute", position = [-0.5, 0, 1], jointAxis = "0 1 0")
        pyrosim.Send_Cube(name="BackLeftLeg", pos=[1, -0.5, -0.5] , size=[0.2, 0.2, 1])
        pyrosim.Send_Joint(name = "Torso_BackRightLeg" , parent= "Torso" , child = "BackRightLeg" , type = "revolute", position = [0.5, 0, 1], jointAxis = "0 1 0")
        pyrosim.Send_Cube(name="BackRightLeg", pos=[0, 0.5, -0.5] , size=[0.2, 0.2, 1])
        
        pyrosim.End()

    def Create_Brain(self):
        pyrosim.Start_NeuralNetwork("brain" + str(self.myID) + ".nndf")
        pyrosim.Send_Sensor_Neuron(name = 0 , linkName = "FrontLeftLeg")
        pyrosim.Send_Sensor_Neuron(name = 1 , linkName = "FrontRightLeg")
        pyrosim.Send_Sensor_Neuron(name = 2 , linkName = "BackLeftLeg")
        pyrosim.Send_Sensor_Neuron(name = 3 , linkName = "BackRightLeg")

        pyrosim.Send_Motor_Neuron( name = 4 , jointName = "Torso_FrontLeftLeg")
        pyrosim.Send_Motor_Neuron( name = 5 , jointName = "Torso_FrontRightLeg")
        pyrosim.Send_Motor_Neuron( name = 6 , jointName = "Torso_BackLeftLeg")
        pyrosim.Send_Motor_Neuron( name = 7 , jointName = "Torso_BackRightLeg")
        for currentRow in range(c.numSensorneurons):
            for currentColumn in range(c.numMotorneurons):
                pyrosim.Send_Synapse(sourceNeuronName = currentRow , targetNeuronName = currentColumn + c.numSensorneurons , weight = self.weights[currentRow][currentColumn])
        pyrosim.End()

    def Mutate(self):
        randomRow = random.randint(0, c.numSensorneurons-1)
        randomCol = random.randint(0, c.numMotorneurons-1)
        self.weights[randomRow,randomCol] = random.random()*2 -1

    def Set_ID(self, id):
        self.myID = id