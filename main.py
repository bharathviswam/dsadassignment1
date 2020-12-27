class customDictOld: 

	# Create empty bucket list of given size 
	def __init__(self, size): 
		self.size = size 
		self.hash_table = self.create_buckets() 

	def create_buckets(self): 
		return [[] for _ in range(self.size)] 

	# Insert values into hash map 
	def setitem(self, key, val): 
		
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
	def getitem(self, key): 
		
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


class customDict(object):
    """
    custom implementation for dict
    """
    def __init__(self, size=1000):
        """
        use list as storage, each element is also a list which is used
        to solve hash conflict
        """
        self.storage = [[] for _ in range(size)]
        self.size = size
        self.length = 0

    def __setitem__(self, key, value):
        """
        set key value, if conflict, append to the sub list
        """
        storage_idx = hash(key) % self.size
        for ele in self.storage[storage_idx]:
            if key == ele[0]:  # already exist, update it
                ele[1] = value
                break
        else:
            self.storage[storage_idx].append([key, value])
            self.length += 1
    
    def __getitem__(self, key):
        """
        get by key, if not found, raise key error
        :raise: KeyError
        :return: value
        """
        storage_idx = hash(key) % self.size
        for ele in self.storage[storage_idx]:
            if ele[0] == key:
                return ele[1]

        raise KeyError('Key {} dont exist'.format(key))
    
    def __delitem__(self, key):
        """
        delete key value from current dictionary instance
        :param key: str
        :return: None
        """
        storage_idx = hash(key) % self.size
        for sub_lst in self.storage[storage_idx]:
            if key == sub_lst[0]:
                self.storage[storage_idx].remove(sub_lst)
                self.length -= 1
                return

        raise KeyError('Key {} dont exist'.format(key))

    def __contains__(self, key):
        """
        check if key exist in current diction
        :param key: str
        :return: boolean
        """
        storage_idx = hash(key) % self.size
        for item in self.storage[storage_idx]:
            if item[0] == key:
                return True
        return False

    def __len__(self):
        """
        return length
        :return: int
        """
        return self.length

    def __iterate_kv(self):
        """
        return an iterator
        :return: generator
        """
        for sub_lst in self.storage:
            if not sub_lst:
                continue
            for item in sub_lst:
                yield item

    def __iter__(self):
        """
        return an iterator
        :return: generator
        """
        for key_var in self.__iterate_kv():
            yield key_var[0]
    
    def __str__(self):
        """
        str representation of the dictionary
        :return: string
        """
        res = []
        for ele in self.storage:
            for key_value in ele:
                if isinstance(key_value[0], str):
                    key_str = '\'{}\''.format(key_value[0])
                else:
                    key_str = '{}'.format(key_value[0])
                if isinstance(key_value[1], str):
                    value_str = '\'{}\''.format(key_value[1])
                else:
                    value_str = '{}'.format(key_value[1])

                res.append('{}: {}'.format(key_str, value_str))
        key_value_pairs_str = '{}'.format(', '.join(res))
        return '{' + key_value_pairs_str + '}'

    def __repr__(self):
        """
        string representation of the class instances
        :return: string
        """
        return self.__str__()

    def keys(self):
        """
        get all keys as list
        :return: list
        """
        return self.__iter__()

    def values(self):
        """
        get all values as list
        :return: list
        """
        for key_var in self.__iterate_kv():
            yield key_var[1]

    def items(self):
        """
        get all k:v as list
        :return: list
        """
        return self.__iterate_kv()

    def get(self, key):
        """
        get value by key
        :param key: str
        :return: value or None if the key is not found
        """
        return self.get(key, None)
    
    def get(self, key, defaultValue):
        """
        get value by key. If key is not found returns the defaultValue
        :param key: str
        :return: value or default value if the key is not found
        """
        try:
            return self.__getitem__(key)
        except KeyError:
            if (defaultValue != None):
                return defaultValue
            else:
                return None


