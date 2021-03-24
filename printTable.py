import numpy


tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

# [0][0]-----[1][0]--------[2][0]
# [0][1]-----[1][1]--------[2][1]
# [0][2]-----[1][2]--------[2][2]
# [0][3]-----[1][3]--------[2][3]

# print(len(tableData))
# print(len(tableData[0]))
# print(tableData[0][0])

colWidth=[]
lencurrentIndex=[]
lenWordsInCurrentIndex=[]

def printTable(tableData):
    # Convertion of list into the matrix and transpose
    a = numpy.array(tableData)
    Transpose_tableData = numpy.transpose(a)

    #Determining the longest word and using it as a .rjust()
    for Index,Items in enumerate(tableData):
        currentIndex=(tableData[Index])
        for x in currentIndex:
            lencurrentIndex.append(len(x))
        lencurrentIndex.sort()
        lencurrentIndex.reverse()
        colWidth.append(lencurrentIndex[0])
        lencurrentIndex.clear()

    #Printing matrix
    for x in range(len(Transpose_tableData)):
        # print(x)
        for y in range(len(Transpose_tableData[0])):
            print(Transpose_tableData[x][y].rjust(colWidth[-1]), end=' ') #[-1] because we aren't clearing the colWidth[]

        print('')

printTable(tableData)
