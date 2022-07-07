l = ["Camera", "Phone", "Laptop", "Mic", "Tripod", "Bag"]

sentence = " and ".join(l) # join sirf strings k saath kaam krega
print(sentence)
print(type(sentence))

# tuple m bhi kaam krega

name = "Harry"
channel = "CodewithHarry"

a = "This is {} and his channel is {}".format(name, channel)
print(a)

a = "This is {1} and his {2} channel is {0}".format(channel, name, "coding")
print(a)
# fstrings jesa hi h