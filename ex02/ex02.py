m = int(input())
i = 2
j = 2
rems = []
rems2 = []
n = 2
while i <= m <= 40:
	rem = int(input())
	rems.append(rem)
	i += 1
print(rems)
while rems2 != rems:
	while j <= m <= 40:
		rems2.append(n % j)
		j += 1
	if rems2 != rems:
		n += 1
		rems2 = []
		j = 2
print(n)