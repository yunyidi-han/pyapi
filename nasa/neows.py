#!/usr/bin/python3
import requests

## Define NEOW URL 
NEOURL = "https://api.nasa.gov/neo/rest/v1/feed?"

def main():
    ## first I want to grab my credentials
    with open("/home/student/nasa.creds", "r") as mycreds:
        nasacreds = mycreds.read()
    ## remove any newline characters from the api_key
    nasacreds = "api_key=" + nasacreds.strip("\n")        

    ## update the date below, if you like
    sdate = str(input("What start date would you like for the search? [YYYY-MM-DD] Format: "))
    startdate = "start_date=" + sdate

    ## the value below is not being used in this
    ## version of the script
    #edate = str(input("What end date would you like for the search? [YYYY-MM-DD] Format: "))
    #enddate = "end_date=" + edate

    # make a request with the request library
    neowrequest = requests.get(NEOURL + startdate + "&" + nasacreds)

    # strip off json attachment from our response
    neodata = neowrequest.json()
    hazardous = 0
    asteroidList = []
    for date1 in neodata['near_earth_objects']:
        #print(date1)
        for asteroid in neodata['near_earth_objects'][date1]:
            #print(asteroid)
            if asteroid['is_potentially_hazardous_asteroid']:
                hazardous += 1
                asteroidList.append(['name: ' + asteroid['name'],['max diameter (miles): ' + str(asteroid['estimated_diameter']['miles']['estimated_diameter_max'])],['speed (MPH): ' + str(asteroid['close_approach_data'][0]['relative_velocity']['miles_per_hour'])],['miss distance (miles): ' + str(asteroid['close_approach_data'][0]['miss_distance']['miles'])]])

    ## display NASAs NEOW data
    #print(neodata['element_count'])
    print(f"Between the dates of {sdate} and 7 days later, there were {neodata['element_count']} near Earth objects")
    print(f"{hazardous} of them were potentially hazardous: ")
    for i in asteroidList:
        print(i)
        print()
if __name__ == "__main__":
    main()

