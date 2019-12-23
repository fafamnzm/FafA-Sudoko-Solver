import time

""" original = []
original.append([8, 0, 0, 7, 1, 0, 0, 0, 0])
original.append([3, 2, 7, 0, 0, 0, 0, 0, 0])
original.append([0, 0, 1, 0, 2, 9, 8, 7, 6])
original.append([6, 5, 0, 0, 0, 0, 0, 0, 0])
original.append([0, 0, 0, 5, 9, 0, 0, 8, 2])
original.append([7, 8, 2, 0, 3, 6, 0, 1, 0])
original.append([9, 0, 5, 2, 6, 4, 7, 3, 0])
original.append([0, 0, 0, 0, 0, 1, 2, 6, 9])
original.append([0, 0, 0, 0, 0, 3, 1, 5, 4]) """
""" original = []
original.append([3, 0, 6, 5, 0, 8, 4, 0, 0])
original.append([5, 2, 0, 0, 0, 0, 0, 0, 0])
original.append([0, 8, 7, 0, 0, 0, 0, 3, 1])
original.append([0, 0, 3, 0, 1, 0, 0, 8, 0])
original.append([9, 0, 0, 8, 6, 3, 0, 0, 5])
original.append([0, 5, 0, 0, 9, 0, 6, 0, 0])
original.append([1, 3, 0, 0, 0, 0, 2, 5, 0])
original.append([0, 0, 0, 0, 0, 0, 0, 7, 4])
original.append([0, 0, 5, 2, 0, 6, 3, 0, 0])
 """
""" checker = []
checker.append([8, 0, 0, 7, 1, 0, 0, 0, 0])
checker.append([3, 2, 7, 0, 0, 0, 0, 0, 0])
checker.append([0, 0, 1, 0, 2, 9, 8, 7, 6])
checker.append([6, 5, 0, 0, 0, 0, 0, 0, 0])
checker.append([0, 0, 0, 5, 9, 0, 0, 8, 2])
checker.append([7, 8, 2, 0, 3, 6, 0, 1, 0])
checker.append([9, 0, 5, 2, 6, 4, 7, 3, 0])
checker.append([0, 0, 0, 0, 0, 1, 2, 6, 9])
checker.append([0, 0, 0, 0, 0, 3, 1, 5, 4]) """
original = []
original.append([0, 0, 3, 0, 7, 0, 0, 0, 5])
original.append([0, 0, 0, 5, 0, 4, 9, 8, 7])
original.append([0, 0, 0, 0, 0, 0, 2, 0, 0])
original.append([2, 0, 4, 0, 0, 0, 0, 0, 0])
original.append([0, 6, 7, 0, 5, 0, 0, 0, 8])
original.append([3, 1, 0, 0, 0, 0, 0, 6, 0])
original.append([0, 0, 1, 8, 4, 0, 0, 5, 0])
original.append([0, 0, 0, 2, 0, 1, 0, 4, 0])
original.append([0, 7, 0, 0, 0, 0, 0, 0, 0])


checker = original

count = 0
startTime = time.time()

def finisher(tbl):
    if count > 5000:
        return False
    
    for row in range(9):
        for col in range(9):
            if tbl[row][col] == 0 or type(tbl[row][col]) == set:
                return True

    return False

for row in range(9):
    for col in range(9):
        if checker[row][col] == 0:
            checker[row][col] = set(range(1,10))

while finisher(checker):    
    for i in range(0, 81):
        repeaterBr = 0
        row = int( i / 9)
        column = i % 9
        if type(original[row][column]) == set:
            #original[row][column] = set([original[row][column]])
            count += 1
            
            for j in range(0, 9):
                if type(checker[row][j]) != set:
                    checker[row][column] = checker[row][column] - set([checker[row][j]])
                if type(checker[j][column]) != set:
                    checker[row][column] = checker[row][column] - set([checker[j][column]])
            if row < 3:
                if column < 3:
                    for r in range(0, 3):
                        for c in range(0,3):
                            if type(checker[r][c]) != set:
                                checker[row][column] = checker[row][column] - set([checker[r][c]])                            
                elif column < 6:
                    for r in range(0, 3):
                        for c in range(3, 6):
                            if type(checker[r][c]) != set:
                                checker[row][column] = checker[row][column] - set([checker[r][c]])
                else:
                    for r in range(0, 3):
                        for c in range(6, 9):
                            if type(checker[r][c]) != set:
                                checker[row][column] = checker[row][column] - set([checker[r][c]])
            elif row < 6:
                if column < 3:
                    for r in range(3, 6):
                        for c in range(0,3):
                            if type(checker[r][c]) != set:
                                checker[row][column] = checker[row][column] - set([checker[r][c]])
                elif column < 6:
                    for r in range(3, 6):
                        for c in range(3, 6):
                            if type(checker[r][c]) != set:
                                checker[row][column] = checker[row][column] - set([checker[r][c]])
                else:
                    for r in range(3, 6):
                        for c in range(6, 9):
                            if type(checker[r][c]) != set:
                                checker[row][column] = checker[row][column] - set([checker[r][c]])
            else:
                if column < 3:
                    for r in range(6, 9):
                        for c in range(0,3):
                            if type(checker[r][c]) != set:
                                checker[row][column] = checker[row][column] - set([checker[r][c]])
                elif column < 6:
                    for r in range(6, 9):
                        for c in range(3, 6):
                            if type(checker[r][c]) != set:
                                checker[row][column] = checker[row][column] - set([checker[r][c]])
                else:
                    for r in range(6, 9):
                        for c in range(6, 9):
                            if type(checker[r][c]) != set:
                                checker[row][column] = checker[row][column] - set([checker[r][c]])
            
            if len(checker[row][column]) == 1 :
                original[row][column] = int(list( checker[row][column] )[0])
#    print(original)
endTime = time.time()

for line in checker:
    print(line)

print()
print("No. Count = %d" %count)
print()
print("Elapsed Time = {} Seconds".format(endTime - startTime))
print()