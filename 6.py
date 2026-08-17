#tuples
my_tuple=("x1","x2","x3")
print(my_tuple)
print(len(my_tuple))
print(my_tuple[0])
#my_tuple[0]="x1 0.2"   #'tuple' object does not support item assignment
tuple1=(2,4,6)
tuple2=(1,1,1)
print(tuple1+tuple2)
print(tuple2*3)
print(my_tuple.count("x1"))
print(my_tuple.index("x2"))
print(type(tuple1))

#sets
my_sets=("apple","banana","cherry")
print(my_sets)
s={12,34,90,45,67,89}    #sets is unordered and unindexed
print(s)
print(len(s))   
print(type(s))