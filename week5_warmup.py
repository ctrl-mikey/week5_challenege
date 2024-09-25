# Problem Set 1: Indexing and Slicing Strings
# Basic Indexing:
 #Given the string 
word = "abracadabra"
#a. Retrieve the 5th character.
print(word[5])
# b. Retrieve the second to last character.
print(word[-2])
# # c. Find the first occurrence of the letter 'c'.
print(word.find("c"))
# # Given the string alphabet = 'abcdefghijklmnopqrstuvwxyz',\
cat = 'abcdefghijklmnopqrstuvwxyz'
# # a. Extract the letters 'hij'.
print(cat[7:10])
# # b. Extract every second letter starting from 'a' to 'm'.
print(cat[0:12:2])
# # c. Reverse the entire string using slicing.
print(cat[::-1])
# # Problem Set 2: Extracting Information
# # From Descriptions:
# # Extract the name of the famous personality from the quote "Ask not what your country can do for you — ask what you can do for your country. - John F. Kennedy"
quote = "Ask not what your country can do for you — ask what you can do for your country. - John F. Kennedy"
print(quote.find("J"))
print(quote[83:])
# # Manipulating Words:
# # Given the string info = "Python is fun. Fun is good. Good is subjective.",
# # a. Extract the word 'subjective' without knowing its exact position.
info = "Python is fun. Fun is good. Good is subjective."
reverse = info[::-1]
last_word = reverse[1:11]
answer = last_word[::-1]
print(answer)
# # b. Extract every third word.
words = info.split()
extracted = (words[0::3])
print("".join(extracted))
# # c. Reverse the positions of the words, but keep the characters in each word in the same order.
words[0::-1]
# # Problem Set 3: String Methods
# Upper & Lower:
# Convert the following text to lowercase: "MAY THE FORCE BE WITH YOU."
quote = "MAY THE FORCE BE WITH YOU."
print(quote.lower())
# String Joining and Splitting:
# Given the list motto = ["Make", "haste", "slowly."],\
motto = ["Make", "haste", "slowly."]
# a. Convert the list into a single string.
single = "".join(motto)
print(single)
# b. Now, split the string at every occurrence of the letter 'a'.
split = single.split("a")
print(split)
# Replacing Words:
# Modify the sentence: "Life is what happens when you are busy making other plans."
quote2 = "Life is what happens when you are busy making other plans."
# a. Replace "busy" with "distracted".
replaced_string = (quote2.replace("busy", "distracted"))
print(replaced_string)
# b. Replace "plans" with "mistakes".
# Problem Set 4: String Properties and Advanced Operations
# Repetition:
# Concatenate the word "Iteration" 7 times.
print("iteration" + "iteration" + "iteration" + "iteration" + "iteration" + "iteration" + "iteration" )
# Word Search:
# Check if the word "moonlight" appears in the quote: "With freedom, books, flowers, and the moon, who could not be happy? - Oscar Wilde"
oscars_quote = "With freedom, books, flowers, and the moon, who could not be happy? - Oscar Wilde"
print("moontlight" in oscars_quote)
# Length and Count:
# a. Calculate the number of characters (including spaces and punctuation) in the word/phrase: "Supercalifragilisticexpialidocious".
string = "Supercalifragilisticexpialidocious"
print(len(string))
# b. Count the number of times the letter 'i' appears in the same word/phrase.
print(string.count("i"))