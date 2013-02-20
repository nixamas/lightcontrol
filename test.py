import lightcontrolnew as LC

print "Starting Test.py ....."
myLC = LC.LightControl();
print "light control type :: " + str(type(myLC))
myLC.setLights(1)
