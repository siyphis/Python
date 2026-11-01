import secrets
def generate_key(text):
    keychain = []
    for char in text: #generates a random string of numbers corralating to each character
        key = secrets.randbelow(26)
        keychain.append(key)
    return keychain

def encode(text):
    keychain = generate_key(text)
    encoded = ''
    characters =[' ',"a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    for i in range(len(text)):#uses the correlating number to perform a cesar shift on each character
        character=text[i]
        index = characters.index(character.lower())
        character =characters[(index + keychain[i])% 26]
        encoded += character
    return encoded,keychain

def decode(text,key):
    decoded =''
    characters =[' ',"a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    for i in range(len(text)):
            decoded +=characters[(characters.index(text[i]) - key[i]) % 26]
    return decoded

cyphertext,keychain = encode(input('Enter Text:'))
print(f"\nCyphertext: '{cyphertext}'")
print(f"Key: '{keychain}'")
print(f"\nDecoded: '{decode(cyphertext,keychain)}'")