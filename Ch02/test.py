#! /usr/bin/env python
# -*- coding: utf-8 -*-

import kNN

if __name__ == '__main__':
    data = kNN.createDataSet()
    print data

    # matrix = kNN.file2matrix('datingTestSet2.txt')
    # print matrix
    # kNN.datingClassTest()
    kNN.handwritingClassTest()