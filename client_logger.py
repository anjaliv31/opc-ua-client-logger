from opcua import Client
import time
import csv 
from datetime import datetime
import os
ENDPOINT = "opc.tcp://localhost:4840/freeopcua/server/"
OUTPUT_DIR="output"

os.makedirs(OUTPUT_DIR,exist_ok=True)
client=Client(ENDPOINT)
client.connect()
print("Connected to OPC UA Server")

objects = client.get_objects_node()
children=objects.get_children()

print("Browsing Objects node")
variable=[]
var_names=[]

for obj in children:
    try:
        ns=obj.nodeid.NamespaceIndex
        if ns ==0:
            continue
        temp_vars=[]
        temp_names=[]
        readable_vars=[]
        for v in obj.get_children():
            try:
                v.get_value()
                temp_vars.append(v)
                temp_names.append(v.get_browse_name().Name)
            except:
                pass
        if temp_vars:
            variables=temp_vars
            var_names=temp_names
            print("Using Object:",obj.get_browse_name())
            break
    except:
        pass

if not variables:
    raise Exception("No readable variables found")


print("Found Variables:", var_names)

current_hour= None
csv_file=None
writer=None

try:
    while True:
        now = datetime.now()
        hour_key=now.strftime("%Y-%m-%d_%H")

        if current_hour!=hour_key:
            if csv_file:
                csv_file.close()


            filename = f"{OUTPUT_DIR}/opcua_data_log.csv"
            csv_file=open(filename,"w",newline="")
            writer=csv.writer(csv_file)
            writer.writerow(["Timestamp"]+var_names)
            current_hour=hour_key

        values=[]
        for var in variables:
            try:
                values.append(var.get_value())
            except:
                values.append(None)

            writer.writerow([now.strftime("%Y-%m-%d %H:%M:%S")]+values)
            csv_file.flush()

            print("Logged data at",now.strftime("%Y-%m-%d %H:%M:%S"))
            time.sleep(60)

except KeyboardInterrupt:
        print("Logging stopped")

client.disconnect()