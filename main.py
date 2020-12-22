class dictPerson:
    def __init__(self, id, name, dob, dod):
        self.id = id
        self.name = name
        self.dob = dob
        self.dod = dod

    def __repr__(self):
        return self.id
        
class yearBirth:
    def __init__(self, year):
        self.year = year
        self.birthCount = 1

class yearDeath:
    def __init__(self, year):
        self.year = year
        self.deathCount = 1
maxDeathYear = 10
leastBirthYear = 2100

def maxPop(arrayOfDictPerson):
    print(leastBirthYear)
    print(maxDeathYear)
    population_changes = [0 for _ in range(leastBirthYear, maxDeathYear+1)]
    print(len(population_changes))
    for person in arrayOfDictPerson:
        population_changes[int(person.dob.split('-')[2]) - leastBirthYear] += 1
        if person.dod != '':
            population_changes[int(person.dod.split('-')[2]) - leastBirthYear] -= 1
    max_population = 0
    max_population_index = 0
    population = 0
    print(population_changes)
    for index, population_change in enumerate(population_changes):
        population += population_change
        if population > max_population:
            max_population = population
            max_population_index = index
    return [leastBirthYear + max_population_index,max_population]



def minPop(arrayOfDictPerson):
    print(leastBirthYear)
    print(maxDeathYear)
    population_changes = [0 for _ in range(leastBirthYear, maxDeathYear+1)]
    print(len(population_changes))
    for person in arrayOfDictPerson:
        population_changes[int(person.dob.split('-')[2]) - leastBirthYear] += 1
        if person.dod != '':
            population_changes[int(person.dod.split('-')[2]) - leastBirthYear] -= 1
    min_population = 1000                                               #need to variablize this-pending
    min_population_index = 0
    population = 0
    for index, population_change in enumerate(population_changes):
        population += population_change
        if population < min_population:
            min_population = population
            min_population_index = index
    return [leastBirthYear + min_population_index,min_population]


def countDied(arrayOfDictPerson, year):
    count = 0
    for person in arrayOfDictPerson:
        if person.dod != '':
            if int(person.dod.split('-')[2]) == year:
                count+=1
    return count

def countBorn(arrayOfDictPerson, year):
    count = 0
    for person in arrayOfDictPerson:
        if person.dob != '':
            if int(person.dob.split('-')[2]) == year:
                count+=1
    return count

def maxBirth(arrayOfBirth):
    maxBirth = 0
    maxBirthYear = 0
    for birthyear in arrayOfBirth:
        if int(birthyear.birthCount) > maxBirth:
            maxBirth = birthyear.birthCount
            maxBirthYear = birthyear.year
    return [maxBirthYear, maxBirth]

def maxDeath(arrayOfDeath):
    maxDeath = 0
    maxDeathYear = 0
    for deathyear in arrayOfDeath:
        if int(deathyear.deathCount) > maxDeath:
            maxDeath = deathyear.deathCount
            maxDeathYear = deathyear.year
    return [maxDeathYear, maxDeath]



def printOutput(dict):
    arrayOfDictPerson = dict[0]
    arrayOfBirth = dict[1]
    arrayOfDeath = dict[2]
    recordCount = dict[3]
    readPrompts = open('promptsPS21.txt','r')
    for line in readPrompts:
        line = line.strip()
        rowSplit = line.split(':')
        if rowSplit[0] == 'bornIn':
            bornInInput = int(rowSplit[1].strip())
            bornCount = countBorn(arrayOfDictPerson,bornInInput)
        if rowSplit[0] == 'diedIn':
            diedInInput = int(rowSplit[1].strip())
            diedCount = countDied(arrayOfDictPerson,diedInInput)
        if rowSplit[0] == 'maxPopulation':
            arrMaxYearCount = maxPop(arrayOfDictPerson)
        if rowSplit[0] == 'minPopulation':
            arrMinYearCount = minPop(arrayOfDictPerson)
        if rowSplit[0] == 'maxBirth':
            maxBirthYear = maxBirth(arrayOfBirth)
        if rowSplit[0] == 'maxDeath':
            maxDeathYear = maxDeath(arrayOfDeath)

    writeOutput = open("outputPS21.txt", "w")   #w will create file if it does not exist
    recordsCaptured = str(recordCount) + " records captured\n"   #need to complete 
    writeOutput.write(recordsCaptured)
    bornInText = "No. of people born in "+ str(bornInInput) +": "+ str(bornCount)+"\n"
    writeOutput.write(bornInText)
    diedInText = "No. of people died in "+ str(diedInInput) +": "+ str(diedCount)+"\n"
    writeOutput.write(diedInText)
    maxPopText = "Maximum population was in year "+ str(arrMaxYearCount[0])+" with "+str(arrMaxYearCount[1])+" people alive.\n"
    writeOutput.write(maxPopText)
    minPopText = "Minimum population was in year "+ str(arrMinYearCount[0])+" with "+str(arrMinYearCount[1])+" people alive.\n"
    writeOutput.write(minPopText)
    maxBirthText = "Maximum births were in year "+ str(maxBirthYear[0])+" with "+str(maxBirthYear[1])+" people born.\n"
    writeOutput.write(maxBirthText)
    maxDeathText = "Maximum deaths were in year "+ str(maxDeathYear[0])+" with "+str(maxDeathYear[1])+" people dead.\n"
    writeOutput.write(maxDeathText)
    writeOutput.close()

def readInputData():
    f = open('inputPS21.txt','r')
    recordCount = 0
    arrayOfDictPerson = []
    arrayOfBirth = []
    arrayOfDeath = []
    global leastBirthYear 
    leastBirthYear = 2100
    global maxDeathYear
    maxDeathYear = 0
    for line in f:
        recordCount+=1
        line = line.strip()
        rowSplit = line.split(',')
        print(rowSplit[2].split('-')[2])
        person = dictPerson(rowSplit[0],rowSplit[1],rowSplit[2],rowSplit[3])
        arrayOfDictPerson.append(person)
        birthFlag = 0
        for birthObj in arrayOfBirth:
            if birthObj.year == rowSplit[2].split('-')[2]:
                birthObj.birthCount += 1
                birthFlag = 1
                print(leastBirthYear)

                if int(birthObj.year) < int(leastBirthYear):
                    leastBirthYear = int(birthObj.year)
        
        if birthFlag == 0:
            yB = yearBirth(rowSplit[2].split('-')[2])
            arrayOfBirth.append(yB)

        if(rowSplit[3] != ''):
            deathFlag = 0
            dodYear = rowSplit[3].split('-')[2]
            for deathObj in arrayOfDeath:
                if deathObj.year == dodYear:
                    deathObj.deathCount += 1
                    deathFlag = 1
                    if int(dodYear) > int(maxDeathYear):
                        maxDeathYear = int(dodYear)
            
            if deathFlag == 0:
                yD = yearDeath(dodYear)  #split is used to fetch only the year from the date
                arrayOfDeath.append(yD)
    
    return [arrayOfDictPerson, arrayOfBirth, arrayOfDeath, recordCount ]


printOutput(readInputData())
