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

    setRGB(0, 255, 0)
    
    while True:
        try:
            # set threshold distance (rotary angle sensor)
            threshold = grovepi.analogRead(potentiometer)
            
            # measure distance (ultrasonic ranger)
            dist_sensor = grovepi.analogRead(sensor)


            print("Threshold reading: " + threshold)
            print("Sensor reading: " + dist_sensor)

            # check object is less than threshold
            if (dist_sensor <= threshold):
                output = threshold + " OBJ PRES\n" + dist_sensor
                setText(output)
            else:
                output = threshold + '\n' + dist_sensor
                setText(output)
        except:
            print("Error executing")

        time.sleep(0.1)