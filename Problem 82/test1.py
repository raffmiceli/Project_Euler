f = open('matrix.txt')
m = [map(int, line.strip().split(',')) for line in f]
f.close()

opt = [[row[0]] for row in m]
for col in range(1, len(m[0])):
    for row in range(len(m)):
        opt[row].append(m[row][col] + opt[row][col - 1])

    for row in range(1, len(m)):
        if opt[row - 1][col] + m[row][col] < opt[row][col]:
            opt[row][col] = opt[row - 1][col] + m[row][col]
    
    for row in reversed(range(len(m) - 1)):
        if opt[row + 1][col] + m[row][col] < opt[row][col]:
            opt[row][col] = opt[row + 1][col] + m[row][col]
    
print min(row[-1] for row in opt)
