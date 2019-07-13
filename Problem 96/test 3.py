def solve(sudoku):
    mask = [0,1,2,9,10,11,18,19,20]
    def getSet(i):
        s, row, col = set(), int(i/9), i%9
        corner = (int(row/3)*27) + (int(col/3)*3)
        for i in range(9):
            for j in [row*9+i, col+i*9, corner + mask[i]]:
                s.add(sudoku[j])
        return set("123456789") - s
    try:
        i = sudoku.index("0")
        for value in getSet(i):
            result = solve(sudoku.replace("0",value,1))
            if result: return result
    except:
        return sudoku
    return False

def problem096():
    t, i, s = 0, 0, ""
    for line in open('sudoku old.txt').readlines():    
        if len(line) > 8:
            s += line[:9]
        if i == 9:
            t += int(solve(s)[:3])
            i, s = 0, ""
        else: i += 1
    return t
    
print problem096()
