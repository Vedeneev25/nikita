import math

vyr = input("vyrazinie").replace(' ', '')
vyrlist = list(vyr)
chisla =['']
znaki = []
OUTPUT =[]
stack = []
nepon =[]
result=''
ops = {'+':2, '-':2, '/':1, '*':1, '^':0, 'sqrt':0}
print(vyr)
print(vyrlist)

for i, letter in enumerate(vyrlist):
    if letter in '+-/*^' and (i>0) and chisla[len(znaki)] != '':
        znaki.append(letter)
        chisla.append('')
    else:
        index = len(znaki)
        chisla[index] = chisla[index] + letter
print(chisla)
print(znaki)
for i in range(max(len(chisla), len(znaki))):
    if i < len(chisla):
        nepon.append(chisla[i])
    if i < len(znaki):
        nepon.append(znaki[i])


print(nepon)
#цикл для отрицалова и корней
for i, l in enumerate(nepon):
    if 'sqrt' in str(l) and ('1' in str(l) or '2' in str(l) or '3' in str(l) or '4' in str(l) or '5' in str(l) or '6' in str(l) or '7' in str(l) or '8' in str(l) or '9' in str(l)):
        nepon[i] = str('(' + nepon[i] + '^0.5)')

for i, l in enumerate(nepon):
    if 'sin' in str(l) and ('1' in str(l) or '2' in str(l) or '3' in str(l) or '4' in str(l) or '5' in str(l) or '6' in str(l) or '7' in str(l) or '8' in str(l) or '9' in str(l)):
       t = (nepon[i].split('sin'))
       v = float(t.pop())
       nepon[i] = str(math.sin(v))
       
for i, l in enumerate(nepon):
    if 'cos' in str(l) and ('1' in str(l) or '2' in str(l) or '3' in str(l) or '4' in str(l) or '5' in str(l) or '6' in str(l) or '7' in str(l) or '8' in str(l) or '9' in str(l)):
       t = (nepon[i].split('cos'))
       v = float(t.pop())
       nepon[i] = str(math.cos(v))
       
for i, l in enumerate(nepon):
    if '-' in str(l) and ('1' in str(l) or '2' in str(l) or '3' in str(l) or '4' in str(l) or '5' in str(l) or '6' in str(l) or '7' in str(l) or '8' in str(l) or '9' in str(l)):
        nepon[i] = str('(0' + nepon[i] + ')' )
       


vyr = ''.join(nepon)


#что то на польском
for i in vyr:
    
    if i in '0123456789.':
        if len(OUTPUT) == 0:
            OUTPUT = [i] + OUTPUT
        else:
            if OUTPUT[0][-1] in '0123456789.' and digit: OUTPUT[0] += i
            else: OUTPUT = [i] + OUTPUT
        digit = True
    else: digit = False
    
    if i == '(':
        stack = [i] + stack
    
    if i == ')':
        while stack != [] and stack[0] != '(': OUTPUT, stack = [stack[0]] + OUTPUT, stack[1:]
        if stack != [] and stack[0] == '(': stack = stack[1:]
    
    if i in ops:
        while stack != [] and stack[0] in ops and ops[i] >= ops[stack[0]]: OUTPUT, stack = [stack[0]] + OUTPUT, stack[1:]
        stack = [i] + stack

while stack != []: OUTPUT, stack = [stack[0]] + OUTPUT, stack[1:]

print('инфиксная запись:\t%s' % (vyr))
print('постфиксная запись:\t%s' % (" ".join(reversed(OUTPUT))))

for i, l in enumerate(OUTPUT):
    if '^' in str(l) and '^' in str(OUTPUT[i+2]):
        OUTPUT[i+1], OUTPUT[i+2] = OUTPUT[i+2], OUTPUT[i+1]

OUTPUT = " ".join(reversed(OUTPUT))
print(OUTPUT)

#расчет
kk = []
for i, letter in enumerate(OUTPUT.split()):
    if '.' in letter or '0' in letter or '1' in letter or '2' in letter or '3' in letter or '4' in letter or '5' in letter or '6' in letter or '7' in letter or '8' in letter or '9' in letter:
        kk.append(letter)
    elif letter == '*':
        vtor = float(kk.pop())
        per = float(kk.pop())
        kk.append(per*vtor)
    
    elif letter == '^':
        vtor = float(kk.pop())
        per = float(kk.pop())
        kk.append(per**vtor)
    elif letter == '+':
        vtor = float(kk.pop())
        per = float(kk.pop())
        kk.append(per+vtor)
    elif letter == '-':
        vtor = float(kk.pop())
        per = float(kk.pop())
        kk.append(per-vtor)
    elif letter == 'sqrt':
        vtor = float(kk.pop())
        kk.append(vtor**0.5)
    elif sin in letter:
        vtor = float(kk.pop())
        kk.append(math.sin(vtor))
                     
    elif letter == '/':
        vtor = float(kk.pop())
        per = float(kk.pop())
        if vtor == 0:
            print('durak chtoli sovsem')
            result = 'inf'
            break
        else:
            kk.append(per/vtor)
    else:
        print('gg')
        
if result == 'inf':
    print('INF')
else:
    print('result:' + str(kk[0]) )
        
        
    
