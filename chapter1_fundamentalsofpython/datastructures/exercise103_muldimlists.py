## Going over the lessons from Data structures subchapter
a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]


## This for loop iterates through the row in the table(list) a, and prints the first element (remember, python starts counting at 0)
#for row in a:
#    print(row[0])


#for row in a:
#    for element in row:
#        print(element)

## in this part, we will try to output diagonal elements from the table
## The output should therefore be 1, 5 and 9

#for i in range(3):
for i in range(len(a)): #Since a list can store sublists, the effective length is 3
    #print(a[i][i])
    ## We are effectivelly calling the first element in the first row, the second element in the second row and the third element in the final, third, row, indeed listing the diagonal elements.

    ##We comment out the print statement above, to implement string formating in the print statement.
    print(f'The {i + 1}-th diagonal element is: {a[i][i]}')