'''
For n = 3
  *
 ***
*****
'''


'''
Also For n = 5
    *
   ***
  *****
 *******
*********
'''

n = int(input("Enter the number: "))
for i in range(1 , n+1):
    print(" " * (n-i), end="")  # end is using because of no default space by print
    print("*" * (2*i-1), end="")
    print("")
    
