

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


# Take input
checker = input()

# Check to see if it's basic English
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


print(f"English: {isEnglish}, Basic:{isBasic}")



