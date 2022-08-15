feed_data = input("Input the values of data you want to stem-display (seperate with single spacing):\n\n")
feed_data = feed_data.split()
fed_data = []
for hin in feed_data:
	hin = int(hin)
	fed_data.append(hin)

def unitdetect(x):
	'''
	This function check to determine the place value of the
	given number data. This will allow us to work faster as 
	we go deeper in our main program.
	'''
	if (x/10) > 0 and (x/10) < 1:
		stem = 0
		leaf = x
	elif (x/10) < 10:
		stem, leaf = x//10, x%10
	else:
		fed_data.remove(x)
		
	
	return stem, leaf

def stemdisplay(data_list):
	'''
	Create a dictionary. Loop through your data list; fill in your
	dictionary and sort. Showcase the output.
	'''
	dictlist = dict()
	for number in data_list:
		val = unitdetect(number)
		if val[0] not in dictlist:
			dictlist[val[0]] = [val[1]]
		else:
			dictlist[val[0]].append(val[1])
			dictlist[val[0]].sort()
		y = list(dictlist.keys())
		y.sort()
		
	print ("\nStem	  Leaf")			
	for g in y:
		print (f"{g}	  {dictlist[g]}")
		
	
stemdisplay(fed_data)

