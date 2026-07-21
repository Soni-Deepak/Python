a = int(input("Enter your age :"))

#if statement no. 1
if(a%2 == 0):
    print("Number is even")
#End of if statement no. 1

#if statement no. 2
if(a>=18):
    print("You are above age of consent")  #the empty spce before print is indentation
    print("Good for you")

elif(a<0):
    print("You are entering an invalid negative age")

elif(a==0):
    print("You are entering 0 which is not a valid age")

else:
    print("You are below the age of consent")    
#End of if statement no. 2

print("End of the Program")