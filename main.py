
import math
import random

consonants = ["b","c","d","f","g","h","j","k","l","m","n","p","q","r","s","t","v","w","x","y","z"]
vowels = ["a","e","i","o","u"]

def getDidgets(v):
    digits = math.floor( math.log10( v ) ) + 1
    return digits

def newtonSQRTaprox(S):
    digits = getDidgets(S)
    if digits < 3:
        currGuess = digits
    elif digits < 6:
        currGuess = digits * 10
    else:
        currGuess = digits * 100

    print "Round0: " + str(currGuess)
    for x in range(1,7):
        currGuess = .5*(currGuess + S/currGuess)
        print "Round"+str(x)+": " + str(currGuess)

#print "library Test Value: "+ str(math.sqrt(25))
#ewtonSQRTaprox(25)

def makeShittyWord(Wlength):
    word = ""
    if Wlength<3:
        vowelPos = random.randint(0, Wlength-1)
        for x in range(0, Wlength):
            if x == vowelPos:
                word += vowels[random.randint(0, len(vowels)-1)]
            else:
                word += consonants[random.randint(0, len(consonants)-1)]
    elif Wlength<7:
        vowelPos = random.randint(0, Wlength-1)
        vowelPos2 = random.randint(0, Wlength-1)
        for x in range(0, Wlength):
            if x == vowelPos or x == vowelPos2:
                word += vowels[random.randint(0, len(vowels)-1)]
            else:
                word += consonants[random.randint(0, len(consonants)-1)]
    return word

for i in range(0,10):
    print makeShittyWord(5)




