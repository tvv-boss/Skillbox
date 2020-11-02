#with open("C:\\soft\\skillbox\\filename.txt", "r") as f:
   #badstr = "Hello world fuck answer"
badstr = input(" Str :")
str = badstr.split(" ")
long = str[0]
for i in str:
    if len(i) >= len(long):
        long = i
print(long)




