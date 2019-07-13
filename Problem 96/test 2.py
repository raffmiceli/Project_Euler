solved = lambda l: not 0 in l

row_iter = lambda i: xrange(9 * (i / 9), 9 * (i / 9) + 9)
col_iter = lambda i: xrange(i % 9, 81, 9)
def block_iter(i):
    start = 27 * (i / 27) + 3 * ((i % 9) / 3)
    for j in range(3):
        for k in range(3):
            yield start + j * 9 + k

# returns the set of possible values for element j in partially completed
# sudoku puzzle a
def options(a, j):
    opts = set(range(1, 10))
    opts -= set([a[k] for k in row_iter(j)])
    opts -= set([a[k] for k in col_iter(j)])
    opts -= set([a[k] for k in block_iter(j)])
    return opts
    

f = open("sudoku old.txt", 'r')
nums = set(range(1, 10))
tot = 0
for i in range(50):
    a = []
    f.readline() # garbage line
    for j in range(9):
        a.extend([int(x) for x in f.readline().split()[0]])

    stack = []
    while not solved(a):
        # sort indices by value first (so only zeros will be chosen),
        # then by the number of choices at each index
        l = []
        for j in range(len(a)):
            l.append((a[j], len(options(a, j)), j))
        l.sort()

        # extract best unfilled index
        j = l[0][2]
        opts = options(a, j)

        # pop the stack until we have some choices
        while len(opts) == 0:
            a[j] = 0
            j, opts = stack[-1]
            del stack[-1]

        # make a choice, push it onto the stack with remaining options
        choice = opts.pop()
        a[j] = choice
        stack.append((j, opts))
        
    tot += 100 * a[0] + 10 * a[1] + a[2]
print tot
