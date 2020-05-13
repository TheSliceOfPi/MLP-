import sys


def main():
    inputFileName=sys.argv[1]
    inputFile=open(inputFileName,"r")
    outputFileName=sys.argv[2]
    outputFile=open(outputFileName,"w+")
    line=inputFile.readline()
    while ("@attribute" not in line):
        line=inputFile.readline()
    while("@data" not in line):
        if(len(line.split())>0 and line.split()[-1]!="numeric"):
            line=line.split()
            outcome=line[-1].replace("{","")
            outcome=outcome.replace("}","")
            outcome=outcome.split(",")
            outcome[0],outcome[1]=outcome[1],outcome[0] #That way Disease is 1
        line=inputFile.readline()
    line=inputFile.readline() #Read the @data line
    while(line):
        feats=line.split(",")
        feats[-1]=outcome.index(feats[-1].replace("\n",""))
        for i in range(len(feats)):
            outputFile.write(str(feats[i]))
            if(i<len(feats)-1):
                outputFile.write(",")
            else:
                outputFile.write("\n")
        line=inputFile.readline()
    inputFile.close()
    outputFile.close()

main()
