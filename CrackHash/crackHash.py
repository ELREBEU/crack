import bcrypt
import hashlib
from Cryptodome.Hash import SHA3_224, SHA3_256, SHA3_384, SHA3_512, BLAKE2b, MD2, MD4, RIPEMD


def decode_hashHexa(hash, wordlist, hash_type):
    hash_funcs = {
        "MD5": lambda data: hashlib.md5(data).hexdigest(),
        "Blake2s": lambda data: hashlib.blake2s(data).hexdigest(),
        "MD4": lambda data: MD4.new(data).hexdigest(),
        "MD2": lambda data: MD2.new(data).hexdigest(),
        "SHA-1": lambda data: hashlib.sha1(data).hexdigest(),
        "RIPEMD-160": lambda data: hashlib.new("ripemd160", data).hexdigest(),
        "SHA-224": lambda data: hashlib.sha224(data).hexdigest(),
        "SHA3-224": lambda data: SHA3_224.new(data).hexdigest(),
        "SHA-256": lambda data: hashlib.sha256(data).hexdigest(),
        "SHA3-256": lambda data: SHA3_256.new(data).hexdigest(),
        "SHA-384": lambda data: hashlib.sha384(data).hexdigest(),
        "SHA3-384": lambda data: SHA3_384.new(data).hexdigest(),
        "SHA-512": lambda data: hashlib.sha512(data).hexdigest(),
        "SHA3-512": lambda data: SHA3_512.new(data).hexdigest(),
        "Blake2b": lambda data: BLAKE2b.new(data).hexdigest(),
    }

    with open(wordlist, 'r', encoding='utf-8', errors='ignore') as file:
        for line in file:
            password_candidate = line.strip()

            # Gestion spécifique pour bcrypt
            if hash_type == "Bcrypt":
                try:
                    if bcrypt.checkpw(password_candidate.encode('utf-8'), hash.encode('utf-8')):  # Corrigez cette partie
                        return password_candidate
                except Exception as e:
                    print(f"Erreur bcrypt : {e}")  # Pour déboguer
                    continue



            # Autres types de hachages
            elif hash_type in hash_funcs:
                hash_func = hash_funcs[hash_type]
                hash_candidate = hash_func(password_candidate.encode('utf-8'))
                if hash_candidate == hash:
                    return password_candidate
            else:
                raise ValueError(f"Type de hash inconnu : {hash_type}")

    return None
