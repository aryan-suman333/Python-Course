myDict = {
	"Fast" : "In a quick manner",
	"Harry" : "A Coder",
	"Marks" : [1, 2, 5],
	"another_dict" : {"harry" : "Player"}
}

print(myDict['Fast'])
print(myDict['Harry'])
print(myDict['Marks'])
print(myDict['another_dict'])
print(myDict['another_dict']['harry'])

myDict['Marks'] = [45,78] # dict k elements change kr skte h
print(myDict['Marks'])

# dictionary is unordered
# duplicate keys nhi daal skte(overwrite ho jaegi agar duplicate daalenge)