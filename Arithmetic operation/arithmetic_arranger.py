def arithmetic_arranger(problems, incl = False):
    if (len(problems) > 5):
        return ("Error: Too many problems.")

    operate = ["+", "-"]

    line1 = []
    line2 = []
    line3 = []
    line4 = []

    for var in problems:
      operator = var.split(" ")

      if operator[1] not in operate:
        return "Error: Operator must be '+' or '-'."

      value_1 = operator[0]
      value_2 = operator[2]

      if value_1.isdigit() == False or value_2.isdigit() == False:
        return "Error: Numbers must only contain digits."

      if len(value_1) > 4 or len(value_2) > 4:
        return "Error: Numbers cannot be more than four digits."

      fill_spaces = max(len(x) for x in operator)
      dash = "-"
      space = " "

      line1.append(value_1.rjust(fill_spaces + 2) + space * 4)
      line2.append(operator[1] + space + value_2.rjust(fill_spaces) + space*4)
      line3.append(dash * (fill_spaces +2) + space*4)
      addorsub = (str(eval(var)))
      line4.append(addorsub.rjust(fill_spaces + 2) + space*4)

    empty = ''
    line1 = empty.join(map(str, line1))
    line1 = line1.rstrip()
    line2 = empty.join(map(str, line2))
    line2= line2.rstrip()
    line3 = empty.join(map(str, line3))
    line3= line3.rstrip()
    line4 = empty.join(map(str, line4))
    line4= line4.rstrip()

    if incl == False:
      arranged_problems = line1 + "\n" + line2 + "\n" + line3
    if incl == True:
      arranged_problems = line1 + "\n" + line2 + "\n" + line3 + "\n" + line4
    print(arranged_problems)

    return arranged_problems