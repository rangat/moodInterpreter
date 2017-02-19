
def makeArray():
    file = open("keywordsList.txt", "r")
    keywordArr = []
    for line in file:
        emotionKeyword = line[:-1]
        keywordArr.append(emotionKeyword)
    print("Keyword list : ", keywordArr)
    return

makeArray()