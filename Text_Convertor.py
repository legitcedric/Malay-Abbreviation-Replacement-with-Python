
import pyperclip

string = input("Please enter the given text: ") #for input prompt

str = string.replace("kau", "kamu") #for text replacement
str1 = str.replace("dgn", "dengan") #for text replacement
str2 = str1.replace("awk", "awak") #for text replacement

pyperclip.copy(str2)
print(str2)