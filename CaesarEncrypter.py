#!python
"""
#CaesarEncrypter
#Created 8/26/2021 by Henry Hall
#Simple demonstration of a Caesar Cipher encrypter.
#Dependencies: 
"""

import string, collections, sys

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
    return encryptedString

if __name__ == "__main__":
    print( sys.argv )
    if len(sys.argv) < 3:
        print("Usage: python CaesarEncrypter.py [\"text to encrypt\"] [rotation]")
        print("Usage: python CaesarEncrypter.py -i [file to encrypt] [rotation]")
        print("Usage: python CaesarEncrypter.py -i [file to encrypt] -o [file to output to] [rotation]")
    elif len(sys.argv) == 3:
        print( "Encrypted text: " + caesarEncrypt( sys.argv[1], int(sys.argv[2])) )
    else:
        print("TODO: lots")
    
