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

if __name__ == "__main__":
    print( sys.argv ) #Temporary to keep track of command line input
    #TODO: put this all in another file.
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
    
