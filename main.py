import re

with open('input.txt', 'r') as numbers:
    for inputNum in numbers:
        inputNum = numbers.readline()
        if re.match(r'^(\+7|8)?[-( ]?9\d{2}[-) ]?\d{3}[- ]?\d{2}[- ]?\d{2}$', inputNum):
            with open('output.txt', 'a') as result:
                result.write(inputNum)
