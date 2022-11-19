import time
import sys
import ibmiotf.application
import ibmiotf.device
import random

#Provide your IBM Watson Device Credentials
organization = "s0uwr0"
deviceType = "weather_device"
deviceId = "vpsr_weather"
authMethod = "token"
authToken = "9mMbsPkwZ-NtBMUAPc"

# Initialize GPIO



def myCommandCallback(cmd):
    print("Command received: %s" % cmd.data['command'])
    print(cmd)
        


try:
	deviceOptions = {"org": organization, "type": deviceType, "id": deviceId, "auth-method": authMethod, "auth-token": authToken}
	deviceCli = ibmiotf.device.Client(deviceOptions)
	#..............................................
	
except Exception as e:
	print("Caught exception connecting device: %s" % str(e))
	sys.exit()

# Connect and send a datapoint "hello" with value "world" into the cloud as an event of type "greeting" 10 times
deviceCli.connect()

while True:
        #Get Sensor Data from DHT11
        Propane =  random.randint(0, 2000);
        Carbon_Monoxide = random.randint(0, 100);
        LPG= random.randint(0, 2000);
        Methane = random.randint(0, 1000);
        Hydrogen= random.randint(0, 5000);
        data = {"d":{
    "Propane": Propane,
  "Carbon_Monoxide": Carbon_Monoxide,
   "LPG": LPG,
   "Methane": Methane,
    "Hydrogen":Hydrogen
}
}
        #print data
        def myOnPublishCallback():
            print ("Published Propane = %s ppm" % Propane, "LPG = %s ppm" % LPG, "to IBM Watson")

        success = deviceCli.publishEvent("IoTSensor", "json", data, qos=0, on_publish=myOnPublishCallback)
        if not success:
            print("Not connected to IoTF")
        time.sleep(1)
        
        deviceCli.commandCallback = myCommandCallback

# Disconnect the device and application from the cloud
deviceCli.disconnect()
