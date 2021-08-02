#!/usr/bin/env python3
#create a list with three items
my_list = [ "192.168.0.5", 5060, "UP" ]
#display the first item
print("The first item in the list (IP): " + my_list[0])
#display the second item and convert to a string
print("The second item in the list (port): " + str(my_list[1]) )
#display the third item 
print("The last item in the list (state): " + my_list[2] )

iplist = [5060, "80", 55, "10.0.0.1","10.20.30.1","ssh"]


print(f"Display only the IP at position 3,4: {iplist[3]},  and  { iplist[4]}")
