# -*- coding: utf-8 -*-
GRAVITY = 9.8

def fallingDistance(time_of_fall):
        
    for time_of_fall in range(1, time_of_fall +1):
        distance_traveled_per_second = 0.5*GRAVITY*time_of_fall**2
        print("\t")
        print(time_of_fall,":(s)")
        print(distance_traveled_per_second)

def main():
    print("Hello,\nThis program will calcualte the speed of an object falling at earth gravity.")
    print ("How many seconds will the object be falling for?")
    time_of_fall = int(input("Second(s): "))
    fallingDistance(time_of_fall)
    
if __name__ == '__main__':
    main()