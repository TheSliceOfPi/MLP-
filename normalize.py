import sys
import numpy as np

def main():
    inputFileName=sys.argv[1]
    inputFile=open(inputFileName,"r")
    outputFileName=sys.argv[2]
    outputFile=open(outputFileName,"w+")
    dataDict={}
    rangeDict={}
    line=inputFile.readline()
    featSize=len(line.split(","))
    for i in range(featSize):
        dataDict[str(i)]=[]
        rangeDict[str(i)]=[0,0]
    while (line):
        line=line.split(",")
        for x in range(len(line)):
            dataDict[str(x)].append(float(line[x]))
            if(float(line[x])<rangeDict[str(x)][0]):
                rangeDict[str(x)][0]=float(line[x])
            elif (float(line[x])>rangeDict[str(x)][1] and float(line[x])<=50):
                rangeDict[str(x)][1]=float(line[x])
            elif(float(line[x])>50 and rangeDict[str(x)][1]<50):
                rangeDict[str(x)][1]=50
        line=inputFile.readline()
    for feat in rangeDict:
        for i in range(len(dataDict[feat])):
            if(dataDict[feat][i]<=50):
                dataDict[feat][i]=(dataDict[feat][i]-rangeDict[feat][0])/(rangeDict[feat][1]-rangeDict[feat][0]) #normalizing
            else:
                dataDict[feat][i]=1
    for i in range(len(dataDict["0"])):
        for j in range(len(rangeDict)):
            outputFile.write(str(dataDict[str(j)][i]))
            if(j !=len(rangeDict)-1):
                outputFile.write(",")
            else:
                outputFile.write("\n")
    inputFile.close()
    outputFile.close()

main()
