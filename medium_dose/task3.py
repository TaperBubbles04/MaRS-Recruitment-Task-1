#getting input for the encrypted message
code=input("Enter the encrypted message: ").upper()
m=""

#decoding each letter according to its position
for i, c in enumerate(code):
    s= i+1
    a=ord(c)-65
    ind= (a-s)%26     #ensures proper loop when we shift before A in the alphabet as A is the first alphabet 
    m+=chr(ind+65)

#displaying decoded message
print(m)