#!/usr/bin/env python3
# open file in read mode
with  open("dnsservers.txt", "r") as dnsfile:

# loop over lines
    for svr in dnsfile:
    #print and end without a newline
        svr = svr.rstrip('\n') 

        if svr.endswith('org'):
            with open("org-domain.txt", "a") as srvfile:
                    srvfile.write(svr + "\n")
        elif svr.endswith('com'):
            with open("com-domain.txt", "a") as srvfile:
                srvfile.write(svr + "\n")

