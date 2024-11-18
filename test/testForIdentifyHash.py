#MD5 possède 32 caractères hexadécimaux basée sur la séquence [a-z0-9]
#SHA1 possède la même séquence que MD5 mais il possède 40 caractères hexadécimaux
#SHA256 possède 64 caractères hexadécimaux
#SHA512 possède 128 caractère hexadécimaux
# Hexadécimal : utilise uniquement les caractères [0-9a-f]
# Base 64 : Utilise des caractères tels que +, /, et se termine souvent par =
import os
import re

from passlib.handlers.bcrypt import bcrypt

Yescrypt = "$y$"
SHA512 = "$6$"
MD5="$1$"
Bcrypt = ["$2y$","$2b$"]


hexa= "0123456789abcdef"
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

    if all(c in hexa for c in hash):
        return hash_hexa_type.get(hash_length)


def identifierBase64(hash):
    try:
        # Vérification si c'est bien un multiple de 4 et si cela correspond aux caractères de Base64
        return re.match('^[A-Za-z0-9+/]*={0,2}$', hash) and len(hash) % 4 == 0
    except:
        return False

def identifierBase58(hash):
    if all(char in base58 for char in hash):
        return True
    return False


def identifierBase32(hash):
    if len(hash) % 8 == 0:
        if all(char in base32 for char in hash.rstrip("=")):
            return True
    return False

def identifierBinaire(hash):
    if all(char in binaire for char in hash):
        return True
    return False

def cheat(hash):
    print(os.system("hashid -m "+hash))

def IsHexa(hash):
    if all(c in hexa for c in hash):
        return True
    else:
        return False

def IsBinaire(hash):
    if all(c in binaire for c in hash):
        return True
    else:
        return False

def startWith(hash):
    if hash.startswith("$2b$") or hash.startswith("$2y$"):
        return "bcrypt"
    elif hash.startswith("$1$"):
        return "MD5"
    elif hash.startswith("$5$"):
        return "SHA-256"
    elif hash.startswith("$6$"):
        return "SHA-512"
    elif hash.startswith("$y$"):
        return "Yescrypt"
    else:
        return None

def TypeBase(hash):
    if identifierBase64(hash):
        return "Base64"
    elif identifierBase32(hash):
        return "Base32"
    elif identifierBase58(hash):
        return "Base58"
    else:
        return None


def detectTypeHash(hash):
    if IsHexa(hash):
        return "Hexa"
    elif IsBinaire(hash):
        return "Binaire"
    type = startWith(hash)
    if type is not None:
        return type
    else:
        return TypeBase(hash)


def identify(hash):
    type = detectTypeHash(hash)
    if type=="Hexa":
        return identifierHexa(hash)
    elif type=="Binaire":
        return identifierBinaire(hash)
    elif type=="None":
        return startWith(hash)
    else:
        return type

print(TypeBase("Uznr71EeNkJkUlypTsgbX1H68wsRom"))
print(identify("48bb6e862e54f2a795ffc4e541caed4d"))





