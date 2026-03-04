#pattern 1:Import the whole module
import math
#now use:math.sqrt(16)

#pattern 2:import specific items from a module
from math import sqrt,pi

#now use:sqrt(16) and pi

import random

number=random.randint(1,10)
choice=random.choice(['apple','banana','cherry'])
print(number)
print(choice)   
