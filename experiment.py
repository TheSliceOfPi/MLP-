import sys
import numpy as np
import mlp
import math

def getParameter(array,parameter):
    info = np.loadtxt('normalizeOutput.txt',delimiter=',')
    numDict={}
    foldDict={}
    for num in array:
        numDict[str(num)]=[0,10000,0]
        foldDict[str(num)]=[]
    for i in range(5):
        np.random.shuffle(info)
        ###START Split between test and valid sample###
        trainInputs=[]
        trainTargets=[]
        validInputs=[]
        validTargets=[]
        testInputs=[]
        testTargets=[]
        for sample in info[:len(info)//5]:
            new=[0,0] #1-N
            new[int(sample[-1])]=1
            validInputs.append(sample[:-1])
            validTargets.append(new)
            np.array(np)
        for sample in info[len(info)//5:2*(len(info)//5)]:
            new=[0,0]
            new[int(sample[-1])]=1
            np.array(np)
            testInputs.append(sample[:-1])
            testTargets.append(new)

        for sample in info[2*(len(info)//5):]:
            new=[0,0]
            new[int(sample[-1])]=1
            np.array(np)
            trainInputs.append(sample[:-1])
            trainTargets.append(new)
        trainInputs=np.array(trainInputs)
        trainTargets=np.array(trainTargets)
        trainInputs=np.array(trainInputs)
        trainTargets=np.array(trainTargets)
        testInputs=np.array(testInputs)
        testTargets=np.array(testTargets)
        ###END Split between test and valid sample###
        print("-------------- Loading fold",i+1,"---------------")
        for num in array:
            sectAvg=0
            for i in range(20):
                if(parameter=="nHidden"):
                    net = mlp.mlp(trainInputs,trainTargets,int(num))
                    err=net.earlystopping(trainInputs,trainTargets,validInputs,validTargets,0.3)
                elif(parameter=="momentum"):
                    net = mlp.mlp(trainInputs,trainTargets,10,momentum=float(num))
                    err=net.earlystopping(trainInputs,trainTargets,validInputs,validTargets,0.3)
                numDict[str(num)][0]=numDict[str(num)][0]+err
                numDict[str(num)].append(err)
                sectAvg=sectAvg+err
                if(err<numDict[str(num)][1]):
                    numDict[str(num)][1]=err
                if (err>numDict[str(num)][2]):
                    numDict[str(num)][2]=err
            foldDict[str(num)].append(sectAvg)
    print("----- Average Means of 5-fold------")
    for case in foldDict:
        print("----"+case+" --------")
        acc=0
        for i in foldDict[case]:
            acc=acc+i
            print(i/20)
        print("Overall Mean Error ",acc/(20*5))
    print("---- Stats of each n tested----")
    for num in numDict:
          if (parameter=="nHidden"):
              print("---- Size "+ num +" hidden layer----")
          elif(parameter=="momentum"):
              print("----- Momentum of "+num+" ----------")
          mAvg=numDict[num][0]/(len(numDict[num])-3)
          print("Mean Error: ",mAvg)
          sd=0.0
          for i in range(3,len(numDict[num])):
              sd=sd+((numDict[num][i]-mAvg)**2)
          sd=sd/(len(numDict[num])-4)
          sd=(sd**(1/2))
          print("Standard Deviation: ",sd)
          print("Max Error: ",numDict[num][2])
          print("Min Error: ",numDict[num][1])

                
                
        
            

def getMatrix(nHidden,momentum):
    info = np.loadtxt('normalizeOutput.txt',delimiter=',')
    np.random.shuffle(info)
    ###START Split between test and valid sample###
    trainInputs=[]
    trainTargets=[]
    validInputs=[]
    validTargets=[]
    testInputs=[]
    testTargets=[]
    for sample in info[:len(info)//5]:
        new=[0,0]
        new[int(sample[-1])]=1
        np.array(new)
        validInputs.append(sample[:-1])
        validTargets.append(new)
        
    for sample in info[len(info)//5:2*(len(info)//5)]:
        new=[0,0]
        new[int(sample[-1])]=1
        np.array(new)
        testInputs.append(sample[:-1])
        testTargets.append(new)
        
    for sample in info[2*(len(info)//5):]:
        new=[0,0]
        new[int(sample[-1])]=1
        np.array(new)
        trainInputs.append(sample[:-1])
        trainTargets.append(new)
    ###END Split between test and valid sample###
    trainInputs=np.array(trainInputs)
    trainTargets=np.array(trainTargets)
    trainInputs=np.array(trainInputs)
    trainTargets=np.array(trainTargets)
    testInputs=np.array(testInputs)
    testTargets=np.array(testTargets)

    net = mlp.mlp(trainInputs,trainTargets,nHidden,momentum=momentum)
    net.earlystopping(trainInputs,trainTargets,validInputs,validTargets,0.3)
    net.confmat(testInputs,testTargets)
            
    
def main():
    #getParameter([1,2,3,5,10,25,50],"nHidden")
    #getParameter([0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1],"momentum")
    getMatrix(10,0.7)

main()
