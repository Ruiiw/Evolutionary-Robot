import numpy
import pyrosim.pyrosim as pyrosim
import constants as c

class SENSOR:

    def __init__(self, linkName):

        self.linkName = linkName
        self.values = numpy.zeros(c.numTimeSteps)

    def Get_Value(self, i):
        self.values[i] = pyrosim.Get_Touch_Sensor_Value_For_Link(self.linkName)

    def Save_Value(self):
        numpy.save('data/sensorData.npy', self.values)