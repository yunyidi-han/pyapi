#!/usr/bin/python3
import requests
import argparse

def hard(photos):
	#photoList = []
	for photo in photos:
		#photoList.append()
		print(photo['img_src'])
		
def harder(photos):
	for photo in photos:
		print(f"Rover: {photo['rover']['name']}")
		print(f"Date: {photo['earth_date']}")
		print(photo['img_src'])
		print()
		
def hardest(photos, camera):
	for photo in photos:
		if photo['camera']['name'] == camera.upper():
			print(f"Camera: {photo['camera']['name']}")
			print(f"Rover: {photo['rover']['name']}")
			print(f"Date: {photo['earth_date']}")
			print(photo['img_src'])
			print()

def main():
	parser = argparse.ArgumentParser(description='Choose which challenge and cam')
	parser.add_argument('-d', choices=['hard','harder','hardest'], help='choose a difficulty')
	parser.add_argument('-c', choices=["FHAZ","RHAZ","MAST","CHEMCAM","NAVCAM"], default='FHAZ', help='pick a camera for hardest challenge')
	args = parser.parse_args()
	apodresp = requests.get("https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?sol=1000&api_key=DEMO_KEY").json()['photos']
	if args.d.lower() == 'hard':
		hard(apodresp)
	elif args.d.lower() == 'harder':
		harder(apodresp)
	elif args.d.lower() == 'hardest':
		hardest(apodresp,args.c)
	
	#print(apodresp)
	

if __name__ == "__main__":
	main()
