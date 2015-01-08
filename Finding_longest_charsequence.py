
example_sequence = "AACCCCTGACTTGGAAACTTGGCCAACAGGGT"

all_time_biggest_subseq = 1
biggest_subseq = 1

for index in range(len(example_sequence)-1):
	if example_sequence[index] == example_sequence[index+1]:
		biggest_subseq += 1
		if biggest_subseq > all_time_biggest_subseq:
			all_time_biggest_subseq += 1
			char = example_sequence[index]
			start_position = index + 2 - all_time_biggest_subseq
			end_position = index + 2 
	else:
		biggest_subseq = 1
longest_subseq = char * all_time_biggest_subseq
print 'The longest subsequence is %s, its %d characters long and its position is %d:%d.' % (longest_subseq, all_time_biggest_subseq,
 start_position, end_position)

