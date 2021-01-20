from tree import Tree
from garden import Garden
from gnome import Gnome
from woodchuck import Woodchuck
import random

garden = Garden()

def main():
    turn_counter = 0
    while len(garden.trees) <= 10 and garden.water_level > 0:
        print("taking a turn now")

        if "tree death chance eequals true kill tree":
            "kill tree"
        else:
            "nothing"

        if garden.check_rain() == True:
            garden.rain()
        else:
            garden.evaporate()
        
        if turn_counter % 10 == 0:
            chance = random.randint(1,2)
            if chance == 1:
                garden.get_gnome()
            else:
                garden.get_tree()
        turn_counter += 1