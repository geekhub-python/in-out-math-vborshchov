#!/usr/bin/env python3

print("Input 3 number\n");

pupils1 = int(input("pupils quantity of class 1: "))
pupils2 = int(input("pupils quantity of class 2: "))
pupils3 = int(input("pupils quantity of class 3: "))

descs1 = ((pupils1 +1) >> 1) << 1
descs2 = ((pupils2 +1) >> 1) << 1
descs3 = ((pupils3 +1) >> 1) << 1
sum = (descs1 + descs2 + descs3) // 2

print ("%s" % sum)