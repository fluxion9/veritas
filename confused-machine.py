def balance(num):
	hails = []
	remainder = num
	while remainder > 0:
		if remainder % 2 == 0:
			hails.append(remainder)
			remainder = remainder / 2
			if remainder == 1:
				hails.append(remainder)
			print(hails)
		else:
			remainder = (3 * remainder) + 1
	return 0



balance(1000)
