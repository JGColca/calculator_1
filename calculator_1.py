number_1 = float(input("Please enter a number: "))
operand = input("Please enter an operand (+,-,*,/):")
number_2 = float(input("Please enter another number: "))

def total(number_1,number_2):
    if operand == "+":
      result = number_1 + number_2
      return result
    elif operand == "-":
      result = number_1 - number_2
      return result
    elif operand == "-":
      result = number_1 * number_2
      return result
    elif operand == "/":
      result = number_1 / number_2
      return result
print(total(number_1,number_2))
