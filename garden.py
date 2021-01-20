from tree import Tree
from gnome import Gnome
from woodchuck import Woodchuck
import random

class Garden:
    def __init__(self, trees=[], gnomes=[], woodchucks=[], water_level=100, water_loss=10):
        self.trees = trees
        self.gnomes = gnomes
        self.woodchucks = woodchucks
        self.water_level = water_level
        self.water_loss = water_loss

    def chance_check(self, current_list):
        random_num = random.randint(1, 20)
        for i in len(range(current_list)):
            if i+1 == random_num:
                return True
        return False

    def get_tree(self):
        self.trees.append(Tree())

    def get_gnome(self):
        self.gnomes.append(Gnome())

    def get_woodchuck(self):
        if self.chance_check(self.woodchucks) == True:
            self.woodchucks.append(Woodchuck())

    def check_rain(self):
        if self.chance_check(self.gnomes) == True:
            return True
        else:
            return False
    
    def rain(self):
        self.water_level += 10
    
    def evaporate(self):
        shade = 2 * len(self.trees)
        self.water_level -= 10 - shade
    
    def kill_tree(self):
        if self.chance_check(self.woodchucks) == True:
            return True
        else:
            return False
