str_command = input("введи команду например 2 + 4 ").replace (' ','')
sF =''
sS =''
str_A =''
str_B =''
operation =''
for letter in enumerate(str_command):
    if letter in =='+-/*^' :
        if str_A == '':
            sF = letter
        elif operation != '':
            sS = letter
        else:
            operation = letter
    else:
        if operation =='':
            str_A = str_A + letter
        else:
            str_B = str_B + letter
            
str_A = sF + str_A.strip()
str_B = sS + str_B.strip()

c = float(str_A)
#print(type(c))

d = float(str_B)
#print(type(d))

if operation == '/':
    if d == 0:
        result = 'inf'
    else:    
        result = eval('{0}{1}{2}'.format(c,operation,d))
elif operation == '^':
    result = c ** d
else:
    result = "unknown"
#print(type(result))
print("Result: " + str(result))




























