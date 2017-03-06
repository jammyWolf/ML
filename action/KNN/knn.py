 # -*- coding: utf-8 -*-
from numpy import *
import matplotlib
import matplotlib.pyplot as plt
import operator
import sys, os

def createDataSet():
    group = array([[1.0,1.1],[1.0,1.0],[0,0],[0,0.1]])
    labels = ['A', 'A', 'B', 'B']
    return group, labels
    
def classify0(inX, dataSet, labels, k):
    dataSetSize = dataSet.shape[0]
    diffMat = tile(inX, (dataSetSize, 1)) - dataSet
    sqDiffMat = diffMat**2  #算出距离平方
    sqDistances = sqDiffMat.sum(axis=1) #按行求和
    distances = sqDistances**0.5
    sortedDistIndicies = distances.argsort()
    classCount = {}
    for i in range(k):
        voteIlabel = labels[sortedDistIndicies[i]]
        classCount[voteIlabel] = classCount.get(voteIlabel, 0) + 1
    sortedClassCount = sorted(classCount.iteritems(),key = operator.itemgetter(1), reverse=True)
    # print(sortedClassCount)
    return sortedClassCount[0][0]
    
def file2matrix(filename, isLabelString):
    fr = open(filename)
    numberofLines = len(fr.readlines())
    returnMat = zeros((numberofLines, 3))
    classLabelVector = []
    fr = open(filename)
    index = 0
    if not isLabelString:
        for line in fr.readlines():
            line = line.strip()
            listFromeLine = line.split('\t')
            returnMat[index, :] = listFromeLine[0:3]
            classLabelVector.append(int(listFromeLine[-1]))
            index += 1
    else:
        for line in fr.readlines():
            line = line.strip()
            listFromeLine = line.split('\t')
            returnMat[index, :] = listFromeLine[0:3]
            classLabelVector.append(listFromeLine[-1])
            index += 1    
    return returnMat, classLabelVector
    
def cur_dir():
    path = sys.path[0]
    if os.path.isdir(path):
        return path
    elif os.path.isfile(path):
        return os.path.dirname(path)

def autoNorm(dataSet):
    minVals = dataSet.min(0)
    maxVals = dataSet.max(0)
    ranges = maxVals - minVals
    normDataSet = zeros(shape(dataSet))
    m = dataSet.shape[0]
    normDataSet = dataSet - tile(minVals, (m, 1))
    normDataSet = normDataSet/tile(ranges, (m, 1))
    return normDataSet, ranges, minVals
    
def datingClassTest():
    hoRatio = 0.10
    filename = cur_dir() + "/datingTestSet.txt"
    datingDateMat, datingLabels = file2matrix(filename2, True)
    m = datingDateMat.shape[0]
    numTestVecs = int(m*hoRatio)
    errorCount = 0.0
    for i in range(numTestVecs):
        classifierResult = classify0()
    
    
        
def main():
    # vote = classify0([0,0], group, labels, 3)
    filename = cur_dir() + "/datingTestSet2.txt"
    mat, vector = file2matrix(filename, False)
    fig = plt.figure()
    ax = fig.add_subplot(111)
    # ax.scatter(mat[:, 1], mat[:,2], marker = 'o')
    # ax.scatter(mat2[:, 1], mat2[:,2], 15.0*array(vector2), 15.0*array(vector2))
    ax.scatter(mat[:, 0], mat[:,1], 15.0*array(vector), 15.0*array(vector))
    a, b, c = autoNorm(mat)
    # print(a, b, c)
    # plt.show()
    # vote = classify0()
    
if __name__ == "__main__":
    main()
