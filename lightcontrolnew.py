import RPi.GPIO as GPIO
import pins

class LightControl:
    numberOfLightsOn = 0
    pinSetting = "0,0,0,0,0,"

    lights_none = "0,0,0,0,0"
    lights_one = "0,0,0,0,1"
    lights_two = "0,0,0,1,1"
    lights_three = "0,0,1,1,1"
    lights_four = "0,1,1,1,1"
    lights_five = "1,1,1,1,1"
    
    #num should be an integer
    def setLights(self, num):
        print "setting lights " + str(num)
        
        self.numberOfLightsOn = num

        if num == 0:
            self.pinSetting = self.lights_none
        elif num == 1:
            self.pinSetting = self.lights_one
        elif num == 2:
            self.pinSetting = self.lights_two
        elif num == 3:
            self.pinSetting = self.lights_three
        elif num == 4:
            self.pinSetting = self.lights_four
        elif num == 5:
            self.pinSetting = self.lights_five
        else:
            #error
            print "error occurred"
            self.pinSetting = self.lights_none
            self.numberOfLightsOn = 0

        print "setting pins :: " + str(self.numberOfLightsOn)
        self.setPins(self.numberOfLightsOn)


    def setPins(self, num):
        print "setting pins, output should be \"" + self.pinSetting + "\" (" + str(self.numberOfLightsOn) + ")"
        pinstates = self.pinSetting.split(',')
        print "pins :: " + str(pinstates)
        
        for p in pinstates:
            print "pin ::::: " + str(p)

        raspPiPins = pins.getLightControlLEDs()
        print "calling pins class :: >> " + str(raspPiPins)
        
        index = 0
        for rppNum in raspPiPins:
            self.applyPin(rppNum, pinstates[index])
            index += 1

    def applyPin(self, pinNum, pinState):
        print "applying " + str(pinState) + " to pin " + str(pinNum)








