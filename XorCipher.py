import random
import string

#Calls Menu or Exits Program
def xorExit():
    option = input('Press [1] to return to Menu or Press [2] to exit: ')
    if option == '1':
        xorPy()
    elif option == '2':
        exit()
    else:
        print('INVALID INPUT, Please input a valid option.')
        xorExit()

#Menu/Options
def xorPy():
    print('''
__   _____________   _____ _       _
\ \ / /  _  | ___ \ /  __ (_)     | |
 \ V /| | | | |_/ / | /  \/_ _ __ | |__   ___ _ __
 /   \| | | |    /  | |   | | '_ \| '_ \ / _ \ '__|
/ /^\ \ \_/ / |\ \  | \__/\ | |_) | | | |  __/ |
\/   \/\___/\_| \_|  \____/_| .__/|_| |_|\___|_|
                            | |
___________________________________________________
            Developed by: JeremyG
             ------------------
      ''')
    option = input('Press [1] for Encryption or Press [2] for Decryption: ')
    if option == '1':
        xorFunction()
    elif option == '2':
        xorOut()
    else:
        print('INVALID INPUT, Please input a valid option.')
        xorExit()

###Encryption via XOR##
def xorFunction():
    userInput = input('Enter Plain-Text: ')


#Key Encryption
    key = ''.join(random.SystemRandom().choice(string.ascii_letters + string.digits) for _ in range(10))
    print('Key: ' + key)
    keyList = list(key)
    asciiKeyList = []
    for x in range(0, len(key)):
        keyBin = bin(ord(key[x]))
        removeBin = keyBin.replace("0b", "")
        asciiKeyList.append(removeBin)
    finalKeyBin = (int(''.join(asciiKeyList)))


#UserInput Encryption
    cipherList = []
    for char in range(0, len(userInput)):
        inputBin = bin(ord(userInput[char]))
        removeB = inputBin.replace("0b", "")
        convertInt = int(removeB)
        xorCipher = convertInt ^ finalKeyBin
        cipherList.append(xorCipher)
        #Asterisk for signifying end of entry
    print('Encrypted Cipher-Text: ' + str(cipherList)[1:-1] + '*')

#DECRYPTION
    decryptionList = []
    for i in range(0, len(cipherList)):
        cipherText = cipherList[i]
        xorDecrypt = str(cipherText ^ finalKeyBin)
        num = int(xorDecrypt, 2)
        text = chr(num)
        decryptionList.append(text)
    PlainText = ''.join(decryptionList)
    print('Plain-Text Message: ', PlainText)
    xorExit()

#Decryption via XOR
def xorOut():
    cipherText = input('Enter Cipher Strings: ')
    key = input('Enter Key: ')

#Convert User-Input to List
    cipherList = []
    myList = []
    for i in cipherText:
        if i == ',':
            cipherList.append('')
            cipherList.remove('')
            test = ''.join(cipherList)
            myList.append(test)
            cipherList.clear()
        elif i == ' ':
            cipherList.append('')
            cipherList.remove('')
        #ends input and clears list
        elif i == '*':
            cipherList.append('')
            cipherList.remove('')
            joinList = ''.join(cipherList)
            myList.append(joinList)
            cipherList.clear()
        else:
            cipherList.append(i)

#Convert key to bin
    keyList = list(key)
    asciiKeyList = []
    for x in range(0, len(key)):
        keyBin = bin(ord(key[x]))
        removeBin = keyBin.replace("0b", "")
        asciiKeyList.append(removeBin)
    finalKeyBin = (int(''.join(asciiKeyList)))

#Decryption
    decryptionList = []
    for i in range(0, len(myList)):
        cipherText = int(myList[i])
        xorDecrypt = str(cipherText ^ finalKeyBin)
        num = int(xorDecrypt, 2)
        text = chr(num)
        decryptionList.append(text)
    print('Decrypted Plain-Text:' + ''.join(decryptionList))
    xorExit()

#Program Start
xorPy()
