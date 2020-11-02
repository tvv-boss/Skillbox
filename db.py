#file = open("filename.txt", "r")
#cont = file.read()
#print(cont)
#file.close()
#with open("filename.txt", "r") as f:
f = open("C:\\soft\\skillbox\\filename.txt", "r")
#for i in file:
book = f.readlines()
dlen = len(book)
j=0
for i in book:
    j+=1
    if j == dlen:
        print(str(i[0]) + str(len(i)+1))
    else:
        print(str(i[0]) + str(len(i)))
f.close()