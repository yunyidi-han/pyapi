#!/usr/bin/env python3
import argparse
heros=  {"flash":{"speed": "fastest", "intelligence": "lowest", "strength": "lowest"}, "batman":{"speed": "slowest", "intelligence": "highest", "strength": "money"}, "superman":{"speed": "fast", "intelligence": "average", "strength": "strongest"}}

def printHero(heroInput,statInput):
    print(f'{heroInput.capitalize()}\'s {statInput} is: {str(heros[heroInput][statInput])}')

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Find a superhero's stats")
    parser.add_argument('-hero', choices=heros.keys(), metavar='HERO', default='flash', help='Pick a hero from [flash, batman, superman]')
    parser.add_argument('-s', choices=heros['flash'].keys() ,metavar='STAT', default='speed',
                        help='Pick a stat from [speed, intelligence, strength]')

args = parser.parse_args()
#print(args)
#print(args.hero)
printHero(args.hero,args.s)
