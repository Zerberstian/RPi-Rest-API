from gpiozero import DigitalInputDevice
import time
import select
import sys

d0input = DigitalInputDevice(4)
d1input = DigitalInputDevice(14)
d2input = DigitalInputDevice(15)
d3input = DigitalInputDevice(18)

inputs = [d0input, d1input, d2input, d3input]



while True:
#	print("start wait")
	time.sleep(5)

#	print("scan")

	# Read the four sensors
	sensor_values = [int(not sensor.value) for sensor in inputs]

	# Write the values to the file
	with open("sensordata.txt", "w") as sensor:
		sensor.write(",".join(map(str, sensor_values)))

	# Read and display the file
	#with open("sensordata.txt", "r") as sensor:
	#	print(sensor.read())


	def read_sensordaten_txt():

	        with open("sensordata.txt", "r", encoding="utf-8") as f:
	                data = [int(x.strip()) for x in f.read().split(",")]
	                return data

#	print(read_sensordaten_txt())

