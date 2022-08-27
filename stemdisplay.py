import time


#for 1 value
user_input = input("Input the values of data you want to stem-display (seperate with single spacing):\n\n")
feed_data = user_input.split()
values = []
for i in feed_data:
	values.append(int(i))
def one_digit(main_digit):
	new_list = []
	for i in str((main_digit)):
		new_list.append(i)
	final_list = new_list
	if len(final_list) > 1:
		power = 10 ** (len(final_list) - 1)
	else:
		power = 10 ** 1
	return power

def unitdetect(val, power):
	'''
	This function check to determine the place value of the
	given number data. This will allow us to work faster as 
	we go deeper in our main program.
	'''
	stem, leaf = val // one_digit(power),  val % one_digit(power)
	return stem, leaf
	
	

def stemdisplay(data_list):

	dictlist = dict()
	val = list()
	for number in data_list:
		k = one_digit(number)
		val = unitdetect(number, k)
		if val[0] not in dictlist:
			dictlist[val[0]] = [val[1]]
		else:
			dictlist[val[0]].append(val[1])
		y = list(dictlist.keys())
		y.sort()
		
	print ("\n Stem	    Leaf")			
	for g in y:
		print (f"  {g}	    {dictlist[g]}")

	
stemdisplay(values)
time.sleep(0.5)
