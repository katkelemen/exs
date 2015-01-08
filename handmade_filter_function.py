def filtero(callable, item):
 	newlist = []
 	for i in item:
 		if callable(i):
 			newlist.append(i)
 	return newlist


def stupidcondition(x): 
	return x > 5

print filter(stupidcondition,  [1,2,3,4,5,6,7,8,9])
print filter(lambda x: x>5, [1,2,3,4,5,6,7,8,9])
print filtero(stupidcondition, [1,2,3,4,5,6,7,8,9])
print filtero(lambda x: x>5, [1,2,3,4,5,6,7,8,9])

