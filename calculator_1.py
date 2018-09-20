
def promptUserForInput():
  while True:
      try:
          number_1 = float(input("Enter first number: "))
      except ValueError:
          print("********* Please enter a number. **********")
          number_1 = float(input("Enter first number: "))
      try:
          operand = input("Enter operand (+,-,*,/): ")
          while operand not in ["+", "-", "*", "/"]:
            print("********* Please enter an operand. **********")
            operand = input("Enter operand (+,-,*,/): ")
      except ValueError:
          print("********* Please enter an operand. **********")

      try:
          number_2 = float(input("Enter second number: "))
      except ValueError:
          print("********* Please enter a number. **********")
          number_2 = float(input("Enter second number: "))

      return (number_1, operand, number_2)


def total(number_1, operand, number_2):
    if operand == "+":
        result = number_1 + number_2
    elif operand == "-":
        result = number_1 - number_2
    elif operand == "*":
        result = number_1 * number_2
    elif operand == "/":
        result = number_1 / number_2
    return result

def display_result(number_1, operand, number_2, result):
    print()
    print("**********************")
    print("{0} {1} {2} = {3}".format(number_1,operand,number_2,result))
    print("**********************")
    print()

(number_1,operand,number_2) = promptUserForInput()
result = total(number_1, operand, number_2)
display_result(number_1, operand, number_2, result)

while True:
  try:
      choice = input('Do you wish to continue?  Press Y to continue or any other character to quit: ')

      if (choice != "Y" and choice != "y"):
        break
      else:
        (number_1,operand,number_2) = promptUserForInput()
        result = total(number_1, operand, number_2)
        display_result(number_1, operand, number_2, result)
  except ValueError:
      print("Try again")

print("Thank you for using calculator.")
