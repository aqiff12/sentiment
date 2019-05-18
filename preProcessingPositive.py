def process(strData):
    strBaru1 = strData.replace(",","").upper()
    strPecah = strBaru1.split()
    cari = str(input("Enter you wanted to find: ").upper())
    for words in strPecah:
        if cari.__eq__( words):
            print("Found")
            return True

    f2=open("newNegative.txt","w",encoding="ANSI")
    for w in strPecah:
        f2.write(w+" ")
    f2.close()


f=open("negative.txt","r", encoding="ANSI") #write and open the text fie#
if f.mode=="r":
    contents=f.read()
    process(contents)


