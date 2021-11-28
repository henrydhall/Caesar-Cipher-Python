import pytest
import CaesarCipher as CC
from pathlib import Path

def test_CaesarCipher():
    testFile = Path('test_text.txt')
    testString = testFile.read_text()
    for i in range(0,100):
        assert testString == CC.caesarDecrypt( CC.caesarEncrypt(testString, i), i )
        assert len(testString) == len( CC.caesarEncrypt(testString,i))
    
    assert CC.caesarEncrypt(testString, 0) == CC.caesarEncrypt(testString,100)

if __name__ == '__main__':
    test_CaesarCipher()