leastBirthYear = 3000                         # Finding the least birth year from the input provided
maxDeathYear = 0
birthYearArray = []
deathYearArray = []
recordCount = 0

def countBorn(dict, year):
    return dict.getitem(str(year))

def countDied(dict, year):
    return dict.getitem(str(year))

def maxPop(dict):
    max = -1
    for i in range(leastBirthYear,maxDeathYear+1):
        if dict.getitem(str(i)) > max:
            max = dict.getitem(str(i))
            maxPopYear = i
    return maxPopYear

def minPop(dict):
    min = dict.getitem(str(leastBirthYear))
    for i in range(leastBirthYear,maxDeathYear+1):
        if dict.getitem(str(i)) < min:
            min = dict.getitem(str(i))
            minPopYear = i
    return minPopYear

def maxBirth(dict):
    max = 0
    for i in birthYearArray:
        if dict.getitem(str(i)) > max:
            max = dict.getitem(str(i))
            maxBirthYear = i
    return maxBirthYear

def maxDeath(dict):
    max = 0
    for i in deathYearArray:
        if dict.getitem(str(i)) > max:
            max = dict.getitem(str(i))
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
                bornCount = countBorn(dict.getitem("birth"),bornInInput)
            if rowSplit[0] == 'diedIn':
                diedInInput = int(rowSplit[1].strip())
                diedCount = countDied(dict.getitem("death"),diedInInput)
            if rowSplit[0] == 'maxPopulation':
                maxPopYear = maxPop(dict.getitem("population")) 
                arrMaxYearCount = [ maxPopYear, dict.getitem("population").getitem(str(maxPopYear)) ]
            if rowSplit[0] == 'minPopulation':
                minPopYear = minPop(dict.getitem("population")) 
                arrMinYearCount = [ minPopYear, dict.getitem("population").getitem(str(minPopYear)) ]
            if rowSplit[0] == 'maxBirth':
                maxBirthYear = maxBirth(dict.getitem("birth")) 
                maxBirthArray = [ maxBirthYear, dict.getitem("birth").getitem(str(maxBirthYear)) ]
            if rowSplit[0] == 'maxDeath':
                maxDeathYear = maxDeath(dict.getitem("death")) 
                maxDeathArray = [ maxDeathYear, dict.getitem("death").getitem(str(maxDeathYear)) ]

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
            bYear = rowSplit[2].split('-')[2]
            bcount = birthCountDict.get(bYear, 0)
            birthCountDict[bYear] = bcount+1
            
            if rowSplit[2].split('-')[2] not in birthYearArray:
                birthYearArray.append(rowSplit[2].split('-')[2])

            if(rowSplit[3] != ''):
                dYear = rowSplit[3].split('-')[2]
                dcount = deathCountDict.get(dYear, 0)
                deathCountDict[dYear] = dcount+1
                
                if rowSplit[3].split('-')[2] not in deathYearArray:
                    deathYearArray.append(rowSplit[3].split('-')[2])
        
        maxPopDict = customDict(maxDeathYear - leastBirthYear)
        popInPrevYear = 0
        for i in range(leastBirthYear,maxDeathYear+1):
            popInThatYear = birthCountDict.getitem(str(i))-deathCountDict.getitem(str(i))
            popInThatYear += popInPrevYear
            maxPopDict.setitem(str(i), popInThatYear)
            popInPrevYear = popInThatYear
        dictExtracted = customDict(3)
        dictExtracted.setitem("birth", birthCountDict)
        dictExtracted.setitem("death", deathCountDict)
        dictExtracted.setitem("population", maxPopDict)
        f.close()
        return dictExtracted
        
    except Exception as e:
        print("Error while reading inputs")
        print(e)
        exit()

printOutput(readInputData())

def testfun():
    car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
    }

    if("color" in car):
        print(car.get('color'))
    else:
        car["color"] = "Red"

    print(car)

#testfun()