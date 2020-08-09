def detectCapitalUse( word):

		if  word.istitle() == True:
			return True
		elif all([True if i.islower() else False for i in word  ])==True:
			return True
		elif all([True if i.isupper() else False for i in word  ])==True:
			return True
		else:
			return False
