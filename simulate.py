import pybullet as p
import time

physicsClient = p.connect(p.GUI)
for i in range(300):
    print(i)
    p.stepSimulation()
    time.sleep(1/60)
p.disconnect()