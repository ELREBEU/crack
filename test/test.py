import hashid

hash_str = '$2y$12$Dwt1BZj6pcyc3Dy1FWZ5ieeUznr71EeNkJkUlypTsgbX1H68wsRom'  # Exemple de hash
hash_obj = hashid.HashID()

result = list(hash_obj.identifyHash(hash_str))


print("Type de hash probable :", result)


