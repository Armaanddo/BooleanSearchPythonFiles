print("Boolean search")
loop = True
choice = -1
doc = []
file = ""


def searchNot(firstWord2, booleanSecond, secondWord, booleanThird, thirdWord,
              foundFirstTerm, foundSecondTerm, foundThirdTerm, doc):
    if booleanSecond == "and" and booleanThird == "and":
        for f in doc:
            if f.find(firstWord2) > -1:
                foundFirstTerm = 1
            if f.find(secondWord) > -1:
                foundSecondTerm = 1

            if f.find(thirdWord) > -1:
                foundThirdTerm = 1

        if (foundFirstTerm == 0 and foundSecondTerm == 1) and foundThirdTerm == 1:
            print("Boolean search valid: True!")
            print(doc)
        else:
            print("Boolean search is not valid!")

    elif booleanSecond == "and" and booleanThird == "or":
        foundFirstTerm: int = 0
        foundSecondTerm: int = 0
        foundThirdTerm: int = 0
        for f in doc:
            if f.find(firstWord2) == -1:
                foundFirstTerm = 0

            if f.find(secondWord) > -1:
                foundSecondTerm = 1

            if f.find(thirdWord) > -1:
                foundThirdTerm = 1
        if (foundFirstTerm == 0 and foundSecondTerm >= 0) or foundThirdTerm >= 0:
            print("Boolean search valid: True!")
            print(doc)
        else:
            print("Boolean search is not valid!")

    elif booleanSecond == "or" and booleanThird == "or":
        foundFirstTerm: int = 0
        foundSecondTerm: int = 0
        foundThirdTerm: int = 0
        for f in doc:
            if f.find(firstWord2) > -1:
                foundFirstTerm = 1
                print(doc)
            elif f.find(secondWord) > -1:
                foundSecondTerm = 1
                print(doc)
            elif f.find(thirdWord) > -1:
                print(doc)
                foundThirdTerm = 1
        ##if (foundFirstTerm == 1 or foundSecondTerm == 1) or foundThirdTerm == 1:
          ##  print("Boolean search valid!")
            ##print(doc)
        ##elif (foundFirstTerm == 0 or foundSecondTerm == 1) or foundThirdTerm == 0:
        ##    print("Boolean search valid!")
          ##  print(doc)
        ##elif (foundFirstTerm == 0 or foundSecondTerm == 1) or foundThirdTerm == 0:
          ##  print("Boolean search valid: True!")
            ##print(doc)
        ##else:
          ##  print("")

    elif booleanSecond == "or" and booleanThird == "and":
        cont=0
        foundFirstTerm: int = 0
        foundSecondTerm: int = 0
        foundThirdTerm: int = 0
        for f in doc:
            if f.find(firstWord2) > -1:
                foundFirstTerm = 1

            elif f.find(secondWord) > -1:
                foundSecondTerm = 1

            elif f.find(thirdWord) > -1:
                foundThirdTerm = 1

        if (foundFirstTerm == 1 or foundSecondTerm == 1) and foundThirdTerm == 1:
            print(doc)
        elif (foundFirstTerm == 1 or foundSecondTerm == 0) and foundThirdTerm == 1:
            print("Boolean search valid!")
            print(doc)
        elif (foundFirstTerm == 0 or foundSecondTerm == 0) and foundThirdTerm == 1:
            print("")
        else:
            print("")

    elif booleanSecond == "and" and booleanThird == "not":
        foundFirstTerm: int = 0
        foundSecondTerm: int = 0
        foundThirdTerm: int = 0
        for f in doc:
            if f.find(firstWord2) == -1:
                foundFirstTerm = 0
            a = f.find(secondWord)
            if a > -1:
                foundSecondTerm = 1
            if f.find(thirdWord) > -1:
                foundThirdTerm = 1
        if (foundFirstTerm == 0 and foundSecondTerm == 1) and foundThirdTerm == 0:
            print("Boolean search valid: True!")
            print(doc)
        else:
            print("Boolean search is not valid!")

    elif booleanSecond == "not" and booleanThird == "and":
        foundFirstTerm: int = 0
        foundSecondTerm: int = 0
        foundThirdTerm: int = 0
        for f in doc:
            if f.find(firstWord2) > -1:
                foundFirstTerm = 1

            if f.find(secondWord) > -1:
                foundSecondTerm = 1

            if f.find(thirdWord) > -1:
                foundThirdTerm = 1
        if (foundFirstTerm == 0 and foundSecondTerm == 0) and foundThirdTerm == 1:
            print("Boolean search valid: True!")
            print(doc)
        else:
            print("Boolean search is not valid!")

    elif booleanSecond == "or" and booleanThird == "not":
        foundFirstTerm: int = 0
        foundSecondTerm: int = 0
        foundThirdTerm: int = 0
        for f in doc:
            if f.find(firstWord2) > -1:
                foundFirstTerm = 1

            if f.find(secondWord) > -1:
                foundSecondTerm = 1

            if f.find(thirdWord) > -1:
                foundThirdTerm = 1
        if (foundFirstTerm == 0 or foundSecondTerm == 1) and foundThirdTerm == 0:
            print("Boolean search valid: True!")
            print(doc)
        else:
            print("Boolean search is not valid!")

    elif booleanSecond == "not" and booleanThird == "not":
        foundFirstTerm: int = 0
        foundSecondTerm: int = 0
        foundThirdTerm: int = 0
        for f in doc:
            a: int = f.find(firstWord2)
            if a > -1:
                foundFirstTerm = 1
            if f.find(secondWord) > -1:
                foundSecondTerm = 1
            if f.find(thirdWord) > -1:
                foundThirdTerm = 1
        if (foundFirstTerm == 0 and foundSecondTerm == 0) and foundThirdTerm == 0:
            print("Boolean search valid: True!")
            print(doc)
        else:
            print("Boolean search is not valid!")


