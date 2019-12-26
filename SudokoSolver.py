#Works perfectly fine and extremly fast and efficient with Sudokos
# with single answers, it also shows where duplicates happen so it can be fixed later
#Still in progress so it can generate one with is as well

import time
from random import randint, shuffle

original = []
original.append([8, 0, 0, 7, 1, 0, 0, 0, 0])
original.append([3, 2, 7, 0, 0, 0, 0, 0, 0])
original.append([0, 0, 1, 0, 2, 9, 8, 7, 6])
original.append([6, 5, 0, 0, 0, 0, 0, 0, 0])
original.append([0, 0, 0, 5, 9, 0, 0, 8, 2])
original.append([7, 8, 2, 0, 3, 6, 0, 1, 0])
original.append([9, 0, 5, 2, 6, 4, 7, 3, 0])
original.append([0, 0, 0, 0, 0, 1, 2, 6, 9])
original.append([0, 0, 0, 0, 0, 3, 1, 5, 4])
""" original = []
original.append([3, 0, 6, 5, 0, 8, 4, 0, 2])
original.append([5, 2, 0, 0, 0, 0, 0, 0, 8])
original.append([0, 8, 7, 0, 0, 0, 0, 3, 1])
original.append([0, 0, 3, 0, 1, 0, 0, 8, 0])
original.append([9, 0, 0, 8, 6, 3, 0, 0, 5])
original.append([0, 5, 0, 0, 9, 0, 6, 0, 0])
original.append([1, 3, 0, 0, 0, 0, 2, 5, 0])
original.append([0, 0, 0, 0, 0, 0, 0, 7, 4])
original.append([0, 0, 5, 2, 0, 6, 3, 0, 0]) """


""" original = []
original.append([0, 0, 3, 0, 7, 0, 0, 0, 5])
original.append([0, 0, 0, 5, 0, 4, 9, 8, 7])
original.append([0, 0, 0, 0, 0, 0, 2, 0, 0])
original.append([2, 0, 4, 0, 0, 0, 0, 0, 0])
original.append([0, 6, 7, 0, 5, 0, 0, 0, 8])
original.append([3, 1, 0, 0, 0, 0, 0, 6, 0])
original.append([0, 0, 1, 8, 4, 0, 0, 5, 0])
original.append([0, 0, 0, 2, 0, 1, 0, 4, 0])
original.append([0, 7, 0, 0, 0, 0, 0, 0, 0]) """
""" original = []
original.append([0, 0, 0, 0, 0, 0, 0, 0, 0])
original.append([0, 0, 0, 0, 0, 0, 0, 0, 0])
original.append([0, 0, 0, 0, 0, 0, 0, 0, 0])
original.append([0, 0, 0, 0, 0, 0, 0, 0, 0])
original.append([0, 0, 0, 0, 0, 0, 0, 0, 0])
original.append([0, 0, 0, 0, 0, 0, 0, 0, 0])
original.append([0, 0, 0, 0, 0, 0, 0, 0, 0])
original.append([0, 0, 0, 0, 0, 0, 0, 0, 0])
original.append([0, 0, 0, 0, 0, 0, 0, 0, 0]) """

""" original[0][0] = 5
original[1][0] = 1
original[2][0] = 2
original[0][1] = 6
original[0][2] = 3
original[1][2] = 7
original[1][1] = 9
original[2][1] = 8
original[2][2] = 4 """

checker = original

def SudoSolver():
    count = 0
    startTime = time.time()

    def finisher(tbl):
        if count > 1000:
            print("Sudoko Does not have a single answer")
            print("You can find the duplicates bellow: ")
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
            #repeaterBr = 0
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
    
SudoSolver()

rowList = [i for i in range(1, 10)]

def FullSudokoTable():
    #firstRow = [i for i in range(1, 10)]
    #shuffle(firstRow)
    #original[0] = firstRow
    rowList = [i for i in range(1, 10)]
    i = 0
    row = 0
    column = 0
    attempt = 0
    shuffle(rowList)
    while i < 81:
        if original[row][column] != 0:
            i += 1
        row = int(i / 9)
        column = i % 9
        
        original[row][column] = randint(1,9)
        for j in range(0, 9):
            if original[row][column] == original[j][column] and row != j:
                original[row][column] = 0
                break
            if original[row][column] == original[row][j] and column != j:
                original[row][column] = 0
                attempt += 1
                break
        if row < 3:
            if column < 3:
                for r in range(0, 3):
                    for c in range(0, 3):
                        if original[row][column] == original[r][c] and r != row and c != column:
                            original[row][column] = 0
                            attempt += 1
                            break
            elif column < 6:
                for r in range(0, 3):
                    for c in range(3, 6):
                        if original[row][column] == original[r][c] and r != row and c != column:
                            original[row][column] = 0
                            attempt += 1
                            break
            else:
                for r in range(0, 3):
                    for c in range(6,9):
                        if original[row][column] == original[r][c] and r != row and c != column:
                            original[row][column] = 0
                            attempt += 1
                            break
        elif row < 6:
            if column < 3:
                for r in range(3, 6):
                    for c in range(0, 3):
                        if original[row][column] == original[r][c] and r != row and c != column:
                            original[row][column] = 0
                            attempt += 1
                            break
            elif column < 6:
                for r in range(3, 6):
                    for c in range(3, 6):
                        if original[row][column] == original[r][c] and r != row and c != column:
                            original[row][column] = 0
                            attempt += 1
                            break
            else:
                for r in range(3, 6):
                    for c in range(6,9):
                        if original[row][column] == original[r][c] and r != row and c != column:
                            original[row][column] = 0
                            attempt += 1
                            break
        else:
            if column < 3:
                for r in range(6, 9):
                    for c in range(0, 3):
                        if original[row][column] == original[r][c] and r != row and c != column:
                            original[row][column] = 0
                            attempt += 1
                            break
            elif column < 6:
                for r in range(6, 9):
                    for c in range(3, 6):
                        if original[row][column] == original[r][c] and r != row and c != column:
                            original[row][column] = 0
                            attempt += 1
                            break
            else:
                for r in range(6, 9):
                    for c in range(6,9):
                        if original[row][column] == original[r][c] and r != row and c != column:
                            original[row][column] = 0
                            attempt += 1
                            break
    rowList = rowList - original[row][column]
    attempt += 1
    for line in original:
        print(line)

#FullSudokoTable()