def unitdetect(x):
	
	if (x/10) > 0 and (x/10) < 1:
		stem = 0
		leaf = x
	elif (x/10) < 10:
		stem, leaf = x//10, x%10
	else:
		return None
	
	return stem, leaf


def stemdisplay(*data_list):
	dictlist = dict()
	for number in data_list:
		val = unitdetect(number)
		if val[0] not in dictlist:
			dictlist[val[0]] = [val[1]]
		else:
			dictlist[val[0]].append(val[1])
			dictlist[val[0]].sort()
		
	print ("Stem	  Leaf\n")			
	for k, v in dictlist.items():
		print (f"{k}	  {v}")

stemdisplay(23, 56, 23, 73, 12, 9, 4, 40)