def searchwithoutnot(firstWord, booleanFirst, secondWord, booleanSecond, thirdWord, doc):
    foundFirstTerm: int = 0
    foundSecondTerm: int = 0
    foundThirdTerm: int = 0
    if booleanFirst == "and" and booleanSecond == "and":

        for f in doc:
            if f.find(firstWord) > -1:
                foundFirstTerm = 1

            if f.find(secondWord) > -1:
                foundSecondTerm = 1

            if f.find(thirdWord) > -1:
                foundThirdTerm = 1

        if (foundFirstTerm == 1 and foundSecondTerm == 1) and foundThirdTerm == 1:
            print("Boolean search valid: True!")
            print(doc)
        else:
            print("Boolean search is not valid!")

    elif booleanFirst == "and" and booleanSecond == "or":
        foundFirstTerm: int = 0
        foundSecondTerm: int = 0
        foundThirdTerm: int = 0
        for f in doc:
            if f.find(firstWord) > -1:
                foundFirstTerm = 1

            if f.find(secondWord) > -1:
                foundSecondTerm = 1

            if f.find(thirdWord) > -1:
                foundThirdTerm = 1
        if (foundFirstTerm == 1 and foundSecondTerm == 1) or foundThirdTerm == 1:
            print("Boolean search valid: True!")
            print(doc)


    elif booleanFirst == "or" and booleanSecond == "or":
        foundFirstTerm: int = 0
        foundSecondTerm: int = 0
        foundThirdTerm: int = 0
        for f in doc:
            if f.find(firstWord) > -1:
                foundFirstTerm = 1

            if f.find(secondWord) > -1:
                foundSecondTerm = 1

            if f.find(thirdWord) > -1:
                foundThirdTerm = 1
        if (foundFirstTerm == 1 or foundSecondTerm == 1) or foundThirdTerm == 1:
            print("Boolean search valid!")
            print(doc)
        else:
            print("Boolean search is not valid!")

    if booleanFirst == "or" and booleanSecond == "and":
        foundFirstTerm: int = 0
        foundSecondTerm: int = 0
        foundThirdTerm: int = 0

        for f in doc:
            if f.find(firstWord) > -1:
                foundFirstTerm = 1

            elif f.find(secondWord) > -1:
                foundSecondTerm = 1

            elif f.find(thirdWord) > -1:
                foundThirdTerm = 1

        if (foundFirstTerm == 1 or foundSecondTerm ==1) and foundThirdTerm == 1:
            print("Boolean search valid!")
            print(doc)

        else:
            print("Boolean search is not valid!")
    if booleanFirst == "and" and booleanSecond == "not":
        foundFirstTerm: int = 0
        foundSecondTerm: int = 0
        foundThirdTerm: int = 0
        for f in doc:
            if f.find(firstWord) > -1:
                foundFirstTerm = 1
            a: int = f.find(secondWord)
            if  a > -1:
                foundSecondTerm = 1

            if f.find(thirdWord) > -1:
                foundThirdTerm = 1
        if (foundFirstTerm == 1 and foundSecondTerm == 1) and foundThirdTerm == 0:
            print("Boolean search valid: True!")
            print(doc)
        else:
            print("Boolean search is not valid!")

    if booleanFirst == "not" and booleanSecond == "and":
        foundFirstTerm: int = 0
        foundSecondTerm: int = 0
        foundThirdTerm: int = 0
        for f in doc:
            if f.find(firstWord) > -1:
                foundFirstTerm = 1

            if f.find(secondWord) > -1:
                foundSecondTerm = 1

            if f.find(thirdWord) > -1:
                foundThirdTerm = 1
        if (foundFirstTerm == 1 and foundSecondTerm == 0) and foundThirdTerm == 1:
            print("Boolean search valid: True!")
            print(doc)
        else:
            print("Boolean search is not valid!")

    if booleanFirst == "or" and booleanSecond == "not":
        foundFirstTerm: int = 0
        foundSecondTerm: int = 0
        foundThirdTerm: int = 0
        for f in doc:
            if f.find(firstWord) > -1:
                foundFirstTerm = 1

            elif f.find(secondWord) > -1:
                foundSecondTerm = 1

            elif f.find(thirdWord) > -1:
                foundThirdTerm = 1

        if (foundFirstTerm == 1 or foundSecondTerm == 1) and foundThirdTerm == 0:
            print("Boolean search valid: True!")
            print(doc)
        else:
            print("Boolean search is not valid!")

    if booleanFirst == "not":
        if booleanSecond == "not":

            for f in doc:
                a: int = f.find(firstWord)
                if a > -1:
                    foundFirstTerm = 1
                    if f.find(secondWord) > -1:
                        foundSecondTerm = 1
                        if f.find(thirdWord) > -1:
                            foundThirdTerm = 1
            if (foundFirstTerm == 1 and foundSecondTerm == 0) and foundThirdTerm == 0:
                print("Boolean search valid: True!")
                print(doc)
            else:
                print("Boolean search is not valid!")


