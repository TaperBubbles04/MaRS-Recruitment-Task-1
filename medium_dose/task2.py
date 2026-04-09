#getting the input for morse code message
mc=input("Enter the Morse Code message:")

#cheat sheet for decoding the message
mccs= {'.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E', '..-.': 'F', '--.': 'G', '....': 'H', '..': 'I', '.---': 'J', '-.-': 'K', '.-..': 'L', '--': 'M', '-.': 'N', '---': 'O', '.--.': 'P', '--.-': 'Q', '.-.': 'R', '...': 'S', '-': 'T', '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X', '-.--': 'Y', '--..': 'Z',
'.----': '1', '..---': '2', '...--': '3', '....-': '4', '.....': '5', '-....': '6', '--...': '7', '---..': '8', '----.': '9', '-----': '0'
}

#We are assuming the message follows the standard rules of morse code where there is 1-unit gap between sybmols and 3-unit gap between each letter and 7-unit gap between each word

#splitting the morse code message into each word
w= mc.strip().split('       ')
mw=[]

#decoding each word
for c in w:
    l= c.split('   ')
    dw=''
    
    #decoding each letter in the word
    for lc in l:
        lc= lc.replace(' ', '')
        if lc in mccs:
            dw+=mccs[lc]   #identifying the letter using cheat sheet
                
    mw.append(dw)

print(' '.join(mw))   #displaying the decoded message