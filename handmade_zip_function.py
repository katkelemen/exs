def zippo(list1, list2):
	""" Zips 2 lists together. List1 and list2 must be the same lenght. """
	zipped = []
	for index in range(len(list1)):
		zipped[index:] = [[list1[index], list2[index]]]
	return zipped

flower = ['rose', 'daffodil', 'daisy', 'lilac']
color = ['red', 'yellow', 'white', 'violet']

print zippo(color, flower)

