#!/usr/bin/env python3
import argparse
import time
import requests
import hashlib

## Define the API here
XAVIER = 'http://gateway.marvel.com/v1/public/characters'

## Calculate a hash to pass through to our MARVEL API call
## Marvel API wants md5 calc md5(ts+privateKey+publicKey)
def hashbuilder(timeywimey, pvkee, pubkee):
    return hashlib.md5((timeywimey+pvkee+pubkee).encode('utf-8')).hexdigest()

## Perform a call to MARVEL Character API
## http://gateway.marvel.com/v1/public/characters
## ?name=Spider-Man&ts=1&apikey=1234&hash=ffd275c5130566a2916217b101f26150
def marvelcharcall(stampystamp, hashyhash, pkeyz, lookmeup, theMedia):
    r = requests.get(XAVIER+"?name="+lookmeup+"&ts="+stampystamp+"&apikey="+pkeyz+"&hash="+hashyhash).json()['data']['results'][0]

    #print(XAVIER+"?name="+lookmeup+"&ts="+stampystamp+"&apikey="+pkeyz+"&hash="+hashyhash)
    print(f"~~~~~~~~~~~~~~~ {r['name']} ~~~~~~~~~~~~~~~")
    print(r['description'])
    theData = []
    if theMedia == 'comics':
        print(f"There are {r['comics']['available']} comics that include {lookmeup}! Here are the first 20: ")
        for comics in r['comics']['items']:
            theData.append(comics['name'])
    elif theMedia == 'series':
        print(f"There are {r['series']['available']} series that include {lookmeup}! Here are the first 20: ")
        for series in r['series']['items']:
            theData.append(series['name'])
    elif theMedia == 'stories':
        print(f"There are {r['stories']['available']} stories that include {lookmeup}! Here are the first 20: ")
        for stories in r['stories']['items']:
            theData.append(stories['name'])
    elif theMedia == 'events':
        print(f"There are {r['events']['available']} events that include {lookmeup}! Here are the first 20: ")
        for events in r['events']['items']:
            theData.append(events['name'])
    for media in theData:
        print(media)
    
def main():           
    
    ## harvest private key
    with open(args.dev) as mccoy:
        beast = mccoy.read().rstrip('\n')
    
    ## harvest public key
    with open(args.pub) as munroe:
        storm = munroe.read().rstrip('\n')
    
    ## create an integer from a float timestamp (for our RAND)
    nightcrawler = str(time.time()).rstrip('.')
    
    ## build hash with hashbuilder(timestamp, privatekey, publickey)
    cerebro = hashbuilder(nightcrawler, beast, storm)

    ## call the API with marvelcharcall(timestamp, hash, publickey, character)
    uncannyxmen = marvelcharcall(nightcrawler, cerebro, storm, args.hero, args.media)
    
    ## display results
    #print(uncannyxmen)

## Define arguments to collect
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--dev', help='Provide the /path/to/file.priv \
      containing Marvel private developer key')
    parser.add_argument('--pub', help='Provide the /path/to/file.pub \
      containing Marvel public developer key')
    
    ## The line below is NEW! This allows us to pass the lookup character
    parser.add_argument('--hero', \
      help='Character to search for within the Marvel universe')
    parser.add_argument('--media', \
      choices = ['comics', 'series', 'stories', 'events'], \
      default= 'comics', \
      help='What type of information you want returned from [comics, series, stories, events]')
    args = parser.parse_args()
    main()

