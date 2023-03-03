import time
import grovepi
from grove_rgb_lcd import *

if __name__ == "__main__":
    # set the bus
    grovepi.set_bus("RPI_1")

    # set rotary angle sensor to A0
    potentiometer = 0

    # set distance sensor
    sensor = 4

    grovepi.pinMode(potentiometer, "INPUT")
    grovepi.pinMode(sensor, "OUTPUT") 

    output = ""
    setRGB(0, 255, 0)
    
    while True:
        try:
            # threshold and dist_sensor are both ints
            # set threshold distance (rotary angle sensor)
            threshold = grovepi.analogRead(potentiometer)
            
            # measure distance (ultrasonic ranger)
            dist_sensor = grovepi.ultrasonicRead(sensor)

            # check object is less than threshold
            if (dist_sensor <= threshold):
                output = str(threshold) + "cm OBJ PRES\n" + str(dist_sensor)
                setText_norefresh(output)
            else:
                output = str(threshold) + 'cm\n' + str(dist_sensor)
                setText_norefresh(output)
        except:
            print("Error executing")
        time.sleep(.5)   