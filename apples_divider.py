#!/usr/bin/env python3

print("Input 2 number - \n");

pupils = int(input("pupils quantity: "))
apples = int(input("apples quantity: "))
get_each_pupil = int(pupils / apples)
remainder = pupils % apples

print("\n");
print("%s apples get each pupil " % get_each_pupil);
print("%s apples remain" % remainder);
