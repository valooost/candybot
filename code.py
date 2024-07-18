from pybricks.hubs import InventorHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

hub = InventorHub()

# setup
# E is the Spin motor
# F is the Give-Motor

spin_motor = Motor(Port.E)
give_motor = Motor(Port.F)

def pos(angle):
    while give_motor.angle() != angle:
        give_motor.run(1)

wait(500)

pos(0)
spin_motor.hold()
give_motor.hold()
give_motor.stop()

# loop
while True:
#for hanging the loop
    print("Hello World")
