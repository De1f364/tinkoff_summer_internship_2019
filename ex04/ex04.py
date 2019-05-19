num = int(input())
dlt = 3
if num % 2 == 0:
	print(2)
else:
	while dlt <= int(pow(num, .5)):
		if num % dlt != 0:
			dlt += 2
		else:
			print(dlt)
			break;
	if num % dlt != 0:
		print(num)