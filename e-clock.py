#!/usr/bin/env python3

print("Type a number\n");

minutes = int(input("minutes from begining of a day: "))

hours = int(int(minutes / 60) % 24)

minutes = minutes % 60

print("Time %s:%s shows e-clock" % (hours, minutes))