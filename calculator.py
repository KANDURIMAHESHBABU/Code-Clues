def calculate(n1,n2,op):
  if op == '+':
    return n1 + n2
  elif op == '-':
    return n1 - n2
  elif op == '*':
    return n1 * n2
  elif op == '/':
    return n1 / n2
  else:
    return "Invalid operator"

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
operator = input("Enter operator (+, -, *, /): ")

result = calculate(num1, num2, operator)
print(result)
