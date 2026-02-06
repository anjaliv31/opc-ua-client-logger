from opcua import Server
import time
import random
server = Server()
server.set_endpoint("opc.tcp://localhost:4840/freeocua/server/")

uri="http://examples.freeopcua.github.io"
idx = server.register_namespace(uri)

objects = server.get_objects_node()
myobj = objects.add_object(idx, "MyObject")

temperature=myobj.add_variable(idx,"Temperature",25.0)
pressure=myobj.add_variable(idx,"Pressure",1.0)
speed = myobj.add_variable(idx,"Speed",100)
vibration=myobj.add_variable(idx,"Vibration",0.5)
humidity=myobj.add_variable(idx,"Humidity",60)
flow=myobj.add_variable(idx,"Flow",10)
voltage=myobj.add_variable(idx,"Voltage",230)
current=myobj.add_variable(idx,"Current",5)
power = myobj.add_variable(idx,"Power",1200)
frequency=myobj.add_variable(idx,"Frequency",50)

variables=[
    temperature,pressure, speed, vibration, humidity, flow,
    voltage, current, power, frequency
]

for v in variables:
    v.set_writable()

server.start()
print("OPC UA Server started at opc.tcp://localhost:4840/server/")

try:
    while True:
        temperature.set_value(random.uniform(20,30))
        pressure.set_value(random.uniform(0.8,1.2))
        speed.set_value(random.randint(80,120))
        vibration.set_value(random.uniform(0.1,1.0))
        humidity.set_value(random.uniform(40,80))
        flow.set_value(random.uniform(5,20))
        voltage.set_value(random.uniform(220,240))
        current.set_value(random.uniform(3,10))
        power.set_value(random.uniform(1000,2000))
        frequency.set_value(random.uniform(49,51))
        time.sleep(2)
finally:
    server.stop()