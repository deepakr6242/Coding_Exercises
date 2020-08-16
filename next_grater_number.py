
def find_ngn(list_):
	unique = []    #to  avoid checking the same item again
	if len(list_)>1:
			for index,value in enumerate(list_):
					list_of_elements_except_the_value = list_[index+1:]
					for  nge in list_of_elements_except_the_value :
							if nge >value and value  not in unique:
								print("{}'s next Greater element  is {}".format(value,nge))
								unique.append(value)
								break

	else:
			print('No  adjacent numbers to find NGe and hence is ',str(list_))
			return list_


if __name__ == '__main__':
	junk_array= (-1,2,'1','&',3,'',4,5,6,78,90,23,-121212,34,4,5,6,6,8,8,89)
	cleaned_array = [ i for i in junk_array  if isinstance(i,int)]
	print(cleaned_array)
	if isinstance(cleaned_array,list):
		find_ngn(cleaned_array)
	else:
		find_nge(list(cleaned_array))

