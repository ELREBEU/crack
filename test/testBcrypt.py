import time
import bcrypt

# Hachage bcrypt (le hachage que vous voulez casser)
hash_to_crack = b"$2y$12$Dwt1BZj6pcyc3Dy1FWZ5ieeUznr71EeNkJkUlypTsgbX1H68wsRom"

# Fonction pour tester un mot de passe contre le hachage
def test_password(password):
    return bcrypt.checkpw(password.encode('utf-8'), hash_to_crack)

# Liste de mots de passe courants à tester (dictionnaire simplifié)
passwords_to_test = ["password", "123456", "monMotDePasse", "letmein", "admin", "hae"]

# Essayer chaque mot de passe dans le dictionnaire
t1 = time.time()
for password in passwords_to_test:
    if test_password(password):
        print(f"Le mot de passe est : {password}")
        break
else:
    print("Le mot de passe n'a pas été trouvé dans le dictionnaire.")
t2 = time.time()
print(t2 - t1)
