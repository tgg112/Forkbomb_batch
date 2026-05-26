import time
import os

instances = 1
os.system("title malware visualiser")
input("this shows how fast the forkbomb increase in size, and is not harmful, continue? ")

while True:
    print(f"There are {instances} tabs open")
    instances *= 2  # Double the number of instances
