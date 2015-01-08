def listtype(list):
	if list == sorted(list):
		return 'steadily increasing sequence'
	elif list == sorted(list, reverse = True):
		return 'steadily decreasing sequence'
	else: return 'else'

l1 = [1,2,3,4,5,6,7]
l2 = [7,6,5,4,3,2,1]
l3 = [2,1,5,7,6,3,4]

print listtype(l1)
print listtype(l2)
print listtype(l3)

