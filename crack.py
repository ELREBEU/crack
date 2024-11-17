import argparse

parser = argparse.ArgumentParser(prog='crack', description='Optional app description')

parser.add_argument('--wordlist', type=str, required=True, help='Chemin vers la liste de mots')

parser.add_argument('-m', type=str, default=None, help='Type de hash')

parser.add_argument('-u', type=str, default=None, help='URL for website')




typeHash = parser.parse_args().typeHash


args = parser.parse_args()

wordlist = args.wordlist

print(wordlist)
print(typeHash)