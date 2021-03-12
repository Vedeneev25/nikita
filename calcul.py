str_command = input("введи команду ")

sF = ''
str_A = ''

sS = ''
str_B = ''

operation = ''
i=0

while i < len(str_command):
	print (str_command [i])
	if str_command[i] == '+' or str_command[i] == '-' or str_command[i] == '*' or str_command[i] == '/' or str_command[i] == '^':
		if str_A == '':
			sF = str_command[i]
		elif operation != '':
			sS = str_command[i]
		else:
			operation = str_command[i]
	else:	
		if operation == '':
			str_A = str_A + str_command[i]
		else:
			str_B = str_B + str_command[i]
	i += 1 
	pass

str_A = sF + str_A.strip()
str_B = sS + str_B.strip()
print(str_A)
print(str_B)


delimoe = float(str_A)

delitel = float(str_B)

result = None

if operation == '/':
    if delitel == 0:
    	result = 'Inf'
    else:
    	result = delimoe / delitel

elif operation == '+':
	result= delimoe + delitel
elif operation == '-':
	result = delimoe - delitel
elif operation == '*':
	result = delimoe * delitel
elif operation == '^':
	result = delimoe ** delitel

else: 
	result = "unknown"


print("Result: " + str(result))