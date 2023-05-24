length, height = 20,20

cols = []
for i in range(length):
    col = []
    for j in range(height):
        col.append((i, j))
    cols.append(col)

rows = []
for j in range(height):
    row = []
    for i in range(length):
        row.append((i, j))
    rows.append(row)

diagonals = []
for i in range(-height+1, height):
    diag = []
    for j in range(length):
        if 0 <= j+i < height:
            diag.append((j, j+i))
    diagonals.append(diag)

r_diagonals = []
for i in range(-height+1, height):
    diag = []
    for j in range(length):
        if 0 <= j+i < height:
            diag.append((length-j-1, j+i))
    r_diagonals.append(diag[::-1])

print(cols)
print()
print(rows)
print()
print(diagonals)
print()
print(r_diagonals)
print()