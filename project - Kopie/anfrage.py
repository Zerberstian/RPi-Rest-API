import requests
import time
print("abfrage laeuft")

def read_text_file():
    with open("../project/RPi-Rest-API/x-api_key.txt", "r", encoding="utf-8") as f:
       return f.read().strip()

def read_sensordaten_txt():

        with open("sensordata.txt", "r", encoding="utf-8") as f:
                data = [int(x.strip()) for x in f.read().split(",")]
                return data

sensordaten = read_sensordaten_txt()

print(sensordaten)


#dings_key = read_text_file()

#print(dings_key)
while True:
	# anfrage 1-4
	for i in range(4):
		url = f"http://192.168.189.22:5000/api/plants/{i+1}"

		header={
		"X-API-Key": read_text_file(),
		"Content-Type": "application/json"
		}

		daten = {
		"waterlevel": read_sensordaten_txt()[i]
		}

		response = requests.patch(
			url,
			headers=header,
			json=daten,
			timeout=5
		)
		print(
			f"Pflanze {i+1}: "
			f"HTTP {response.status_code} - {response.text}"
		)
	print("--------------------------------------------------------------\n")
	time.sleep(20)
