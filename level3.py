#!/usr/bin/env python

from itertools import combinations


def readfile(filename):
    f = open(filename, 'r')
    l = list((int(i) for i in (f.readline().split(','))))
    return l


def getSubsets(elements):
    subsets = []

    for j in range(2, len(elements)):
        combis = combinations(elements, j)
        for combi in combis:
            sum_of_elements = reduce(lambda x, y: x + y, combi)
            if sum_of_elements in elements:
                print sum_of_elements, combi
                subsets.append({sum_of_elements: combi})

    return subsets


def main():
    numlist = readfile("numbers.csv")
    subsets = getSubsets(numlist)
    print ("Answer: %d sets" % len(subsets))


if __name__ == "__main__":
    main()
