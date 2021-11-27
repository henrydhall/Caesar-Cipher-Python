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
    """
    # A simple Caesar Cipher is implemented with a 100 character alphabet.
    # It inputs the string that you want encrypted, and the rotation you want performed on it.
    # It returns an encrypted string.
    # This is where the magic happens.
    """
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
    # Returns "" if no file found.
    """
    try:
        fileToRead = Path(fileName)
        fileContents = fileToRead.read_text()
        return fileContents
    except FileNotFoundError:
        print(f"FileNotFoundError: {fileName} doesn't exist.")
        return ""

def writeToFile(fileName, writeString):
    """
    # Writes writeString to fileName.
    # Returns nothing.
    """
    fileToWrite = Path(fileName)
    fileToWrite.write_text(writeString)

def caesarDecrypt(encryptedString, rotateNum):
    """
    # Accepts an encrypted string, and the rotation that was used to encrypt it.
    # Returns the decrypted string.
    """

    #Create deques of characters.
    charactersDeque = collections.deque( string.printable )
    rotatedCharactersDeque = collections.deque( string.printable )
    rotatedCharactersDeque.rotate(-rotateNum)

    #Make the deques strings for the translations.
    charactersString = "".join(list(charactersDeque))
    rotatedCharactersString = "".join(list(rotatedCharactersDeque))

    #Create translation table and perform the translation.
    translateTable = encryptedString.maketrans( rotatedCharactersString, charactersString )
    decryptedString = encryptedString.translate( translateTable )

    return decryptedString

def printUsage():
    print("Usage: python CaesarEncrypter.py -e [\"text to encrypt\"] [rotation]")
    print("Usage: python CaesarEncrypter.py -ei [file to encrypt] [rotation]")
    print("Usage: python CaesarEncrypter.py -d [\"text to decrypt\"] [rotation]")
    print("Usage: python CaesarEncrypter.py -di [file to decrypt] [rotation]")

if __name__ == "__main__":

    if len(sys.argv) < 3:
        printUsage()

    elif len(sys.argv) == 4:
        if sys.argv[1] == '-e':
            print( "Encrypted text: " + caesarEncrypt( sys.argv[2], int(sys.argv[3])) )
        if sys.argv[1] == '-ei':
            print( "Encrypted text: " + caesarEncrypt( readFromFile(sys.argv[2]), int(sys.argv[3])) )
        elif sys.argv[1] == '-d':
            print( "Decrypted text: " + caesarDecrypt( sys.argv[2], int(sys.argv[3])) )
        if sys.argv[1] == '-di':
            print( "Decrypted text: " + caesarDecrypt( readFromFile(sys.argv[2]), int(sys.argv[3])) )
    else:
        printUsage()
    
