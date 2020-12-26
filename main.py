class customDict: 

	# Create empty bucket list of given size 
	def __init__(self, size): 
		self.size = size 
		self.hash_table = self.create_buckets() 

	def create_buckets(self): 
		return [[] for _ in range(self.size)] 

	# Insert values into hash map 
	def set_val(self, key, val): 
		
		# Get the index from the key 
		# using hash function 
		hashed_key = hash(key) % self.size 
		
		# Get the bucket corresponding to index 
		bucket = self.hash_table[hashed_key] 

		found_key = False
		for index, record in enumerate(bucket): 
			record_key, record_val = record 
			 
			# check if the bucket has same key as 
			# the key to be inserted 
			if record_key == key: 
				found_key = True
				break

		# If the bucket has same key as the key to be inserted, 
		# Update the key value 
		# Otherwise append the new key-value pair to the bucket 
		if found_key: 
			bucket[index] = (key, val) 
		else: 
			bucket.append((key, val)) 

	# Return searched value with specific key 
	def get_val(self, key): 
		
		# Get the index from the key using 
		# hash function 
		hashed_key = hash(key) % self.size 
		
		# Get the bucket corresponding to index 
		bucket = self.hash_table[hashed_key] 

		found_key = False
		for index, record in enumerate(bucket): 
			record_key, record_val = record 
			
			# check if the bucket has same key as 
			# the key being searched 
			if record_key == key: 
				found_key = True
				break

		# If the bucket has same key as the key being searched, 
		# Return the value found 
		# Otherwise indicate there was no record found 
		if found_key: 
			return record_val 
		else: 
			return 0

	# To print the items of hash map 
	def __str__(self): 
		return "".join(str(item) for item in self.hash_table) 


leastBirthYear = 3000                         # Finding the least birth year from the input provided
maxDeathYear = 0
birthYearArray = []
deathYearArray = []
recordCount = 0
def countBorn(dict, year):
    return dict.get_val(str(year))

def countDied(dict, year):
    return dict.get_val(str(year))

def maxPop(dict):
    max = -1
    for i in range(leastBirthYear,maxDeathYear+1):
        if dict.get_val(str(i)) > max:
            max = dict.get_val(str(i))
            maxPopYear = i
    return maxPopYear

def minPop(dict):
    min = dict.get_val(str(leastBirthYear))
    for i in range(leastBirthYear,maxDeathYear+1):
        if dict.get_val(str(i)) < min:
            min = dict.get_val(str(i))
            minPopYear = i
    return minPopYear

def maxBirth(dict):
    max = 0
    for i in birthYearArray:
        if dict.get_val(str(i)) > max:
            max = dict.get_val(str(i))
            maxBirthYear = i
    return maxBirthYear

def maxDeath(dict):
    max = 0
    for i in deathYearArray:
        if dict.get_val(str(i)) > max:
            max = dict.get_val(str(i))
            maxDeathYear = i
    return maxDeathYear


