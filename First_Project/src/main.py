import inputs as var
import serial, time, base, http-lib, mqtt-lib 

# Base
base = base.Connection()

# HTTP
http = http-lib.HTTP()
    
# MQTT
mqtt = mqtt-lib.MQTT()

def control_base(self):
    base.check_base()

# HTTP Implementations
def http_get(self):
    http.set_PDP()
    http.connect()
    http.http_get()
    
 def http_post(self): 
    http.set_PDP()
    http.connect()
    http.http_post()

# MQTT Implementations
def mqtt_sub(self):
    mqtt.connect()
    mqtt.subscribe()

def mqtt_pub(self):
    mqtt.connect()
    mqtt.publish()
    
if __name__ == "__main__":
    modem = serial.Serial(var.port, var.baudrate, timeout=5)
    # Check
    control_base()

    # HTTP
    http_get()

    # MQTT
    mqtt_pub()

    modem.close()
