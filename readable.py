# Check to see if it's basic English
def inputyn(item):
    acceptableResponse = False
    response = ""
    while(not acceptableResponse):
        response = input(f"{item}: ")
        if response.lower() == 'y':
            acceptableResponse = True
            return True
        elif response.lower() == 'n':
            acceptableResponse = True
            return False
        else:
            print(f"That is not an acceptable response, do you know this word? (Y/n):")

    return False

def textCleaner(paragraph):
    NON_LETTER_CHARACTERS = "!@#$%^&*()[]{}_+<>?:.,;/0123456789"
    cleanParagraph_text = ""
    cleanParagraph1 = []
    cleanParagraph2 = []
    finalParagraph = []

    for a in paragraph:
        if a not in NON_LETTER_CHARACTERS:
            cleanParagraph_text += a
        else:
            cleanParagraph_text += " "

    cleanParagraph1 = cleanParagraph_text.split()

    for i in range(len(cleanParagraph1)):
        cleanParagraph1[i] = cleanParagraph1[i].lower()

    for i in cleanParagraph1:
        if i not in cleanParagraph2:
            cleanParagraph2.append(i)

    cleanParagraph2.sort()
    finalParagraph = cleanParagraph2

    return finalParagraph


def basicEnglishChecker(checker):
    isBasic = False

    try:
        basicWords.index(checker.lower())
        isBasic = True
    except ValueError:
        isBasic = False

    isEnglish = False

    if isBasic:
        isEnglish = True
    else:
        try:
            allEnglish.index(checker.lower())
            isEnglish = True
        except ValueError:
            isEnglish = False
    return isEnglish, isBasic

# The purpose of this section is to import a list of basic English words, clean it, and sort it.
basicWords_file = open("/home/atahmid/PycharmProjects/readable/basic_wordlist", "r")
basicWords = basicWords_file.readlines()

for i in range(len(basicWords)):
    basicWords[i] = basicWords[i].lower()
    basicWords[i] = basicWords[i].rstrip("\n")
basicWords.sort()

# Now we want to do the same with all words in English.

allEnglish_file = open("/home/atahmid/PycharmProjects/readable/all_english", "r")
allEnglish = allEnglish_file.readlines()

for i in range(len(allEnglish)):
    allEnglish[i] = allEnglish[i].lower()
    allEnglish[i] = allEnglish[i].rstrip("\n")
allEnglish.sort()

# Now we import the article
article_file = open("/home/atahmid/PycharmProjects/readable/article", "r")
article_whole = article_file.read()

article = textCleaner(article_whole)

isEnglishWord = False
isBasicWord = False

easyWords = []
complexWordsCandidates = []
complexWords = []

for a in article:
    isEnglishWord, isBasicWord = basicEnglishChecker(a)
    if isBasicWord:
        easyWords.append(a)
    elif isEnglishWord:
        complexWordsCandidates.append(a)
    else:
        pass

complexWordsCandidates.sort()

print("For each of the following words, indicate, do you know what this word means? (Y/n)")
for item in complexWordsCandidates:
    wordKnown = inputyn(item)
    if wordKnown:
        easyWords.append(item)
    else:
        complexWords.append(item)



easeRatio = float(len(easyWords))/(float(len(complexWords)) + float(len(easyWords)))
easeRatio = round(easeRatio, 2)

print(f"The ease ratio is {easeRatio}")



