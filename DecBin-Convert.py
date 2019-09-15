#Created by 'Angga Surya'. 

import time

def banner():
  
print("===========================================")

print("Enter any number to see its binary form.")

print("===========================================")









print('\nEnter your num:\n')
print("=================================")
time.sleep(1)
n = int(input()) 
bin = "" 
temp = n 

while n>0:
    rem = n % 2
    bin+=str(rem) 
    n = n // 2
print("Binary Form Of",temp,"is",bin[::-1],"\n")
time.sleep(0.5)
print("Thanks For Viewing My Code! ^^\n")
time.sleep(1)
print("bye")
 
