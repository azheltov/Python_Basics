for i in range(29, 3, -1):
    print(i, end=" ")
    

    
    
    
    
    
from math import sqrt	
L = []	
for i in range(1, 100):	
	L.append(round(sqrt(i), 4))
print(L)	



# AND, OR, NOT

num = eval(input ("Please enter a number: "))                                 # eval - convert to int
if not (num == 0 or num ==2 or num==5 or 10<num<15 or 20<num<25):
	print("Ok")
else:
	print("Not okay")
	

l = input("Enter prog language: ")
l = l.lower()
if l == "python":
	return "Yes"
	

# l.replace()
# x.isalpha()

# x = 'abc'
# x.index("b")             - gives index of the char

breakpoint = name.index(' ')
first = name.[:breakpoint]
last = name[breakpoint+1:]

###
#1
s = 'The weather is so nice'
print(s[0],end="")
for i in range(len(s)):
    if s[i] == " ":
        print(s[i+1],end="")
	
#2
s = 'The weather is so nice'
z = s.split()
a = []
for i in range(len(z)):
	a.append(z[i][0])

print(a)

# split is based on " "
##

email = 'johndoe@hotmail.com'
breakpoint = email.index("@")
print("User name:", email[:breakpoint], "Domain: ", email[breakpoint+1:])

##
L = blal bla bla numbers
mx = max(L)

for x in L:
	if 10 < x < mx:
		mx = x
print("Smallest thing grater than 10: ", mx)

##
#JOIN concaternates STRRINGs
#JOIN converts list.join(num(list))         JOIN and SEPARATOR

ourList = ['1','2','3']
sep = ','
print(sep.join(ourList))

##

L = [18,25,30]
M = [18,2,30]

##

L = eval(input("Enter a list of integer: "))                             # create an input list 
M = [x+1 for x in L if x%2 == 0]                                         # comprehesion 1) loop 2) if 3) begging
print(M)

##


myList = []
for x in range(len(L)):
	if L[x] > M[x]:
		myList.append(L[x])
	else:
		myList.append(M[x])
print(myList)

##

from random import randint
studentList = []
for s in range(10):
    x = randint(90,100)
    studentList.append(x)
print(studentList)

lucky_index = randint(0,9)
studentList[lucky_index] = 0
print(studnetList)

##

L = ['a','bc','d','e','fg']
I = [4,2]

for i in range(len(I)):
    L.pop(I[i])

print(L)

#OR

L = ['a','bc','d','e','fg']
I = [4,2]

M = []
for x in range(len(L)):
	if x not in I:                         # NOT IN
		M.append(L[x])
print(M)

##

from random import choice
s = ''
for i in range(100):
    s += choice('HT')                         # CHOICE
print(s)

##
						# % probability
letter = 'A'*60 + 'B'*30 + 'C'*8 + 'D'*2
s = []
for i in range(1000):
	s.append(choice(letter))

print(''.join(s))

##

from random import smaple                                  # SAMLE function !!!
from random import sample
c = "python"
indices = []

for i in range(len(c)):
    indices.append(i)

spots = sample(indices,3)
t = ''

for i in range(len(c)):
    if i in spots:
        t += "*"
    else:
        t += c[i]

print(t)

##

myList = []
for i in range(100):
    myList.append(i ** 2)

print(myList)

list_using_compre = [i**2 for i in range(100)]               # COMPREHENSION
print(list_using_compre)

# OR

from math import sqrt
L=[round(sqrt(i),2) for i in range(100)]                     # ROUND        2 decemal
print(L)

##
L = [[1,23],[2,3], [34,78]]
L1 = []
for x in range(len(L)):
    y = L[x]
   L1.append(y[-1])
print(L1)

#OR with comprehension

L = [[1,23],[2,3], [34,78]] 
M = [x[-1] for x in L]
print(M)

##

L = 'helloworld'
k = []
for char in L:
    k.append(char)
s = sorted(k)
print(s)

##

s = "helloworld"
L = [s.count(s.count(c) for c in "abcdefghijklmnopqrstuvwxyz"]
print(L)
	     
	     ##
string1 = "python?"
string2 = "Python!"
L = []
for x in range(len(string1)):
    if string1[x] != string2[x]:
        print("yes",x)
        L.append(x)
print(L)
	     
#comprehesion 
#k = [L.append(x) for x in range(len(string1)) if string1[x] != string2[x]]
#print(L)
	     
	     #OR just
	     #L = [x for x in range(len(string1)) if string1[x] != string2[x]]
	     #print(L)
	     
nested_list = [[1,2,3],[4,5,6],[7,8,9]]
print(nested_list[1][2])
for l in nested_list:
    for val in l:
        print(val,end='')

#comprehension
k = [l for l in nested_list]
print(k)

                                        # new line (don forget!)  \n

for i in range(7,9):
    for j in range(1,11):
        print(f'{i}*{j}={i*j}')         # print with       f'{}'
	     
#   [i * j for j in range(1,11) for i in range(7,9)] - flat output
#   [[i * j for j in range(1,11)] for i in range(7,9)] - nested list
	     
from random import randint
L = [[randint(0,1) for x in range(10)]for x in range(10)]                 #randint
print(L)
	     
#OR
	     
	    
from random import randint
arr = []
for i in range(10):
    arr.append([])
    for j in range(10):
        arr[i].append(randint(0,1))

print(arr) 

	     ##                                                 BATTLESHIP
from random import randint
arr = []
for i in range(10):
    arr.append([])
    for j in range(10):
        arr[i].append(randint(0,1))

r = int(input("Enter two row from 0 to 9: "))
c = int(input("Enter colomn number from 0 - 9: "))

if arr[r][c] == 0:
    print("Missed")
else:
    print("Hit")
	     
	     ##

from random import randint
k =[]
k = [[randint(0, 2) for i in range(6)]for i in range(6)]
print(k)

r1 = eval(input("Enter starting row: "))
r2 = eval(input("Enter ending row: "))
c1 = eval(input("Enter starting col: "))
c2 = eval(input("Enter ending col: "))

total = 0
for i in range(r1, r2+1):
    for j in range(c1, c2+1):
        total += k[i][j]

print(total)
	     
	     ##
