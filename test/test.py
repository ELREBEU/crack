import hashid

hash_str = '2bc813c71ca8c5bc7f60b5ecdfb2e1da'  # Exemple de hash
hash_obj = hashid.HashID()

result = list(hash_obj.identifyHash(hash_str))


print("Type de hash probable :", result)


