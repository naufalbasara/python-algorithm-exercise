def arithmetic_arranger(problems, show_result=False):
  answer = 0
  line1 = line2 = line3 = line4 = ""

  if len(problems) > 5:
    return "Error: Too many problems."
  
  for index, problem in enumerate(problems):
    num1, operator, num2 = problem.split()

    if not num1.isdigit() or not num2.isdigit():
      return "Error: Numbers must only contain digits."
    if int(num1) > 9999 or int(num2) > 9999:
      return 'Error: Numbers cannot be more than four digits.'
    if operator not in ['+', '-']:
      return "Error: Operator must be '+' or '-'."

    if show_result == True:
      if operator == '+':
        try:
          answer = int(num1) + int(num2)
        except:
          return "Error: Numbers must only contain digits."

      if operator == '-':
        try:
          answer = int(num1) - int(num2)
        except:
          return "Error: Numbers must only contain digits."
    
    space = max(len(str(num1)), len(str(num2)))
    if index ==0:
      line1 += f'{num1}'.rjust(space+2)
      line2 += operator + f'{num2}'.rjust(space + 1)
      line3 += '-' * (space+2)
      line4 += f'{answer}'.rjust(space + 2)
    else:
      line1 += f'{num1}'.rjust(space + 6)
      line2 += '    ' + operator + f'{num2}'.rjust(space + 1)
      line3 += '    ' + '-' * (space+2)
      line4 += f'{answer}'.rjust(space+6)

  if show_result == True:
    return line1 + '\n' + line2 + '\n' + line3 + '\n' + line4
  return line1 + '\n' + line2 + '\n' + line3