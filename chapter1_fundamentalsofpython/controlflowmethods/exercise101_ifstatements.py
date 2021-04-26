## Example to test if statements
#_______________________________________________________________________________

# we declare a variable
x = 130
y = 104832

# After running the script first, we can uncomment the line below and check the output for number 104832
## the output should be 'x is divisible by 6'
#x = y

# alternatively, we can try outputting to a log file, that we will call output.txt
# to do this, we use the 'with' keyword together with the 'open()' function

# we write an if statement to check if the variable is divisible by 5
if x % 5 == 0:  #check python operators if not sure what the modulo (%) operator does
    with open('output.txt', 'w') as f:
        f.write('x is divisible by 5')
    #print('x is divisible by 5')
# equally, we can continue writing additional conditions to check with the elif statement
elif x % 6 == 0:
    with open('output.txt', 'w') as f:
        f.write('x is divisible by 6')
    #print('x is divisible by 6')
elif x % 7 == 0:
    with open('output.txt', 'w') as f:
        f.write('x is divisible by 7')
    #print('x is divisible by 7')
# we write a final else statement to close the loop and set instructions if the variable does not satisfy any of the above conditions
else:
    with open('output.txt', 'w') as f:
        f.write('x is not divisible by either 5, 6 or 7')
    #print('x is not divisible by either 5, 6 or 7')


