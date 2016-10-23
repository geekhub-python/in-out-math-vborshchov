#!/usr/bin/env python3

print("Input 4 number\n");

aa = int(input("distance between rows: "))
bb = int(input("distance between holes: "))
ii = int(input("spare lenght: "))
nn = int(input("holes quantity: "))
result = 2*(nn-1)*(aa+bb)+aa+2*ii

print("The lenght of shoelace is equals to %s " % result)