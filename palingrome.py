# Write a function/functions that checks whether the sentence you get from the user is a palindrome. (Do not consider punctuation and special characters. Only consider "alphanumeric" characters.)

# input : "ey edip adana'da, pide ye!"

# output : "ey edip adana'da, pide ye!" is a palindrome

# input : "Was it a car or a cat I saw?"

# output : "Was it a car or a cat I saw?" is a palindrome

sentence = input("Please enter a sitring: ")
liste = []
n = 0
while n < len(sentence) :
    if sentence.lower()[n].isalnum() :
        liste.append(sentence.lower()[n])
    n += 1
    
# print(liste[::])
# print(liste[len(liste)::-1])
if liste[::] == liste[len(liste)::-1] :
    print(f"{sentence} is a palindrome")
else :
    print(f"{sentence} is not a palindrome")