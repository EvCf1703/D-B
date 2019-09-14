#Created by 'Angga Surya'. 

'''
===========================================

Enter any number to see its binary form.

==========================================='''

n = int('input'()) 
bin = "" 
temp = n 

while n>0:
    rem = n % 2
    bin+=str(rem) 
    n = n // 2
print("Binary Form Of",temp,"is",bin[::-1],"\n")
print("Thanks For Viewing My Code! ^^/n bye")
 
