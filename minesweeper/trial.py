
cell = (7, 7)
surrounding_cells = []
for i in range(-1, 2, 1):
    for j in range(-1, 2, 1):
        print(f"i = {i}, j = {j}")
        if (i != 0 or j != 0) and 0 <= cell[0] + i < 8 and 0 <= cell[1] + j < 8:
            print(f"append")
            surrounding_cells.append((cell[0] + i, cell[1] + j))

print(surrounding_cells)
surrounding_cells.append()
print(surrounding_cells)
