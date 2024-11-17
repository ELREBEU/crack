import argparse

parser = argparse.ArgumentParser(prog='crack', description='Optional app description')

parser.add_argument('--wordlist', type=str)

args = parser.parse_args()

print(args.wordlist)