# Q04(a)

import random

# Get input
productName = input("What is the product name?: ")
productAcroynm = ""
for x in range(3): # I forgot how to sub string in python
    productAcroynm += productName.upper()[x]

# Generate a random number between 10 and 30 inclusive

randInt = random.randint(10, 30)
randIntString = str(randInt) # converted random string


# Generate the product code - first three letters of product name and the random number

productCode = productAcroynm + randIntString


# Display the product code and the product name

print(f"{productCode} - {productName}")
