story = '''once upon a time there was a youtuber named Harry who uploaded python 
course with notes'''

print(len(story))
print(story.endswith("dfb")) # bool return krega, string dfb se end ho rhi h ya nhi
print(story.endswith("notes"))
print(story.count("a")) # count krega kitne 'a' h string m
print(story.count("th"))
print(story.capitalize()) # string k 1st letter ko capital kr deta h
print(story.find("Harry")) # index return krega jaha p harry present h, nhi hoga to -1
print(story.replace("Harry", "Aryan")) # jaha jaha harry hoga sbko replace krega

story = "Harry is good.\nHe\t is very good\\"
print(story)

line = "	Harry is good		"
print(line)
print(line.strip())

if 'harry' in story.lower(): # string in lowercase
	print("Yes")