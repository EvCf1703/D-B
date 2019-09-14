#Created by 'Angga Surya'. 

def banner():
   print("\033[93m\t\t\t
===========================================

Enter any number to see its binary form.

===========================================
")








print('\n\033[93m\t\t\tEnter your num:\n')
n = int(input()) 
bin = "" 
temp = n 

while n>0:
    rem = n % 2
    bin+=str(rem) 
    n = n // 2
print("Binary Form Of",temp,"is",bin[::-1],"\n")
print("Thanks For Viewing My Code! ^^\n")
print("bye")
 
