import argparse
from Identify import identify
from CrackHash import crackHash

parser = argparse.ArgumentParser(prog='crack', description='Optional app description')
parser.add_argument('--wordlist', type=str, required=True, help='Chemin vers la liste de mots')
parser.add_argument('-hash', type=str, required=True, help='The hash')
parser.add_argument('-salt', type=str, default=None, help='Sel du hash')
parser.add_argument('-m', type=str, default=None, help='Type de hash')
parser.add_argument('-u', type=str, default=None, help='URL for website')
parser.add_argument('-i', type=str, default=None, help='Pour interface')

wordlist = parser.parse_args().wordlist
hash = parser.parse_args().hash
hash = hash.lower() #Pour tout mettre en minuscule si le hash est en majucule
typeHash = parser.parse_args().m
URL = parser.parse_args().u
interface = parser.parse_args().i


def identifyHash(hash):
    hash = hash.lower()
    hash_type = identify.identify(hash)
    print(f"Type de hash identifié : {hash_type}")  # Ajout pour débogage
    return hash_type



def decodeHash(hash, wordlist, typeHash):
    if not typeHash:
        print("Aucun type de hachage détecté.")
        return None

    if not isinstance(typeHash, list):
        typeHash = [typeHash]

    for i in range(len(typeHash)):
        print(f"Débogage : tentative avec type {typeHash[i]}")  # Ajout pour le débogage
        try:
            crack = crackHash.decode_hashHexa(hash, wordlist, typeHash[i])
            if crack is not None:
                return crack
        except ValueError as e:
            print(f"Erreur : {e}")  # Gestion des erreurs pour type inconnu
    return None





def main(hash,wordlist):
    type = identifyHash(hash)
    mdp_trouvee = decodeHash(hash,wordlist,type)
    print(mdp_trouvee)


main(hash, wordlist)