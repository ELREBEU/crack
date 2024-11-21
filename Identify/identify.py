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
        32:["MD5","Blake2s","MD4","MD2"],
        40:["SHA-1","RIPEMD-160"],
        48:["Tiger"],
        56:["SHA-224", "SHA3-224"],
        64:["SHA-256","SHA3-256","Blake3","RIPEMD-256"],
        80:["RIPEMD-320"],
        96:["SHA-384","SHA3-384"],
        128:["SHA-512","SHA3-512","Blake2b","Whirlpool"],
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
        return "Bcrypt"
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
    # Priorité : détecter les types de hachage avec préfixes spécifiques
    type = startWith(hash)
    if type is not None:
        return type

    # Vérifications secondaires pour les bases ou autres formats
    if IsHexa(hash):
        return "Hexa"
    elif IsBinaire(hash):
        return "Binaire"
    elif identifierBase64(hash):
        return "Base64"
    elif identifierBase58(hash):
        return "Base58"
    elif identifierBase32(hash):
        return "Base32"

    # Aucun type détecté
    return None




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
