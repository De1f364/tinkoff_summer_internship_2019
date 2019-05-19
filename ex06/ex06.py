def right(i, j, matrix, pw):
	pw = pw + matrix[i][j + 1]
	return pw
def down(i, j, matrix, pw):
	pw = pw + matrix[i + 1][j]
	return pw

x, y = input().split()
x = int(x)
y = int(y)
i = 0
j = 0
lst_pw = []
pw = "a"
matrix = []
while i < x:
	line = input()
	matrix.append(line)
	i += 1
