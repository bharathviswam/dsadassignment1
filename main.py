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

def readInputData():
    f = open('inputPS21.txt','r')
    arrayOfDictPerson = []
    arrayOfBirth = []
    arrayOfDeath = []
    for line in f:
        line=line.strip()
        rowSplit = line.split(',')
        person = dictPerson(rowSplit[0],rowSplit[1],rowSplit[2],rowSplit[3])
        arrayOfDictPerson.append(person)
        birthFlag = 0
        for birthObj in arrayOfBirth:
            if birthObj.year == rowSplit[2].split('-')[2]:
                birthObj.birthCount += 1
                birthFlag = 1
        
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
            
            if deathFlag == 0:
                yD = yearDeath(dodYear)  #split is used to fetch only the year from the date
                arrayOfDeath.append(yD)

        print(line)
    return [arrayOfDictPerson, arrayOfBirth, arrayOfDeath ]

vals = readInputData()

for i in vals[0]:
    print(i.__dict__)
    #print(repr(i))


for i in vals[1]:
    print(i.year)
    print(i.birthCount)


for i in vals[2]:
    print(i.year)
    print(i.deathCount)
