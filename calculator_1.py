number_1 = float(input("Please enter a number: "))
operand = input("Please enter an operand (+,-,*,/):")
number_2 = float(input("Please enter another number: "))

#def total(number_1,number_2):
#    if operand == "+":
#      result = number_1 + number_2
#      return result
#    elif operand == "-":
#      result = number_1 - number_2
#      return result
#    elif operand == "-":
#      result = number_1 * number_2
#      return result
#    elif operand == "/":
#      result = number_1 / number_2
#      return result
#print(total(number_1,number_2))

def add(number_1,number_2):
    if operand == "+":
      result = number_1 + number_2
      return result

def sub(number_1,number_2):
    if operand == "-":
      result = number_1 - number_2
      return result

def mult(number_1,number_2):
    if operand == "*":
      result = number_1 - number_2
      return result

def div(number_1,number_2):
    if operand == "/":
      result = number_1 - number_2
      return result

print (add(number_1,number_2))
print (sub(number_1,number_2))
print (mult(number_1,number_2))
print (div(number_1,number_2))
