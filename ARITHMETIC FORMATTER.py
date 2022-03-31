def arithmetic_arranger(problems , solve= False):
    
    # checks the number of problems passed into the function, return an error message if it's more than 5.
    if len(problems) > 5:
        return "Error: Too many problems."
    

    firstLine = ""
    secondLine = ""
    dashLines = ""
    resultLines = ""
    string_of_arithmetic = ""
    
    for problem in problems:
        firstNumber = problem.split(' ')[0]
        operator = problem.split(' ')[1]       
        secondNumber = problem.split(' ')[2]

        # checks to see if each number contains only digits, returns an error message if otherwise        
        if (firstNumber).isdigit() and (secondNumber).isdigit():
            

            # checks to see if the operator is / or *, returns an error message if that is the case            
            if operator == '/' or operator == '*':
                return "Error: Operator must be '+' or '-'."
        else:
            return "Error: Numbers must only contain digits."


        # returns an error message if the length of any of the numbers is greater than 4        
        if len(firstNumber) > 4 or len(secondNumber) > 4:
            return "Error: Numbers cannot be more than four digits."

        operation = ''
        
        if operator == '+':
            operation = str(int(firstNumber) + int(secondNumber))
            
        elif operator == '-':
            operation = str(int(firstNumber) - int(secondNumber))
            

        length = max(len(firstNumber) , len(secondNumber)) + 2
        top = str(firstNumber).rjust(length)
        bottom = operator + str(secondNumber).rjust(length - 1)
        line = ''
        

        result = str(operation).rjust(length)
        for i in range(length):
            line += '-'

        if problem != problems[-1]:
            firstLine += top + '    '
            secondLine += bottom + '    '
            dashLines += line + '    '
            resultLines += result + '    '
            

    if solve:
        string_of_arithmetic = firstLine + '\n' + secondLine + '\n' + dashLines + '\n' + resultLines

    else:
        string_of_arithmetic = firstLine + '\n' + secondLine + '\n' + dashLines

    return string_of_arithmetic


