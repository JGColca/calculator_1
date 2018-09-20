
def promptUserForInput():

    number_1 = float(input("Please enter a number: "))
    operand = input("Please enter an operand (+,-,*,/): ")
    number_2 = float(input("Please enter another number: "))
    return (number_1, operand, number_2)

    print(number_1)

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
    #print(f"{no1} {choice} {no2} = {result}")
    print("**********************")
    print()

(number_1,operand,number_2) = promptUserForInput()
result = total(number_1, operand, number_2)
display_result(number_1, operand, number_2, result)

while True:
  try:
      choice = input('Do you wish to continue?  Press Y to continue or any other character to quit:')

      if (choice != "Y" and choice != "y"):
        break
      else:
        (number_1,operand,number_2) = promptUserForInput()
        result = total(number_1, operand, number_2)
        display_result(number_1, operand, number_2, result)
  except ValueError:
      print("Try again")

print("Thank you for using calculator.")
