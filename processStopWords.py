def process(strData):
    remove=strData.replace("\n"," ").upper()
    print(remove)
    f2=open("newStopWords.txt","w")
    for w in remove:
        f2.write(w)
    f2.close()
f=open("stopWords.txt","r")
if f.mode=="r":
    contents=f.read()
    process(contents)