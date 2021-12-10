# Caesar-Cipher-Python
Simple Caesar Cipher in Python to encrypt and decrypt text.

# Description
Using an alphabet of 100 printable characters, the program will accept input from the command line or text files to encrypt and print to the command line.
# Usage
## Encrypt Text
In command line enter 

    python CaesarEncrypter.py -e \[Text to encrypt] \[rotation] 
or

    python CaesarEncrypter.py -ei \[File to encrypt] \[rotation]

If outputting to a file, use the o flag to remove extra text. Ex: -eio, -do, etc.

Text to encrypt: whatever you want to encrypt. Use quotes around.

Rotation: how many places you want the alphabet rotated.

File to encrypt: the file whose contents you want to encrypt.

## Decrypt Text

Use -d and -di flags to decrypt text in place of -e and -ei flags.

## Brute Force Decryption

Use -b and -bi flags to brute force decrypt text.

It is recommended to output to a file, as it will produce 100 lines of output for each line of output.

The o flag will not affect output of the program when brute force decrypting.

Decrypted texts are separated by a line of text as below.

    ********** n
Where n is the number of the rotation made.

# Features
Encrypt text from the commandline or a file and print to command line.

Decrypt text from the commandline or a file print to command line.

Brute force decrpyt text from the commandline or a file and print to command line.

# Future Updates
Improve brute force decryption by enabling search for keywords from file.

Improve brute force decryption by allowing user to restrict alphabet.