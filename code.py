from pybricks.hubs import InventorHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

hub = InventorHub()

# setup
# E is the Spin motor
# F is the Give-Motor
#b is the UltraSonicsensor

spin_motor = Motor(Port.E)
give_motor = Motor(Port.F)
hub.speaker.volume(25)

def pos(motor, angle):
    while motor.angle() != angle:
        motor.run(25)
    
    motor.stop()

melody = [
    (392, 500), (392, 500), (440, 750), (392, 250), (349, 500), (349, 500), (330, 1000),  # We're no strangers to love
    (262, 500), (262, 500), (349, 750), (294, 250), (330, 500), (349, 500), (392, 1000),  # You know the rules and so do I
    (440, 500), (392, 500), (349, 500), (330, 500), (294, 500),  # A full commitment's what I'm thinking of
    (262, 500), (262, 500), (294, 750), (294, 250), (330, 500), (349, 500), (392, 1000)  # You wouldn't get this from any other guy
]


wait(500)

#setup 2
UltrasonicSensor(Port.B).lights.off()
#pos(spin_motor, 0)
wait(1000)
give_motor.run_until_stalled(200)
give_motor.run_until_stalled(200)
spin_motor.stop()
give_motor.stop()

# loop
while True:
    if UltrasonicSensor(Port.B).distance() <= 100:
        UltrasonicSensor(Port.B).lights.on(50)
        spin_motor.hold()
        #pos(spin_motor, 0)
        give_motor.run_until_stalled(-200)
        give_motor.run_until_stalled(-200)

        for note, duration in melody:
            hub.speaker.beep(note, duration)
            wait(duration)

        interrupt()
        #unknown command, stops algorithm of undefineness
    else:
        UltrasonicSensor(Port.B).lights.off()
        spin_motor.run(1000)
        
