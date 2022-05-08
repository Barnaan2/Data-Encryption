print("caesar Cipher: ")
print('the first encryption code with only three letter jump')
letters = {'A': 1, 'B': 2, 'C': 3, 'D': 4,
           'E': 5, 'F': 6, 'G': 7, 'H': 8,
           'I': 9, 'J': 10, 'K': 11, 'L': 12,
           'M': 13, 'N': 14, 'O': 15, 'P': 16,
           'Q': 17, 'R': 18, 'S': 19, 'T': 20,
           'U': 21, 'V': 22, 'W': 23, 'X': 24, 'Y': 25,
           'Z': 26, " ": 27}


def lock(to_arrays, key):
    key = 3
    word = ""
    for item in to_arrays:
        capture = item.upper()
        letter = int(letters[capture]) + key
        value = letter % 27
        for items in letters:
            if letters[items] == value:
                 word += items


    return word


def unlock(to_arrays, key):
    key=3
    word = ""
    for item in to_arrays:
        capture = item.upper()
        letter = int(letters[capture]) - key
        value = letter % 27
        for items in letters:
            if letters[items] == value:

                 word += items



    return word


a = input('Insert the text you want to Encrypt/Decrypt ')
to_array = [char for char in a]
b = int(input("insert the key: "))
if b==3:
    pass
else:
    print('illegal key')

check = input('enter 1 for encrypting , 2 for decrypting')

if check == '1':
    cipher = lock(to_array, 3)
    print(cipher)
elif check == '2':
    cipher = unlock(to_array, 3)
    print(cipher)
else:
    print('illegal input')