def printOutput(dict):
    try:
        try:
            readPrompts = open('promptsPS21.txt','r')
        except:
            print("File promptsPS21.txt doesnot exist")
        for line in readPrompts:
            line = line.strip()
            rowSplit = line.split(':')
            if rowSplit[0] == 'bornIn':
                bornInInput = int(rowSplit[1].strip())
                bornCount = countBorn(dict.get_val("birth"),bornInInput)
            elif rowSplit[0] == 'diedIn':
                diedInInput = int(rowSplit[1].strip())
                diedCount = countDied(dict.get_val("death"),diedInInput)
            elif rowSplit[0] == 'maxPopulation':
                maxPopYear = maxPop(dict.get_val("population")) 
                arrMaxYearCount = [ maxPopYear, dict.get_val("population").get_val(str(maxPopYear)) ]
            elif rowSplit[0] == 'minPopulation':
                minPopYear = minPop(dict.get_val("population")) 
                arrMinYearCount = [ minPopYear, dict.get_val("population").get_val(str(minPopYear)) ]
            elif rowSplit[0] == 'maxBirth':
                maxBirthYear = maxBirth(dict.get_val("birth")) 
                maxBirthArray = [ maxBirthYear, dict.get_val("birth").get_val(str(maxBirthYear)) ]
            elif rowSplit[0] == 'maxDeath':
                maxDeathYear = maxDeath(dict.get_val("death")) 
                maxDeathArray = [ maxDeathYear, dict.get_val("death").get_val(str(maxDeathYear)) ]

        #Writing to outputPS21.txt
        writeOutput = open("outputPS21.txt", "w")   #w will create file if it does not exist
        if 'recordCount' in locals():
            recordsCaptured = str(recordCount) + " records captured\n"   #need to complete 
            writeOutput.write(recordsCaptured)
        if 'bornInInput' in locals():
            bornInText = "No. of people born in "+ str(bornInInput) +": "+ str(bornCount)+"\n"
            writeOutput.write(bornInText)
        if 'diedInInput' in locals():
            diedInText = "No. of people died in "+ str(diedInInput) +": "+ str(diedCount)+"\n"
            writeOutput.write(diedInText)
        if 'arrMaxYearCount' in locals():
            maxPopText = "Maximum population was in year "+ str(arrMaxYearCount[0])+" with "+str(arrMaxYearCount[1])+" people alive.\n"
            writeOutput.write(maxPopText)
        if 'arrMinYearCount' in locals():
            minPopText = "Minimum population was in year "+ str(arrMinYearCount[0])+" with "+str(arrMinYearCount[1])+" people alive.\n"
            writeOutput.write(minPopText)
        if 'maxBirthYear' in locals():
            maxBirthText = "Maximum births were in year "+ str(maxBirthArray[0])+" with "+str(maxBirthArray[1])+" people born.\n"
            writeOutput.write(maxBirthText)
        if 'maxDeathYear' in locals():
            maxDeathText = "Maximum deaths were in year "+ str(maxDeathArray[0])+" with "+str(maxDeathArray[1])+" people dead.\n"
            writeOutput.write(maxDeathText)
        
        # Closing the file
        writeOutput.close()
        readPrompts.close()
    except:
        print("Something went wrong while writing output")
        readPrompts.close()
        exit()


def readInputData():
    try:
        try:
            f = open('inputPS21.txt','r')
        except:
            print("File inputPS21.txt doesnot exist")
        global leastBirthYear , deathYearArray, birthYearArray, maxDeathYear, recordCount
        leastBirthYear = 3000                         # Variable to store least birth year from the input provided
        maxDeathYear = 0                              # Variable to store Max Death year from the input provided


        # Used to find the maximum death year and least birth year from the inputs provides
        for line in f:
            recordCount+=1
            line = line.strip()
            rowSplit = line.split(',')
            if(leastBirthYear > int(rowSplit[2].split('-')[2]) ):
                leastBirthYear = int(rowSplit[2].split('-')[2])
            if(rowSplit[3] != ''):
                if(maxDeathYear < int(rowSplit[3].split('-')[2]) ):
                    maxDeathYear = int(rowSplit[3].split('-')[2])



        birthCountDict = customDict(recordCount+1)
        deathCountDict = customDict(recordCount+1)
        f.seek(0)                                                               # Read the file from the beginning
        for line in f:
            line = line.strip()
            rowSplit = line.split(',')
            bcount = birthCountDict.get_val(rowSplit[2].split('-')[2])
            birthCountDict.set_val(rowSplit[2].split('-')[2], bcount+1)
            if rowSplit[2].split('-')[2] not in birthYearArray:
                birthYearArray.append(rowSplit[2].split('-')[2])
            if(rowSplit[3] != ''):
                dcount = deathCountDict.get_val(rowSplit[3].split('-')[2])   
                deathCountDict.set_val(rowSplit[3].split('-')[2], dcount+1)
                if rowSplit[3].split('-')[2] not in deathYearArray:
                    deathYearArray.append(rowSplit[3].split('-')[2])

        maxPopDict = customDict(maxDeathYear - leastBirthYear)
        popInPrevYear = 0
        for i in range(leastBirthYear,maxDeathYear+1):
            popInThatYear = birthCountDict.get_val(str(i))-deathCountDict.get_val(str(i))
            popInThatYear += popInPrevYear
            maxPopDict.set_val(str(i), popInThatYear)
            popInPrevYear = popInThatYear
        dictExtracted = customDict(3)
        dictExtracted.set_val("birth", birthCountDict)
        dictExtracted.set_val("death", deathCountDict)
        dictExtracted.set_val("population", maxPopDict)
        f.close()
        return dictExtracted
        for dictName in dictName.values():
            
    except:
        print("Something went wrong while reading inputs")
        exit()

printOutput(readInputData())
