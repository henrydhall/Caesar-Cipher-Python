#!python
"""
#CaesarEncrypter
#Created 8/26/2021 by Henry Hall
#Simple demonstration of a Caesar Cipher encrypter.
#Dependencies: 
"""

import string, collections

def caesarEncrypt( unencryptedString, rotateNum ):
    #Create deques of characters.
    charactersDeque = collections.deque( string.printable )
    rotatedCharactersDeque = collections.deque( string.printable )
    rotatedCharactersDeque.rotate(rotateNum)
    #Make the deques strings for the translations.
    charactersString = "".join(list(charactersDeque))
    rotatedCharactersString = "".join(list(rotatedCharactersDeque))
    #Create translation table and perform the translation.
    translateTable = unencryptedString.maketrans( rotatedCharactersString, charactersString )
    encryptedString = unencryptedString.translate( translateTable )
    print(encryptedString)
    
    
def playAround():
    txt = "Good night Sam!"
    x = "Goda"
    y = "abcx"
    z = "odnght"
    mytable = txt.maketrans(x, y)
    print(txt.translate(mytable))

if __name__ == "__main__":
    caesarEncrypt("This is Henry's fancy thing!",10)
    #playAround()
