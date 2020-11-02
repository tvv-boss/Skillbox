#filename = input("Enter a filename: ")

def count_char(text, char):
  count = 0
  for c in text:
    if c == char:
      count += 1
  return count

with open("C:\\soft\\skillbox\\filename.txt", "r") as f:
   text = f.read()

for char in "abcdefghijklmnopqrstuvwxyz1234567890":
  perc = 100 * count_char(text, char) / len(text)
  print("{0} - {1}%".format(char, round(perc, 2)))

