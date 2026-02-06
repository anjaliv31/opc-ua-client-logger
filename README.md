Assignment 2 – Data Integration using OPC UA

Overview

This project demonstrates industrial data integration using the OPC UA protocol. A Python-based OPC UA server simulates industrial sensor data, and a client application connects to the server, dynamically browses the address space, reads real-time values from 10 OPC UA tags, and logs the data into hour-wise CSV files.

Objectives

Implement an OPC UA server to simulate industrial data
Create 10 OPC UA tags with continuously changing values
Develop an OPC UA client to collect data from the server
Log timestamped data into hourly CSV files
Demonstrate continuous monitoring across multiple hours

Technologies Used

Python,
OPC UA (freeopcua library),
CSV for data storage.


OPC UA Tags Implemented

The OPC UA server simulates the following 10 tags:
Temperature
Pressure
Speed
Vibration
Humidity
Flow
Voltage
Current
Power
Frequency
Each tag is periodically updated to simulate real industrial sensor readings.

How the System Works

OPC UA Server (server.py)

Creates a local OPC UA server
Registers a custom namespace
Defines a custom object (MyObject)
Adds 10 sensor variables
Continuously updates values at regular intervals

OPC UA Client (client_logger.py)

Connects to the OPC UA server
Dynamically browses the address space
Automatically detects custom variables
Reads tag values every minute
Logs data into separate CSV files for each hour

Key Features

Dynamic OPC UA node browsing (no hardcoded NodeIds)
Hour-wise CSV logging
Timestamped industrial data
Robust error handling
Fully compliant with Assignment 2 requirements

Conclusion

This project successfully demonstrates OPC UA–based data integration by simulating industrial sensor data, collecting values using a client application, and logging timestamped data into hourly CSV files.
