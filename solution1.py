def answer(numbers):
	numbersSeen=[]
	#numbersSeen.append(0)
	loopStartIndex = 0
	numberCount = 0
	index = 0

	print numbers
	while True:
		numbersSeen.append(numbers[index])
		index2 = 0
		while index2 != len(numbersSeen):
			if numbers[index] == numbersSeen[index2]:
				numberCount = numberCount + 1
			index2 = index2 + 1
		if numberCount == 2:
			loopStartIndex = numbers[index]
			numberCount = 0
			break
		else: 
			numberCount = 0
		index = numbers[index]

	loopCount = 1
	loopStart = numbers[loopStartIndex]
	loopNext = loopStart
	while True:
		loopNext = numbers[loopNext]
		numberCount = numberCount + 1
		if loopNext == loopStart:
			return numberCount

numbers = [1,2,3,1]
numbers2 = [1,5,3,2,4,2]
asdf = answer(numbers2)
print asdf
