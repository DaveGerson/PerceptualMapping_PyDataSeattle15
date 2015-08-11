# -*- coding: utf-8 -*-
__author__ = 'gerson64'

from stemming.porter2 import stem
from nltk.corpus import stopwords
import sys
import string
import scipy
import numpy

reload(sys)
sys.setdefaultencoding('utf8')

stemStopwords = map(lambda x: stem(x).strip().lower(), stopwords.words('english'))


def unique(inList):
    return list(set(inList))

def dedupe_files(infilename, outfilename):
    lines_seen = set()  # holds lines already seen
    outfile = open(outfilename, "w")
    for line in open(infilename, "r"):
        if line not in lines_seen:  # not a duplicate
            outfile.write(line)
            lines_seen.add(line)
    outfile.close()


def stem_files(infilename, outfilename):
    outfile = open(outfilename, "w")
    for line in open(infilename, "r"):
        line_array = line.translate(None, string.punctuation).split(" ")
        if line_array > 0:
            for i in range(len(line_array )):
                line_array[i] = stem(line_array[i].strip()).lower()
                line = " ".join(line_array) + "\n"
        outfile.write(line)
    outfile.close()

def lineParse(line):
    inList = line.translate(None, string.punctuation).split(" ")
    distinctWords = set()
    for x in inList:
        stemmed = stem(x.strip()).lower()
        if stemmed not in distinctWords and len(stemmed) > 3 :
            distinctWords.add(stemmed)
    filtered = [w for w in list(distinctWords) if not w in stemStopwords]
    return filtered



def fileParse(infilename):
    lineList = list()
    for line in open(infilename, "r"):
        lineList.append(lineParse(line))
    return lineList

def parseByList(lineList, restList, filterList):
    out = dict()
    for i in range(len(restList)):
        restList[i] = stem(restList[i].strip()).lower().replace("@", "")
    for i in restList:
        out[i] = list()
    filterList = [elem for elem in filterList if elem not in restList]
    for i in lineList:
        intersect = set(i).intersection(restList)
        if len(intersect) > 0:
            for j in intersect:
                words = [elem for elem in i if elem in filterList]
                out[j].append(words)
    for i in restList:
        x = out[i]
        #out[i] = [val for sublist in x for val in sublist]
    return out;


