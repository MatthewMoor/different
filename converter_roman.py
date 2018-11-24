def converter(num):
	romanNumeral = [ 'M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I' ]
	arabicNumeral = [ 1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1 ]
	
	romanized = ''
	
	for i, val in enumerate(arabicNumeral):
		while arabicNumeral[i] <= num:
			romanized += romanNumeral[i]
			num -= arabicNumeral[i]
	return romanized

print(converter(35))
