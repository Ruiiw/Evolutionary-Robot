import pybullet as p

class WORLD:

    def __init__(self):
        
        self.planeId = p.loadURDF("plane.urdf")
        # self.robotId = p.loadURDF("body.urdf")
        