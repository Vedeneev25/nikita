str_input = input("первое число: ")
A = int(str_input)
#print(type(delimoe))
operation = input("+ / * - ^")

str_input2 = input("Второе число: ")
B = int(str_input2)
#print(type(delitel))

if operation == '/':
    result = A / B
elif operation == '+':
    result = A + B
elif operation == '-':
    result = A - B
elif operation == '*':
    result = A * B
elif operation == '^':
    result = A ** B
else:
    result = "unknown"
#print(type(result))
print("Result: " + str(result))