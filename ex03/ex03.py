n = int(input())
i = 0
j = 0
lst_x = []
lst_y = []
diff_x = []
diff_y = []
if n < 3:
	print('NO')
while i < n:
	x, y = input().split()
	lst_x.append(int(x))
	lst_y.append(int(y))
	i += 1
while j < n - 1:
	diff_x.append(abs(lst_x[j] - lst_x[j + 1]))
	diff_y.append(abs(lst_y[j] - lst_y[j + 1]))
	j += 1
if sum(lst_x) / n == lst_x[0] and sum(lst_x) % n == 0:
	print('NO')
elif sum(lst_y) / n == lst_y[0] and sum(lst_y) % n == 0:
	print('NO')
elif diff_x == diff_y:
	print('NO')
else:
	print('YES')