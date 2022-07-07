num = int(input("Enter the number\n"))

for i in range(10):
	print(f"{num}x{i} = {num*i}")

# " iske pehle ek f likhdo or phir jaha jaha variable likhne h waha {} lgaado or baaki
# direct likho

l = ['Harry', 'Aryan', 'Shubham', 'Swati']

for name in l:
    if name.startswith("S"):
    	print(f"Hello {name}")