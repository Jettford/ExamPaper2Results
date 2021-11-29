# Q03(a)

# Initialise variables
alphabet = ["a","b","c","d","e","f","g","h","i","j",
            "k","l","m","n","o","p","q","r","s","t",
            "u","v","w","x","y","z"]

plaintext = ""
ciphertext = ""
key = 0
plaintextLength = 0
count = 0

# Add your code to get the plaintext and convert it to lowercase
tempPlainText = input("What would you like to run through the cipher?:")
plaintext = tempPlainText.lower()

# Add your code to get the key and make sure the key is between 1 and 25 
tempKey = input("What key would you like to use?: ")
try: # check if it isn't an integer
    key = int(tempKey) # convert to int
except ValueError:
    print("The key needs to be a positive integer between 1 and 25")
    exit(0)

if key > 25 or 1 > key: # integer is outside of bounds
    print("The key you entered is out of bounds, please re enter it between 1 and 25")
    exit(0)

# Ciphertext is generated
plaintextLength = len(plaintext)

# Each plaintext letter is convereted into a ciphertext letter
while count <  plaintextLength:
    found = False
    alphabetCount = 0
    while alphabetCount < 26 and found == False:
        if alphabet[alphabetCount] == plaintext[count]:
            found = True
            if alphabetCount + key - 26 < 0:
                ciphertext += alphabet[alphabetCount + key]
            else:
                ciphertext += alphabet[alphabetCount + key - 26]
        alphabetCount = alphabetCount + 1
    count = count + 1

# Add your code to write the ciphertext to a text file    
with open("Cipher.txt", "w") as file:
    file.write(ciphertext)

# Add your code to display the ciphertext
print(f"The cipher is: {ciphertext}")