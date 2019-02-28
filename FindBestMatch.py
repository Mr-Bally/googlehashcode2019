import sys
from photo import Photo

def findBestMatch(listOfElements, toMatch):
    currentBest = listOfElements[0]
    bestTotal = -1
    toMatchTags = toMatch.tags
    for element in listOfElements:
        currentTotal = 0
        for tag in element.tags:
            if tag in toMatchTags:
                currentTotal+= 1
        if currentTotal > bestTotal:
            currentBest = element
    return element
