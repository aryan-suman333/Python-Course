a = 'aryan"s'
b = "aryan's"
c = '''aryan"s and aryan's'''

print(a)
print(b)
print(c)

d = '''my name
is aryan'''

e = '''my name
	   is aryan'''
	   
print(d)
print(e)

greeting = "Good morning, "
name = "Aryan"
print(greeting + name)

new_str = greeting + name
print(new_str)

print(new_str[0])
print(new_str[1])
print(new_str[2])
print(new_str[3])

print(name[0:4]) # isme 4 not include h 0:5 likhne p pura aryan print hoga
                 # 1:3 m 1 include hoga 3 nhi,aage waala hoga piche waala nhi
print(name[:4])  # left khali chhodne prr sabse minimum waala daal dega mtlb 0
print(name[0:])  # right khali chhodne prr sabse maximum waala daal dega mtlb 5

print(name[-1])  # -2 length-2 waala dega,-3 length-3 waala 
print(name[-4:-1]) # this will print rya as -1 not included

print(new_str[0::1]) # this will print Good morning, Aryan
print(new_str[0::2]) # but this will print Go onn,Ayn as 1 character skip ho ho kr aaega
print(new_str[0::3]) # but this will print Gdoi,rn as 2 character skip ho ho kr aaega