def threetimes(fun, number):
	return fun(number)*3

print threetimes(lambda x: x*3, 10)

def third(number):
	return number/ 3

print threetimes(third, 10)

def double(number):
	return number* 2

print threetimes(double, 10)

def chain(list_of_functions, integer):
	for i in list_of_functions:
		integer = list_of_functions[i](integer)
	return integer

print chain([double, third], 6)
