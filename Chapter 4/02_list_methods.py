friends = ["apple" , "orange" , 5 , 4.332 , "false" , "Rohan"]
print(friends)

#IN STRING METHODS IT MAKE A NEW STRING AND DOES NOT CHANGE THE ORIGINAL BUT IN LIST IT CHANGE THE ORIGINAL 

friends.append("Harry")
print(friends)

l1 = [1 , 2 ,34 , 32 , 21]
# l1.sort() #in increasing order
# l1.reverse() #reverse 
l1.insert(3 , 3333) #insert the value 1st one is index and 2nd is the value
# l1.pop(2) #remove the number on given index and return its value
# print(l1.pop(4)) #return the pop value
value = l1.pop(2)
print(value) #sme return the pop value
print(l1)