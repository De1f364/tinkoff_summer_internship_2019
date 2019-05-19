x, y = input().split()
i = 1
x = float(x)
y = float(y)
summ = x
while summ < y and x > 0 and y <= 1000:
	x = x * 1.7
	summ += x
	i += 1
print(i)