d = {} #Empty dictionary

marks = {
    "Harry" : 100,
    "Rohan" : 56,
    "shubham" : 89,
    0 : "Harry",
}

# print(marks.items()) #gives key value pair list of items
# print(marks.keys())
# print(marks.values())
# marks.update({"Harry" : 99 , "Renuka" : 78}) #Dict are mutable it can chaange or update the key value pair
# print(marks)


print(marks.get("Harry2")) #Prints None
print(marks["Harry2"]) #Returns an Error