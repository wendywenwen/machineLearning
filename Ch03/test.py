#! /usr/bin/env python
# -*- coding: utf-8 -*-

import trees

if __name__ == '__main__':
    data = trees.createDataSet1()
    # print data
    dataSet = data[0]
    lables = data[1]
    print dataSet
    feature = trees.chooseBestFeatureToSplit(dataSet)
    feature1 = trees.chooseBestFeatureToSplit1(dataSet)
    print feature
    print feature1
    mytree = trees.createTree(dataSet, lables)
    print mytree

    print trees.splitDataSet(dataSet,0,1)

    featLabels = ['outlook', 'temperature', 'humidity', 'windy']
    testVec = [0, 1, 0, 0]
    print trees.classify(mytree, featLabels, testVec)
