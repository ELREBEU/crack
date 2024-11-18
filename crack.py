import argparse


parser = argparse.ArgumentParser(prog='crack', description='Optional app description')
parser.add_argument('--wordlist', type=str, required=True, help='Chemin vers la liste de mots')
parser.add_argument('-h', type=str, required=True, help='The hash')
parser.add_argument('-m', type=str, default=None, help='Type de hash')
parser.add_argument('-u', type=str, default=None, help='URL for website')
parser.add_argument('-i', type=str, default=None, help='Pour interface')

wordlist = parser.parse_args().wordlist
hash = parser.parse_args().h
typeHash = parser.parse_args().m
URL = parser.parse_args().u
interface = parser.parse_args().i

def identifyHash(hash):
    print("Code pour identifier le hash")

def decodeHash(hash,wordlist,typeHash):
    print("Code pour décoder le hash")


print(wordlist)
print(typeHash)