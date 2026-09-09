from gpiozero import DigitalInputDevice
import time

d0input = DigitalInputDevice(4)
d1input = DigitalInputDevice(14)
d2input = DigitalInputDevice(15)
d3input = DigitalInputDevice(18)
sensordata = []


while True:
	print("start wait")
	time.sleep(2)
	print("scan")
	#sensordata.clear()
	with open("sensordata.txt", "w") as sensor:

		if (not d0input.value):
			#print(d0input.value)
			sensor.write("0, ")
			#time.sleep(2)
		else:
			#print(d0input.value)
			sensor.write("1, ")
			#time.sleep(2)

		if(not d1input.value):
			#print(d1input.value)
			sensor.write("0, ")
			#time.sleep(2)
		else:
			#print(d1input.value)
			sensor.write("1, ")
			#time.sleep(2)

		if (not d2input.value):
			#print(d2input.value)
			sensor.write("0, ")
			#time.sleep(2)
		else:
			#print(d2input.value)
			sensor.write("1, ")
			#time.sleep(2)

		if(not d3input.value):
			#print(d3input.value)
			sensor.write("0")
			#time.sleep(2)
		else:
			#print(d3input.value)
			sensor.write("1")
			#time.sleep(2)


		sensor.close()
#	with open("sensordata.txt") as sensor:
#		print(sensor.read())
	def read_sensordaten_txt():

	        with open("sensordata.txt", "r", encoding="utf-8") as f:
	                data = [str(x.strip()) for x in f.read().split(",")]
	                return data

	print(read_sensordaten_txt())

	time.sleep(2)
