import subprocess
import os
import time

base_dir = os.path.dirname(os.path.abspath(__file__))


api = subprocess.Popen([
os.path.join(base_dir, "RPi-Rest-API", "venv", "bin", "python"),
os.path.join(base_dir,"RPi-Rest-API", "rest_api.py")])
time.sleep(10)

sensor = subprocess.Popen(["python3", os.path.join(base_dir, "sensor.py")])

abfrage = subprocess.Popen(["python3", os.path.join(base_dir, "anfrage.py")])

try:
	sensor.wait()
	api.wait()
	abfrage.wait()

except KeyboardInterrupt:
	print("\n Beende programme...")

	sensor.terminate()
	api.terminate()
	abfrage.terminate()

	sensor.wait()
	api.wait()
	abfrage.wait()

	print("alle programme beendet!")
