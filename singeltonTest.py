from Phidget22.Devices.Stepper import *
from Phidget22.Devices.RCServo import *
from Phidget22.Devices.DCMotor import *
import time
from Phidget22.Devices.VoltageInput import *

#the Index: the Port , I AM NOT SURE HOW ACCURATE THIS IS TO THE PORTS

mapping = {0:3, 1:5, 2:1, 3:2}

motorsch = []
class SingletonMeta(type):
    _instances = {}

    def __call__(cls, num, *args, **kwargs):
        if num not in cls._instances:
            cls._instances[num] = super().__call__(num, *args, **kwargs)
        return cls._instances[num]

class Singleton(metaclass=SingletonMeta):
    def __init__(self, num):
        self.num = num
        self.theInstance = 0
        self.VHubSerial_motors = 697178

    def createInstance(self):
        ch_lsdm = VoltageInput()
        print("made voltage sensor")
        VHubSerial_motors = 697178
        ch_lsdm.setDeviceSerialNumber(VHubSerial_motors)
        print("set voltage sensor vinthub as: ", VHubSerial_motors)
        numInstance = mapping[self.num]
        ch_lsdm.setHubPort(numInstance)
        print("set voltage sensror hub port as", ch_lsdm.getHubPort())
        self.theInstance = ch_lsdm
        # ch_lsdm.openWaitForAttachment(5000)
        print("ch_lsdm attached: ", ch_lsdm.getAttached())
    def useThatInstance(self):
        self.theInstance.getVoltage()
        print(f"motorsch[{self.num}] is attached: {self.theInstance.getAttached()}")
        print("max voltage:", self.theInstance.getMaxVoltage())
        print("min voltage: ", self.theInstance.getMinVoltage())
        return self.theInstance.getVoltage()



if __name__ == "__main__":
    s1 = Singleton(1)
    s2 = Singleton(2)
    # try doing a while loop
    while s1 != s2:
        print("Singleton works, both variables contain the same instance.")
        s1.createInstance()
        s2.createInstance()

    else:
        print("Singleton failed, variables contain different instances.")