s1 = {"mango","banana"}
s2 = {"apple","orange","mango"}
s = s1 | s2 #union
s_intersection = s1 & s2 #intersection
s_diff = s1-s2  #difference
print(s)
print(s_intersection)
print(s_diff )  #s1 remaining elements will be printed bcs we did s1-s2
s1.add("Guava")#to add element in s1
print(s1)
#s2.remove("chicken") #remove operation if given element exits or else error
print(s2)
s2.discard("banana")
print(s2)