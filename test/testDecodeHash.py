import base64
import hashlib
import base58



def decode_base64(chaine):
    return base64.b64decode(chaine)

def decode_base58(chaine):
    return base58.b58decode(chaine)

def decode_base32(chaine):
    return base64.b32decode(chaine)

def decode_binaire(chaine):
    return int(chaine, 2)

def decode_binaire_to_text(chaine):
    return ''.join(chr(int(chaine[i:i+8], 2)) for i in range(0, len(chaine), 8))


def decode_hash(hash, wordlist, hash_type):
    hash_funcs={
        "SHA-1": hashlib.sha1,
        "SHA-224": hashlib.sha224,
        "SHA-256": hashlib.sha256,
        "SHA-384": hashlib.sha384,
        "SHA-512": hashlib.sha512,
        "SHA3-384": hashlib.sha3_384,
        "SHA3-512": hashlib.sha3_512,
        "SHA3-224": hashlib.sha3_224,
        "SHA3-256": hashlib.sha3_256,
        "MD5": hashlib.md5,
        "Blake2b" : hashlib.blake2b,
        "Blake2s": hashlib.blake2s
    }

    hash_func = hash_funcs[hash_type]

    with open(wordlist, 'r', encoding='utf-8', errors='ignore') as file:
        for line in file:
            password_candidat = line.strip()
            hash_candidat = hash_func(password_candidat.encode('utf-8')).hexdigest()
            if hash_candidat==hash:
                return password_candidat
    return None




hash = "48bb6e862e54f2a795ffc4e541caed4d"
encoded_base64 = "SGVsbG8gd29ybGQ="
encoded_base58 = "2cQv7sP8KhxQJg6DXYq"
encoded_base32 = "JBSWY3DPEHPK3PXP"
encoded_binaire = "0100100001100101011011000110110001101111"  # Correspond à "Hello"

"""
print(decode_base64(encoded_base64))  # Affiche: b'Hello world'
print(decode_base58(encoded_base58))  # Affiche: b'Hello world' (en bytes)
print(decode_base32(encoded_base32))  # Affiche: b'Hello world'
print(decode_binaire(encoded_binaire))  # Affiche: 310939249775
print(decode_binaire_to_text(encoded_binaire))  # Affiche: Hello
"""

print(decode_hash(hash,"/home/daoudi/Documents/outil_hack/wordlists/rockyou.txt","MD5"))
