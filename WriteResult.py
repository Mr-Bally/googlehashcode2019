def writeResults(listToPrint):
    for elem in listToPrint:
        finalString = finalString + elem + "\n"
        
    with open("./Data/results.txt", 'w') as f:
        f.writelines(finalString)
        f.close()
