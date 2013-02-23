
pin_zero = 7
pin_one = 8
pin_two = 25
pin_three = 24
pin_four = 23

def getLightControlLEDs():
    pins = [pin_four,pin_three,pin_two,pin_one,pin_zero]
    print "LightControlLEDs ::> " + str(pins)
    return pins
