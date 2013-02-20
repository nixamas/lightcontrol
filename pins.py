
pin_one = 12
pin_two = 22
pin_three = 32
pin_four = 42
pin_five = 52

def getLightControlLEDs():
    pins = [pin_one,pin_two,pin_three,pin_four,pin_five]
    print "LightControlLEDs ::> " + str(pins)
    return pins
