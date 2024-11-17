#MD5 possède 32 caractères hexadécimaux basée sur la séquence [a-z0-9]
#SHA1 possède la même séquence que MD5 mais il possède 40 caractères hexadécimaux
#SHA256 possède 64 caractères hexadécimaux
#SHA512 possède 128 caractère hexadécimaux
# Hexadécimal : utilise uniquement les caractères [0-9a-f]
# Base 64 : Utilise des caractères tels que +, /, et se termine souvent par =
import os

hash_str = "LPJNul+8oy4mspQi7omB8xT8WnZ/sFO61ldh7RTQ4CM="

#MD2, MD4, MD5, SHA1, SHA224, SHA256, SHA-384, SHA512, SHA3-224, SHA3-256, SHA3-384, SHA3-512

hexa = "0123456789abcdef"
binaire="01"
base64 = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ+/="
base58 = "123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz"
base32 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ234567"



def identifierHexa(hash):

    hash_hexa_type={
        32:["MD2","MD4","MD5","RIPEMD-128","Blake2s"],
        40:["SHA-1","RIPEMD-160"],
        48:["Tiger"],
        56:["SHA-224", "SHA3-224"],
        64:["SHA-256","SHA3-256","RIPEMD-256","Blake3"],
        80:["RIPEMD-320"],
        96:["SHA-384","SHA3-384"],
        128:["SHA-512","SHA3-512","Whirlpool","Blake2b"],
    }

    hash_length = len(hash)

    if all(c in hexa for c in hash_str):
        return hash_hexa_type.get(hash_length)


def identifierBase64(hash): #Rajouter à la fin que le hash doit se terminer par un "="

    if len(hash) % 4 == 0:
        if all(char in base64 for char in hash.rstrip("=")):
            return "Base64"
    return None

def identifierBase58(hash):
    if all(char in base58 for char in hash):
        return "Base58"
    return None


def identifierBase32(hash):
    if len(hash) % 8 == 0:
        if all(char in base32 for char in hash.rstrip("=")):
            return "Base32"
    return None

def identifierBinaire(hash):
    if all(char in binaire for char in hash):
        return "Binaire"
    return None

def cheat(hash):
    print(os.system("hashid -m "+hash))


print(identifierBase64(hash_str))

# Exemple de hachage en Base64
hash_base64 = "SGVsbG8gd29ybGQ="
print(identifierBase64(hash_base64))  # Affichera "Base64"

# Exemple de hachage en Base58
hash_base58 = "2cQv7sP8KhxQJg6DXYq"
print(identifierBase58(hash_base58))  # Affichera "Base58"

# Exemple de hachage en Base32
hash_base32 = "JBSWY3DPEHPK3PXP"
print(identifierBase32(hash_base32))  # Affichera "Base32"

# Exemple de hachage binaire
hash_binaire = "101010"
print(identifierBinaire(hash_binaire))  # Affichera "Binaire"
