from opcua import Client

client=Client("opc.tcp://localhost:4840/freeopcua/server/")
client.connect()
print("Connected to the server")

objects = client.get_objects_node()
children = objects.get_children()

for child in children:
    print("Object:",child)

    for var in child.get_children():
        try:
            value=var.get_value()
            print("Variable:",var,"Value:",value)
        except Exception as e:
            print("Variable:",var,"Value:<not readable>")
client.disconnect()