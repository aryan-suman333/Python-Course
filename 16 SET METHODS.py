a = set()

a.add(4)
a.add(5)
a.add(5) # 5 vps add nhi hoga as no repetetive element
a.add((2, 3, 5)) # tuple ko add kr skte h sets m

# a.add([2, 3, 5]) set m list add nhi kr skte
# a.add({2 : 3}) set m dict add nhi kr skte

print(a)
print(len(a))

a.remove(5)
print(a)

print(a.pop()) # koi bhi element pop kr dega or usko return kr dega

a.clear() # empty kr dega set ko
print(a)

b = {1, 3 , 5}

print(b.union({1, 2, 3, 4}))
print(b.intersection({1, 2, 3, 4}))