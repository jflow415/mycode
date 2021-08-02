#!/usr/bin/env python3
import random
#create our first list
icecream= ["flavors", "salty"]

#create our second list of names
tlgclass= ["Adrian","Bikash","Chas","Chathula","Chris","Hongyi","Jauric","Joe L.","Joe V.","Josh","Justin","Karlo","Kerri-Leigh","Jason","Nicholas","Peng","Philippe","Pierre","Stephen","Yun"]

#append the integer 99 to the list of icecream
icecream.append(99)
# ask for user input
number = input("Choose a number between 0 and 19.")

print(icecream[2], icecream[0], "and ", tlgclass[int(number)], " chooses to be ", icecream[1])
print(icecream[2], icecream[0], "and ", random.choice(tlgclass), "chooses to be ", icecream[1])
