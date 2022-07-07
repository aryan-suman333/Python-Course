while(True):
	print("Press q to quit")
	a = input('Enter a number: ')
	if a == 'q':
		break
	try:
		a = int(a) # yaha p value error aaega, isliye yaha se direct except waali line p chla jaega
		if a > 6:
			print(a, 'is greater than 6')
		c = 1/a # yaha p zero division error aaega, isliye yaha se direct except waali line p chla jaega
		print('c =', c)

	except ValueError as e:
		print("Exception 1 occured")
		print(f"Invalid input: {e}")

	except ZeroDivisionError as e:
		print("Exception 2 occured")
		print(f"Invalid input: {e}")

	except Exception as e:
		print(f"Invalid input: {e}") # any other error

	else:
		print("Thanks for using") # koi exception nhi hua to else run hoga

	finally:
		print("Code is perfect") # ye run krega hi, pehle khi break hua tb bhi chlega