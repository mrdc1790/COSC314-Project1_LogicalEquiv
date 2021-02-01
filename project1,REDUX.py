#   By: Adam Pollack
#	E02063895
#   Created: 1/27/2021
#   For: COSC 314 - Discrete Mathematics
#	Title: Project 1: Logical Expressions Evaluator
#   Function: Takes a logical expression and evaluates the truth value - True or False

print("Logical Expressions Evaluator")
print("-----------------------------")
numVar = int(input("Enter the number of variables in the expression: "))

def trueOrFalse(x): #used to return a boolean value when given a string
	if x.startswith('f' or 'F'):
		return False
	if x.startswith('t' or 'T'):
		return True
	if not x.startswith('t' or 'T' or 'F' or 'f'): #used to replicate if given wrong input
		print("Please enter a valid value")
		findNumVar(numVar)

def findNumVar(numVar): #used to return a boolean value to the respective variable when given a certain number of inputs
	print("Enter the values of variables - true or false: ")
	global numA, numB, numC, numD, numE
	global a, b, c, d, e
	if numVar == 1:
		a = (input("a: "))
		numA = trueOrFalse(a)
	elif numVar == 2:
		a = (input("a: "))
		b = (input("b: "))
		numA = trueOrFalse(a)
		numB = trueOrFalse(b)
	elif numVar == 3:
		a = (input("a: "))
		b = (input("b: "))
		c = (input("c: "))
		numA = trueOrFalse(a)
		numB = trueOrFalse(b)
		numC = trueOrFalse(c)
		return
	elif numVar == 4:
		a = (input("a: "))
		b = (input("b: "))
		c = (input("c: "))
		d = (input("d: "))
		numA = trueOrFalse(a)
		numB = trueOrFalse(b)
		numC = trueOrFalse(c)
		numD = trueOrFalse(d)
	elif numVar == 5:
		a = (input("a: "))
		b = (input("b: "))
		c = (input("c: "))
		d = (input("d: "))
		e = (input("e: "))
		numA = trueOrFalse(a)
		numB = trueOrFalse(b)
		numC = trueOrFalse(c)
		numD = trueOrFalse(d)
		numE = trueOrFalse(e)
	else:
		print("Please enter 2-5 variables")
		numVar = int(input("Enter the number of variables in the expression: "))
		findNumVar(numVar)

findNumVar(numVar)
exp = input("Enter a logical expression: ")
boolArray = exp.split(" ")  #take the input (string) and converts it to an array
hi = ""   #initalize a string to pass booleans through

for i in range(len(boolArray)): #the bulk of the programs work is done here; evaluates which variables are used in the expression
								# and stores the string version of the boolean within the preexisting spot in the array
	if ("and" != boolArray[i]):
		boolArray[i] = boolArray[i].replace('n', "not ")
	if ('a' == boolArray[i]):
		boolArray[i] = str(numA)
	elif ('b' == boolArray[i]):
		boolArray[i] = str(numB)
	elif ('c' == boolArray[i]):
		boolArray[i] = str(numC)
	elif ('d' == boolArray[i]):
		boolArray[i] = str(numD)
	elif ('e' == boolArray[i]):
		boolArray[i] = str(numE)
	if ("and" != boolArray[i] and "or" != boolArray[i] and 'n' in boolArray[i]): #condition to deal with operators and not screw up "and" cuz it has an 'a' in it
		hi = str(eval(boolArray[i])) + " "
		hi = not eval(hi)
	if ("not" in boolArray[i]):
		boolArray[i] = str(hi)

sentence = " ".join(boolArray)
print(sentence)
print(boolArray)
answer = eval(sentence)

if (answer == True):
	print("The truth value of the given logical expression is: True")
else:
	print("The truth value of the given logical expression is: False")