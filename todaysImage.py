#!/usr/bin/env python3

import requests as re
import json
from PIL import Image
import urllib.request
import datetime
import time

def pod():
	print("This program displays the NASA picture of the day")
	print("Choose from the following menu")
	print("1. Today's picture")
	print("2. Custom date")
	choice = int(input("Your choice: "))
	
	if choice == 1:
		date = datetime.date.today()
	else:
		date = input("Enter date in YYYY-MM-DD format: ")
		
	result = re.get("https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY", params={'date': date})
	
	if result.status_code == 200:
		data = result.text
		json_parse = json.loads(data)
		url = json_parse['url']
		print("Downloading the image... please wait!")
		urllib.request.urlretrieve(url, str(date)+'.jpg')
		img = Image.open(str(date)+'.jpg')
		img.show()
		print("Explanation: ")
		print(json_parse['explanation'])
	
	else:
		print("Error retrieving the image")
		if choice==2:
			res = input("Did you give the date in the correct format(y/n):")
			if res=='y':
				print("It seems like there was an error retrieving the data from the NASA website")
			else:
				print("-->Retry<--")
				pod()
				return

pod()
