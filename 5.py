#lists
item1="apple"
item2="banana"
item3="cherry"

items=["apple","banana","cherry","laddu","apple2"]

print(item1,item2,item3)
print(items)
print(items[0])
print(items[-1])
items.pop()
print(items)
items.pop(1)
print(items)
items.append("mango")
print(items)
items.remove("apple")
print(items)
items.insert(0,"apple")
print(items)
items.clear()
print(items)

items=["apple","banana","cherry","laddu","apple2"]

items[0]="orange"
print(items)
print(sorted(items))
print(items.index("banana"))
items.reverse()
print(items)


matrix=[[1,2,3],[4,5,6],[7,8,9]]
print(matrix[0])
print(matrix[1][2])