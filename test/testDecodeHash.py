import base64
import hashlib
import os
import sys

import base58
import bcrypt
from multiprocessing import Pool,cpu_count



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


def decode_hashHexa(hash, wordlist, hash_type):
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


def test_passwordBcrypt(password, hash_bytes):
    if bcrypt.checkpw(password.encode('utf-8'), hash_bytes):
        print(f"Mot de passe trouvé : {password}")
        return True

def decode_Bcrypt(hash, wordlist_path):
    # Conversion du hash en bytes s'il est sous forme de chaîne
    if isinstance(hash, str):
        hash_bytes = hash.encode('utf-8')
    else:
        hash_bytes = hash

    # Lire le fichier .txt ligne par ligne avec un encodage approprié
    try:
        with open(wordlist_path, 'r', encoding='latin-1') as file:
            wordlist = [line.strip() for line in file]
    except UnicodeDecodeError:
        print("Erreur de décodage : impossible de lire certains caractères.")
        return

    # Utiliser `starmap` pour passer chaque mot de la wordlist avec le hash
    with Pool(cpu_count()) as pool:
        args = [(word, hash_bytes) for word in wordlist]
        results = pool.starmap(test_passwordBcrypt, args)
        if any(results):
            print("Mot de passe cassé avec succès")
        else:
            print("Aucun mot de passe trouvé")






print(decode_Bcrypt("$2y$12$Dwt1BZj6pcyc3Dy1FWZ5ieeUznr71EeNkJkUlypTsgbX1H68wsRom","/home/daoudi/Documents/outil_hack/wordlists/rockyou.txt"))
