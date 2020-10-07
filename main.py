print("Boolean search")
loop = True
choice = -1
doc = []
file = ""

#função que inicia busca com palavra reservada not, com parametros de primeiro termo, segunda palavra
#reservada not ou or ou and, segundo termo, segunda palavra reservada not ou or ou and, terceiro termo
#flag para saber se achou algum termo ou nao
def searchNot(firstWord2, booleanSecond, secondWord, booleanThird, thirdWord,
              foundFirstTerm, foundSecondTerm, foundThirdTerm, doc):
    if booleanSecond == "and" and booleanThird == "and": #se a busca foi not termo and termo2 and termo3
        for f in doc:
            if f.find(firstWord2) > -1: # find retorna um valor acima de -1 se achou, retorna -1 se não achou
                foundFirstTerm = 1
            if f.find(secondWord) > -1:
                foundSecondTerm = 1

            if f.find(thirdWord) > -1:
                foundThirdTerm = 1

        if (foundFirstTerm == 0 and foundSecondTerm == 1) and foundThirdTerm == 1: #se não achou primeiro termo, achou o segundo e o terceiro
            print("Boolean search valid: True!") #busca valida
            print(doc) #mostra quais doc estao
        else:
            print("Boolean search is not valid!")

    elif booleanSecond == "and" and booleanThird == "or": #se a busca foi not termo and termo2 or termo3
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
        if (foundFirstTerm == 0 and foundSecondTerm == 1) or foundThirdTerm == 1: #não achou o primeiro termo e achou o segundo termo ou achou o terceiro
            print("Boolean search valid: True!") #valido
            print(doc)
        else:
            print("Boolean search is not valid!")

    elif booleanSecond == "or" and booleanThird == "or": #buscas com or sao facilmente propicias a mostrar todos os documentos pq basta achar um true que todos os outros viram true e mostram tdos
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

#função que começa a busca com termo primeiro e depois palavras reservadas e outros termos
#so difere do not antes em comparação a função anterior
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
#abre os documentos e salva cada um em uma lista, armazenando cada linha do documento em uma posição
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

        with open("Dicionario.txt", "r") as ins:
            dicionary = []
            for line in ins:
                dicionary.append(line)

    elif choice == '2':
        search = str(input("Search: ")).strip()
        search.split(" ")#separar cada palavra em uma posiçao
        firstWord = search.split()[0] #para saber se é uma busca começando com not ou nao
        if firstWord == 'not': #se for com not
            booleanFirst = search.split()[0]
            firstWord2 = search.split()[1] #primeiro termo
            booleanSecond = search.split()[2] #or ou not ou and
            secondWord = search.split()[3] #segundo termo
            booleanThird = search.split()[4] #or ou not ou and
            thirdWord = search.split()[5] #terceiro termo
            foundFirstTerm: int = 0 #flags se achou o termo ou nao
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

        elif firstWord != 'not': #se a busca não inicia com not
            firstWord2 = search.split()[0] #primeiro termo
            booleanFirst = search.split()[1] #or ou not ou and
            secondWord = search.split()[2] #segundo termo
            booleanSecond = search.split()[3] #or ou not ou and
            thirdWord = search.split()[4] #terceiro termo


            searchwithoutnot(firstWord, booleanFirst, secondWord, booleanSecond, thirdWord, doc1)
            searchwithoutnot(firstWord, booleanFirst, secondWord, booleanSecond, thirdWord, doc2)
            searchwithoutnot(firstWord, booleanFirst, secondWord, booleanSecond, thirdWord, doc3)
            searchwithoutnot(firstWord, booleanFirst, secondWord, booleanSecond, thirdWord, doc4)
            searchwithoutnot(firstWord, booleanFirst, secondWord, booleanSecond, thirdWord, doc5)
            searchwithoutnot(firstWord, booleanFirst, secondWord, booleanSecond, thirdWord, doc6)
            searchwithoutnot(firstWord, booleanFirst, secondWord, booleanSecond, thirdWord, doc7)

    elif choice == '3': #sair do programa
        exit(1)
