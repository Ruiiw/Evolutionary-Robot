import pybullet as p
import pyrosim.pyrosim as pyrosim

class WORLD:

    def __init__(self):
        self.planeId = p.loadURDF("plane.urdf")
        self.box = p.loadURDF("box.urdf")
        