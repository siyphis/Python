import secrets
def generate_key(text):
    keychain = []
    for char in text: #generates a random string of numbers corralating to each character
        key = str(secrets.randbelow(27))
        keychain.append(key)
    return keychain

def encode(text):
    keychain = generate_key(text)
    encoded = ''
    characters =[' ',"a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    for i in range(len(text)):#uses the correlating number to perform a cesar shift on each character
        character=text[i]
        index = characters.index(character.lower())
        if (index+int(keychain[i])) < (len(characters)):
            character =characters[index + int(keychain[i])]
        else:
            character =characters[index + int(keychain[i]) - len(characters)]
        encoded += character
    print(encoded)
    print("".join(keychain))

encode(input('Enter Text:'))