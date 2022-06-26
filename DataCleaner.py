import csv
import os
from re import L

def checkIfNoneEmpty(l):
    marker = ''
    retVal = any(marker == item for item in l)
    return not retVal


def processCsvFile(inCsv, outCsv):
    lol = []

    inFile = open(inCsv,'r')
    inContent = csv.reader(inFile)

    for row in inContent:
        if checkIfNoneEmpty(row):
           lol.append(row) 

    outFile = open(outCsv,'w',newline="")
    with outFile:
        write = csv.writer(outFile)
        write.writerows(lol)

    inFile.close()
    outFile.close()

def main():
    inDrive = "C:\\"
    inPath = os.path.join(inDrive, "Users", "sumad", "OneDrive - San José Unified School District", "Documents", "WaterQualityData.csv")

    outDrive = "C:\\"
    outPath = os.path.join(outDrive, "Users", "sumad", "OneDrive - San José Unified School District", "Documents", "WaterQualityDataProcessed.csv")

    processCsvFile(inPath, outPath)

main()