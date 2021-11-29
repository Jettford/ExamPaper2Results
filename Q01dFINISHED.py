# Q01d

vowels = ["a","e","i","o","u"] 
numVowels = [0,0,0,0,0] 

sentence = input("Input the sentence ")

for letter in sentence: # iteration starts
    for vowel in vowels: # selection starts
        if vowel == letter:   # relational operator
            numVowels[vowels.index(vowel)] +=1 # data structure is initialised

print("Here are the number of vowels in the sentence "+ sentence)      
for vowel in vowels:
    print("The number of",vowel,"is",numVowels[vowels.index(vowel)])
