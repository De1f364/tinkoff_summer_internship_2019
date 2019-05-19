pw = input()
smb = 0
low = []
up = []
num = []
for i in pw:
	smb += 1
	if 48 <= ord(i) <= 57:
		num.append(i)
	elif 97 <= ord(i) <= 122:
		low.append(i)
	elif 65 <= ord(i) <= 90:
		up.append(i)
if not num or not low or not up or smb < 8:
	print('NO')
else:
	print('YES')
print(smb)
print(num)
print(low)
print(up)
