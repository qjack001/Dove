


def label(line):
	global labels
	name = line.split()[0][1:]

	if name[-1] == ":":
		name = name[:-1]

	labels[name] = lineNumber


def getVar(var):
	if var in vars:
		return vars[var]
	else:
		error("Variable \"" + var + "\" does not exist.")


def getMem():
	if memory[0] == "\"":
		return memory
	elif isNum(memory):
		return memory
	else:
		return getVar(memory.split()[0])


def command(line):
	if len(line) <= 0:
		return
	elif line[0] == "#":
		label(line)
		return

	elem = line.split()

	if elem[0] == "print":
		printFunc(line)
	elif elem[0] == "str":
		strFunc(line)
	elif elem[0] == "ldr":
		ldrFunc(line)
	elif elem[0] == "new":
		newFunc(line)
	elif elem[0] == "add":
		addFunc(line)
	elif elem[0] == "sub":
		subFunc(line)
	elif elem[0] == "rsft":
		shiftRightFunc(line)
	elif elem[0] == "lsft":
		shiftLeftFunc(line)
	elif elem[0] == "if":
		ifFunc(line)
	elif elem[0] == "goto":
		gotoFunc(line)
	elif elem[0][0] == "@":
		#this is a comment, disregard
		pass
	else:
		error("Command \"" + elem[0] + "\" not found.")

def newFunc(line):
	global vars
	elem = line.split()

	if len(elem) <= 1:
		error("Token expected after \"new\".")
	elif elem[1] in vars:
		error("Variable \"" + elem[1] + "\" already exists.")
	elif isNum(elem[1]) or elem[1][0] == "\"":
		error("Invalid variable name \"" + elem[1] + "\".")
	else:
		vars[elem[1]] = None


def addFunc(line):
	global memory
	elem = line.split()

	one = 0
	two = 0

	if len(elem) <= 1:
		error("Token expected after \"add\".")
	elif len(elem) == 2:
		one = getMem()
		two = elem[1]
	else:
		one = elem[1]
		two = elem[2]


	if (not isNum(one)) and (one[0] != "\""):
		one = getVar(one)

	if (not isNum(two)) and (two[0] != "\""):
		two = getVar(two)


	if isNum(one) and isNum(two):
		memory = str(int(one) + int(two))
	else:
		memory = "\"" + one.strip("\"") + two.strip("\"") + "\""



def subFunc(line):
	global memory
	elem = line.split()

	one = 0
	two = 0

	if len(elem) <= 1:
		error("Token expected after \"add\".")
	elif len(elem) == 2:
		one = getMem()
		two = elem[1]
	else:
		one = elem[1]
		two = elem[2]


	if (not isNum(one)) and (one[0] != "\""):
		one = getVar(one)

	if (not isNum(two)) and  (two[0] != "\""):
		two = getVar(two)

	if isNum(one) and isNum(two):
		memory = str(int(one) - int(two))
	else:
		error("Cannot preform subtraction on String value.")


def shiftLeftFunc(line):
	global memory
	elem = line.split()
	one = 0
	two = 0

	if len(elem) <= 1:
		error("Token expected after \"lsft\".")
	elif len(elem) == 2:
		one = getMem()
		two = elem[1]
	else:
		one = elem[1]
		two = elem[2]

	if (not isNum(one)) and (one[0] != "\""):
		one = getVar(one)

	if (not isNum(two)) and  (two[0] != "\""):
		two = getVar(two)

	if isNum(one) and isNum(two):
		memory = str(int(one) << int(two))
	else:
		error("Cannot preform arithmetic shift on String value.")


def shiftRightFunc(line):
	global memory
	elem = line.split()
	one = 0
	two = 0

	if len(elem) <= 1:
		error("Token expected after \"rsft\".")
	elif len(elem) == 2:
		one = getMem()
		two = elem[1]
	else:
		one = elem[1]
		two = elem[2]

	if (not isNum(one)) and (one[0] != "\""):
		one = getVar(one)

	if (not isNum(two)) and  (two[0] != "\""):
		two = getVar(two)

	if isNum(one) and isNum(two):
		memory = str(int(one) >> int(two))
	else:
		error("Cannot preform arithmetic shift on String value.")


def ifFunc(line):
	global lineNumber
	statement = line[3:].strip()

	if isTrue(statement):
		pass
	else:
		lineNumber += 1;


def isTrue(eq):
	operators = ["==","!=","<=",">=","<",">"] #todo: add all
	

	if "==" in eq:
		first = eq.split("==")[0].strip()
		second = eq.split("==")[1].strip()
		if not isNum(first):
			first = getVar(first)
		else:
			first = int(first)
		if not isNum(second):
			second = getVar(second)
		else:
			second = int(second)

		if isNum(str(first)) and isNum(str(second)):
			return int(first) == int(second)
		elif not (isNum(str(first)) and isNum(str(second))):
			return first == second
		else:
			error("Cannot compare \"" + first + "\" and \"" + second + "\".")
	elif "<" in eq:
		first = eq.split("<")[0].strip()
		second = eq.split("<")[1].strip()
		if not isNum(first):
			first = getVar(first)
		else:
			first = int(first)
		if not isNum(second):
			second = getVar(second)
		else:
			second = int(second)

		if isNum(str(first)) and isNum(str(second)):
			return int(first) < int(second)
		elif not (isNum(str(first)) and isNum(str(second))):
			return first < second
		else:
			error("Cannot compare \"" + first + "\" and \"" + second + "\".")

def find(label):
	global labels
	for i in range(len(content)):
		if len(content[i]) >= 1:
			if content[i][0] == "#":
				labels[content[i][1:]] = i

def gotoFunc(line):
	global lineNumber
	elem = line.split()

	if len(elem) <= 1:
		error("Token expected after \"goto\".")

	find(elem[1])

	if elem[1] not in labels:
		error("The tag \"" + elem[1] + "\" does not exist.") #todo: search for labels down the line

	lineNumber = labels[elem[1]]


def strFunc(line):
	global memory
	elem = line.split()

	if len(elem) <= 1:
		error("Token expected after \"str\".")
	
	isNum(line[4:].strip())
	memory = line[4:].strip()


def ldrFunc(line):
	global vars
	elem = line.split()

	if len(elem) <= 1:
		error("Token expected after \"ldr\".")

	if elem[1] not in vars:
		error("Variable \"" + elem[1] + "\" does not exist.")
	else:
		vars[elem[1]] = getMem()


def printFunc(line):
	elem = line.split()

	if len(elem) <= 1:
		print(getMem())
	elif elem[1][0] == "\"":
		print(line.split("\"")[1])
	elif isNum(elem[1][0]):
		print(elem[1][0])
	else:
		print(getVar(elem[1]))


def isNum(input):
	digits = "1234567890"

	if len(input) <= 0:
		return False
	if input[0] not in digits:
		return False

	for i in input:
		if i not in digits:
			error("Invalid variable name \"" + input + "\".")

	return True


def error(msg):
	print("♫♪ this is what it sounds like when doves cry ♫♪")
	print("\n\nError on line " + str(lineNumber + 1) + ":\n" + msg)
	quit()



def main():
	global lineNumber
	fname = input()
	global content

	try:
		with open(fname) as f:
		    content = f.readlines()
	except Exception:
		error("Unable to open file.")

	content = [x.strip().lower() for x in content]

	
	try:
		while lineNumber < len(content):
			command(content[lineNumber])
			lineNumber += 1
	except Exception:
		error("Unknown error (tell jack).")



memory = 0
lineNumber = 0
labels = dict()
vars = dict()
content = None
main()

