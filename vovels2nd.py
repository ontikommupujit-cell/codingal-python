sentence=input("Enter a sentence: ")

vowels=set()

for letter in sentence.lower():
    if letter in "aeiou":
        vowels.add(letter)

print("Unique vowels:",vowels)
print("Total unique vowels:",len(vowels))