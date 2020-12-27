class customDict(object):
    """
    custom implementation for dictionary
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
    
    def get(self, key, defaultValue = None):
        """
        get value by key. If key is not found returns the defaultValue
        :param key: str
        :return: value or default value if the key is not found
        """
        try:
            return self.__getitem__(key)
        except KeyError:
            return defaultValue


leastBirthYear = 3000                         # Finding the least birth year from the input provided
maxDeathYear = 0
recordCount = 0

def countBorn(dict, year):
    return dict.get(str(year))

def countDied(dict, year):
    return dict.get(str(year))

def maxPop(dict):
    max = -1
    for i in range(leastBirthYear,maxDeathYear+1):
        if dict.get(str(i)) > max:
            max = dict.get(str(i))
            maxPopYear = i
    return maxPopYear

def minPop(dict):
    min = dict.get(str(leastBirthYear))
    for i in range(leastBirthYear,maxDeathYear+1):
        if dict.get(str(i)) < min:
            min = dict.get(str(i))
            minPopYear = i
    return minPopYear

def maxBirth(dict):
    max = 0
    for year in dict:
        if dict.get(year) > max:
            max = dict.get(year)
            maxBirthYear = year
    return maxBirthYear

def maxDeath(dict):
    max = 0
    for year in dict:
        if dict.get(year) > max:
            max = dict.get(year)
            maxDeathYear = year
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
                bornCount = countBorn(dict.get("birth"),bornInInput)
            if rowSplit[0] == 'diedIn':
                diedInInput = int(rowSplit[1].strip())
                diedCount = countDied(dict.get("death"),diedInInput)
            if rowSplit[0] == 'maxPopulation':
                maxPopYear = maxPop(dict.get("population")) 
                arrMaxYearCount = [ maxPopYear, dict.get("population").get(str(maxPopYear)) ]
            if rowSplit[0] == 'minPopulation':
                minPopYear = minPop(dict.get("population")) 
                arrMinYearCount = [ minPopYear, dict.get("population").get(str(minPopYear)) ]
            if rowSplit[0] == 'maxBirth':
                maxBirthYear = maxBirth(dict.get("birth")) 
                maxBirthArray = [ maxBirthYear, dict.get("birth").get(str(maxBirthYear)) ]
            if rowSplit[0] == 'maxDeath':
                maxDeathYear = maxDeath(dict.get("death")) 
                maxDeathArray = [ maxDeathYear, dict.get("death").get(str(maxDeathYear)) ]

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
    except Exception as e:
        print("Error while writing output")
        print(e)
        readPrompts.close()
        exit()

def readInputData():
    try:
        try:
            f = open('inputPS21.txt','r')
        except:
            print("File inputPS21.txt doesnot exist")
        global leastBirthYear , maxDeathYear, recordCount
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
        # Read the file from the beginning
        f.seek(0)                                                               
        for line in f:
            line = line.strip()
            rowSplit = line.split(',')
            bYear = rowSplit[2].split('-')[2]
            # getting birth count from dictionary. If key not found default value of 0 is taken
            bcount = birthCountDict.get(bYear, 0)
            birthCountDict[bYear] = bcount+1

            if(rowSplit[3] != ''):
                dYear = rowSplit[3].split('-')[2]
                dcount = deathCountDict.get(dYear, 0)
                deathCountDict[dYear] = dcount+1
        
        populationDictinary = customDict(maxDeathYear - leastBirthYear)
        popInPrevYear = 0
        for i in range(leastBirthYear,maxDeathYear+1):
            popInThatYear = birthCountDict.get(str(i),0)-deathCountDict.get(str(i),0)
            popInThatYear += popInPrevYear
            populationDictinary[str(i)] = popInThatYear
            popInPrevYear = popInThatYear
        
        dictExtracted = customDict(3)
        dictExtracted["birth"] = birthCountDict
        dictExtracted["death"] = deathCountDict
        dictExtracted["population"] = populationDictinary
    
        f.close()
        return dictExtracted
        
    except Exception as e:
        print("Error while reading input data")
        print(e)
        exit()

printOutput(readInputData())