#!python
"""
#CaesarEncrypter
#Created 8/26/2021 by Henry Hall
#Simple demonstration of a Caesar Cipher encrypter.
#Dependencies: 
"""

import string, collections, sys
from pathlib import Path

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

def readFromFile(fileName):
    """
    # This reads text from a file and returns contents as a string.
    """
    fileToRead = Path(fileName)
    return fileToRead.read_text()

if __name__ == "__main__":
    print( sys.argv ) #Temporary to keep track of command line input
    if len(sys.argv) < 3:
        print("Usage: python CaesarEncrypter.py [\"text to encrypt\"] [rotation]")
        print("Usage: python CaesarEncrypter.py -i [file to encrypt] [rotation]")
        print("Usage: python CaesarEncrypter.py -i [file to encrypt] -o [file to output to] [rotation]")
    elif len(sys.argv) == 3:
        print( "Encrypted text: " + caesarEncrypt( sys.argv[1], int(sys.argv[2])) )
        #print( "Decrypted text: " + caesarEncrypt( caesarEncrypt( sys.argv[1], int(sys.argv[2])) , - int(sys.argv[2]) ))
    elif len(sys.argv) == 4:
        print( "Encrypted text: " + caesarEncrypt( readFromFile(sys.argv[2]), int(sys.argv[3])))
    else:
        print("TODO: lots")
    
