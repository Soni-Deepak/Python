#[lists] are mutable and (tuples) are immutable

a = (1 ,2,3 ,4 ) #tuple
a = (1) #integer
a = (1,) #tuple
# a[0] = 345 tuple cannot be changed because it is immutable
print(type(a))