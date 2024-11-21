from Cryptodome.Hash import MD4

# Fonction lambda pour calculer le hash MD2
hash_md2 = lambda data: MD4.new(data).hexdigest()

# Exemple d'utilisation avec une chaîne de caractères "Hello"
data = b'admin'
print(hash_md2(data))  # Affiche le hash MD2 de 'Hello'
