f = open('sample.txt', 'r') # pehle file name phir mode(r mtlb read mode)
data = f.read()
print(data)
f.close()

# by default mode is r
# w for write mode
# a for append mode
# + for updating(read + write) mode
# f.read(5) read upto 5 characters
# f.readline() sirf 1 line read krega vps readline krenge to next line read krega

f = open('sample.txt', 'w')
f.write("Please write this to file")
f.close()

# with open('sample.txt', 'r') as f:
# 	a = f.read()
# print(a)
# with open('sample.txt', 'w') as f:
# 	a = f.write("Hello")

# with se open krne p close krne ki jarurat nhi