while loop:

    choice = input("Enter 1 for choose document\nEnter 2 for Boolean Search\nEnter 3 for exit: ")
    if choice == '1':

        with open("Doc1.txt", "r") as ins:
            doc1 = []
            for line in ins:
                doc1.append(line)

        with open("Doc2.txt", "r") as ins:
            doc2 = []
            for line in ins:
                doc2.append(line)

        with open("Doc3.txt", "r") as ins:
            doc3 = []
            for line in ins:
                doc3.append(line)

        with open("Doc4.txt", "r") as ins:
            doc4 = []
            for line in ins:
                doc4.append(line)

        with open("Doc5.txt", "r") as ins:
            doc5 = []
            for line in ins:
                doc5.append(line)

        with open("Doc6.txt", "r") as ins:
            doc6 = []
            for line in ins:
                doc6.append(line)

        with open("Doc7.txt", "r") as ins:
            doc7 = []
            for line in ins:
                doc7.append(line)
        print("Files open")
    elif choice == '2':
        search = str(input("Search: ")).strip()
        search.lower()
        search.split(" ")
        firstWord = search.split()[0]
        if firstWord == 'not':
            booleanFirst = search.split()[0]
            firstWord2 = search.split()[1]
            booleanSecond = search.split()[2]
            secondWord = search.split()[3]
            booleanThird = search.split()[4]
            thirdWord = search.split()[5]
            foundFirstTerm: int = 0
            foundSecondTerm: int = 0
            foundThirdTerm: int = 0
            searchNot(firstWord2, booleanSecond, secondWord, booleanThird, thirdWord,
                      foundFirstTerm, foundSecondTerm, foundThirdTerm, doc1)
            searchNot(firstWord2, booleanSecond, secondWord, booleanThird, thirdWord,
                      foundFirstTerm, foundSecondTerm, foundThirdTerm, doc2)
            searchNot(firstWord2, booleanSecond, secondWord, booleanThird, thirdWord,
                      foundFirstTerm, foundSecondTerm, foundThirdTerm, doc3)
            searchNot(firstWord2, booleanSecond, secondWord, booleanThird, thirdWord,
                      foundFirstTerm, foundSecondTerm, foundThirdTerm, doc4)
            searchNot(firstWord2, booleanSecond, secondWord, booleanThird, thirdWord,
                      foundFirstTerm, foundSecondTerm, foundThirdTerm, doc5)
            searchNot(firstWord2, booleanSecond, secondWord, booleanThird, thirdWord,
                      foundFirstTerm, foundSecondTerm, foundThirdTerm, doc6)
            searchNot(firstWord2, booleanSecond, secondWord, booleanThird, thirdWord,
                      foundFirstTerm, foundSecondTerm, foundThirdTerm, doc7)

        elif firstWord != 'not':
            firstWord2 = search.split()[0]
            booleanFirst = search.split()[1]
            secondWord = search.split()[2]
            booleanSecond = search.split()[3]
            thirdWord = search.split()[4]


            searchwithoutnot(firstWord, booleanFirst, secondWord, booleanSecond, thirdWord, doc1)
            searchwithoutnot(firstWord, booleanFirst, secondWord, booleanSecond, thirdWord, doc2)
            searchwithoutnot(firstWord, booleanFirst, secondWord, booleanSecond, thirdWord, doc3)
            searchwithoutnot(firstWord, booleanFirst, secondWord, booleanSecond, thirdWord, doc4)
            searchwithoutnot(firstWord, booleanFirst, secondWord, booleanSecond, thirdWord, doc5)
            searchwithoutnot(firstWord, booleanFirst, secondWord, booleanSecond, thirdWord, doc6)
            searchwithoutnot(firstWord, booleanFirst, secondWord, booleanSecond, thirdWord, doc7)

    elif choice == '3':
        exit(1)
