def process(i, strData, positive, negative):
    news = strData.upper()
    removeDoubleQuote = news.replace("\"","") #remove Double quote in a string
    removeSingleQuote = removeDoubleQuote.replace("'\'", "") #remove single quote
    removeFullstop = removeSingleQuote.replace("\.", "") #remove fullstop
    news3 = removeFullstop.split() #split the news, to identify the sentiment
    positiveWords = positive.split() #load and split the positive words
    negativeWords = negative.split() #load and split the negative words
    match(i, negativeWords, positiveWords, news3)


def match(i, negativeWord, positiveWord, news3):
    negative = 0   #initiliaze the value of negative, positive and neutral
    positive = 0
    neutral = 0
    f = open("newStopWords.txt", "r") #to remove stop words, bcs it is not important and only affect the neutral counting.
    if f.mode == "r":
        ada = f.read()
    for berita in news3:
        if berita in positiveWord: #use brute force algorithm where we check one by one
            positive += 1 #if the word is found in positive words, we will increment positive
        elif berita in negativeWord:
            negative+=1 #if the word is found in negative words, we will increment negative
        elif berita in ada:
            neutral -= 1 #if the word is found in stop words, we will decrement neutral
        else:
            neutral+=1 #if the word is not found in three of the file words, we will increment neutral

#to print the type of file, positive, negative and neutral of the text file (not overall, only that file)
    print("File {} ".format(i))
    print("Positivity: ",positive)
    print("Negativity: ",negative)
    print("Neutral: ",neutral)
    total = positive + neutral +negative
    if positive > neutral and positive > negative:
        print("This text is positive: ", positive / total)
    elif negative > neutral and negative > positive:
        print("This text is negative: ",negative/total)
    else :
        print("This text is neutral: ", neutral/total)
    print()



print("The pitstops are \nHavana \nLondon \nBarcelona \nNew York \nTokyo \nShanghai \nSydney")
print()
destination = str(input("Please enter your destination: "))

#array of the files of the pitstops
sydneyArr = ["sydney/sydney.txt","sydney/sydney2.txt", "sydney/sydney3.txt", "sydney/sydney4.txt"]
shanghaiArr = ["shanghai/shanghai.txt", "shanghai/shanghai2.txt", "shanghai/shanghai3.txt"]
tokyoArr = ["tokyo/tokyo.txt","tokyo/tokyo2.txt","tokyo/tokyo3.txt"]
londonArr = ["london/london.txt","london/london2.txt","london/london3.txt"]
nyArr = ["NY/newyork.txt","NY/newyork2.txt","NY/newyork3.txt"]
havanaArr = ["havana/havana.txt","havana/havana2.txt","havana/havana3.txt"]
barcelonaArr = ["barcelona/barcelona.txt","barcelona/barcelona2.txt","barcelona/barcelona3.txt"]

#load positive and negative files
f2=open("newPositive.txt", "r")
f3=open("newNegative.txt","r", encoding="ANSI")


if destination == "Havana":
    for i in havanaArr:
        f1=open(i,"r")
        f2=open("newPositive.txt", "r")
        f3=open("newNegative.txt","r", encoding="ANSI")
        if f1.mode=="r":
            if f2.mode=="r":
                if f3.mode=="r":
                    contents=f1.read()
                    positive=f2.read()
                    negative=f3.read()
                    process(i,contents, positive, negative)

elif destination == "Sydney":
    for i in sydneyArr:
        f1=open(i,"r")
        f2=open("newPositive.txt", "r")
        f3=open("newNegative.txt","r", encoding="ANSI")
        if f1.mode=="r":
            if f2.mode=="r":
                if f3.mode=="r":
                    contents=f1.read()
                    positive=f2.read()
                    negative=f3.read()
                    process(i,contents, positive, negative)

elif destination == "Shanghai":
    for i in shanghaiArr:
        f1=open(i,"r")
        f2=open("newPositive.txt", "r")
        f3=open("newNegative.txt","r", encoding="ANSI")
        if f1.mode=="r":
            if f2.mode=="r":
                if f3.mode=="r":
                    contents=f1.read()
                    positive=f2.read()
                    negative=f3.read()
                    process(i,contents, positive, negative)


elif destination == "Tokyo":
    for i in tokyoArr:
        f1=open(i,"r")
        f2=open("newPositive.txt", "r")
        f3=open("newNegative.txt","r", encoding="ANSI")
        if f1.mode=="r":
            if f2.mode=="r":
                if f3.mode=="r":
                    contents=f1.read()
                    positive=f2.read()
                    negative=f3.read()
                    process(i,contents, positive, negative)

elif destination == "London":
    for i in londonArr:
        f1=open(i,"r")
        f2=open("newPositive.txt", "r")
        f3=open("newNegative.txt","r", encoding="ANSI")
        if f1.mode=="r":
            if f2.mode=="r":
                if f3.mode=="r":
                    contents=f1.read()
                    positive=f2.read()
                    negative=f3.read()
                    process(i,contents, positive, negative)

elif destination == "New York":
    for i in nyArr:
        f1=open(i,"r")
        f2=open("newPositive.txt", "r")
        f3=open("newNegative.txt","r", encoding="ANSI")
        if f1.mode=="r":
            if f2.mode=="r":
                if f3.mode=="r":
                    contents=f1.read()
                    positive=f2.read()
                    negative=f3.read()
                    process(i,contents, positive, negative)

elif destination == "Barcelona":
    for i in barcelonaArr:
        f1=open(i,"r")
        f2=open("newPositive.txt", "r")
        f3=open("newNegative.txt","r", encoding="ANSI")
        if f1.mode=="r":
            if f2.mode=="r":
                if f3.mode=="r":
                    contents=f1.read()
                    positive=f2.read()
                    negative=f3.read()
                    process(i,contents, positive, negative)

else:
    print("Sorry, no news for the city")