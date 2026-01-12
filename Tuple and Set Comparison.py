#Create a list of elements and convert it into both a tuple and a set.
a = ["apple","banana",24,True]
b = tuple(a)
c = set(a)
c.add("guava")
print(b) #Print both the tuple and the set.
print(c) 
#Try to add new elements to the tuple and set= not possible to add in tuple bcs it is immutable if any changes needed directly we need to assign values