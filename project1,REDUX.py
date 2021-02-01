print("Logical Expressions Evaluator")
print("-----------------------------")
numVar = int(input("Enter the number of variables in the expression: "))

def trueOrFalse(x):
	if x.startswith('f' or 'F'):
		return False
	if x.startswith('t' or 'T'):
		return True
	if not x.startswith('t' or 'T' or 'F' or 'f'):
		print("Please enter a valid value")
		findNumVar(numVar)

def findNumVar(numVar):
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
boolArray = exp.split(" ")
hi = ""

for i in range(len(boolArray)):
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
	elif ("n" == boolArray[i]):
		boolArray[i] = boolArray[i].replace("n", "not ")
	if ("and" != boolArray[i] and "or" != boolArray[i] and 'n' in boolArray[i]):
		hi = str(eval(boolArray[i])) + " "
		hi = not eval (hi)
	if ("not" in boolArray[i]):
		boolArray[i] = str(hi)

sentence = " ".join(boolArray)
print(sentence)
answer = eval(sentence)

if (answer == True):
	print("The truth value of the given logical expression is: True")
else:
	print("The truth value of the given logical expression is: False")