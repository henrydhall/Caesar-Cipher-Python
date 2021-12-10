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
    alphabet = string.ascii_letters + string.digits + string.punctuation + string.whitespace
    charactersDeque = collections.deque( alphabet )
    rotatedCharactersDeque = collections.deque( alphabet )
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
    alphabet = string.ascii_letters + string.digits + string.punctuation + string.whitespace
    charactersDeque = collections.deque( alphabet )
    rotatedCharactersDeque = collections.deque( alphabet )
    rotatedCharactersDeque.rotate(-rotateNum)

    #Make the deques strings for the translations.
    charactersString = "".join(list(charactersDeque))
    rotatedCharactersString = "".join(list(rotatedCharactersDeque))

    #Create translation table and perform the translation.
    translateTable = encryptedString.maketrans( rotatedCharactersString, charactersString )
    decryptedString = encryptedString.translate( translateTable )

    return decryptedString

def bruteForceDecrypt( text ):
    decryptions = ''
    for i in range(1,100):
        decryptions += '*'*10 + ' ' + str(i) + '\n' # Neatly separate each decryption, include key.
        decryptions += caesarDecrypt(text,i) + '\n'
    return decryptions

def getOutput( flags, text ):
    if flags.startswith('b'):
        return text

    if flags.endswith('o'):
        return text
    elif flags.startswith('-e'):
        return 'Encrypted text: ' + text
    elif flags.startswith('-d'):
        return 'Decrypted text: ' + text
    

def printUsage():
    print("Usage: python CaesarEncrypter.py -[flags] [\"text\"] [rotation]")
    print("Usage: python CaesarEncrypter.py -[flags] [file] [rotation]")

if __name__ == "__main__":

    if len(sys.argv) == 3:
        if sys.argv[1].startswith('-bi'):
            encryptedText = bruteForceDecrypt( readFromFile(sys.argv[2]) )
        elif sys.argv[1].startswith('-b'):
            encryptedText = bruteForceDecrypt( sys.argv[2] )

        print(encryptedText)

    elif len(sys.argv) == 4:
        encryptedText = ''
        if sys.argv[1].startswith('-ei'):
            encryptedText = caesarEncrypt( readFromFile(sys.argv[2]), int(sys.argv[3]))
        elif sys.argv[1].startswith('-e'):
            encryptedText = caesarEncrypt( sys.argv[2], int(sys.argv[3]))
        elif sys.argv[1].startswith('-di'):
            encryptedText = caesarDecrypt( readFromFile(sys.argv[2]), int(sys.argv[3])) 
        elif sys.argv[1].startswith('-d'):
            encryptedText = caesarDecrypt( sys.argv[2], int(sys.argv[3]))
        

        encryptedText = getOutput(sys.argv[1],encryptedText)
        print(encryptedText)

    else:
        printUsage()
    
