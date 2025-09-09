import csv
filename="raceData.csv"
fields=[]
rows=[]
columns=[]
def readFile():
    try:
        with open(filename, 'r') as file:
            csvreader= csv.reader(file)

            fields = next(csvreader)
            for row in csvreader:
                rows.append(row)
    except:
        print("error opening file or reading")
        quit()
readFile()

distances=rows[1]# turn the first row in to distances
print(distances)
#del distances[1]

del rows[0:2]#clear up the titles from the top
del rows[39:]#clear up the recoreds rows from the bottom

#remove the DNR and replace it with a emptey string
for row in rows:
    while "DNR" in row:
        row[row.index("DNR")]=''

    #del row[1]
    
    #print(row,"\n")


#turn the rows from min:sec:tenth format to just sec
paces=rows
for racer in paces:
    for i in range(1,14):
        try:
            min_str, sec_str = racer[i].split(':')
            try:
                sec_str, tenth_str = sec_str.split('.')
            except:
                pass
            racer[i]=60*int(min_str)+int(sec_str)
        except:
            racer[i]=''

#converts to paces
for racer in paces:
    for i in range(1,14):
        try:
            if distances[i]=='3K':

                racer[i]=int(racer[i])/1.86411
            elif distances[i]=='5K':
                racer[i]=int(racer[i])/3.10686
            elif distances[i]=='3 miles' or distances[i]=='3 mile':
                racer[i]=int(racer[i])/3
                
        except Exception as e:
            #print(i)
            #print(e)
            
            racer[i]=='null'
for racer in paces:
    while '' in racer:
        del racer[racer.index('')]
     


#print(paces)
def average(dataList):#used to take the avarege of the data part of the list
    try:
        return sum(dataList)/len(dataList)
    except:#returns if no data
        return 1200

def secToPace(seconds):
    if seconds==1200:
        return 'DNR'
    mins,secs =divmod(seconds*3.1,60)
    if secs<10:
        secs='0'+str(secs)
    else:
        secs=str(secs)
    secs=secs[:4]
    if mins<10:
        mins=str(mins)
        mins=mins[:1]
    else:
        mins=str(mins)
        mins=mins[:2]
    return mins+':'+secs


sortedlist = sorted(paces, key=lambda x: average(x[1:]))
numrunner=0
for runner in sortedlist:
    runner[0],blank=runner[0].split()
    while len(runner[0])<9:
        runner[0]=runner[0]+' '
    numrunner+=1
    if numrunner<10:
        strnum='0'+str(numrunner)
    else:
        strnum=str(numrunner)
    print(strnum,runner[0],"avarage 5K pace: ",secToPace(average(runner[1:])))
