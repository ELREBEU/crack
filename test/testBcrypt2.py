import bcrypt
from multiprocessing import Pool, cpu_count
import time


hash_to_crack = b"$2y$12$Dwt1BZj6pcyc3Dy1FWZ5ieeUznr71EeNkJkUlypTsgbX1H68wsRom"
test="$2y$12$Dwt1BZj6pcyc3Dy1FWZ5ieeUznr71EeNkJkUlypTsgbX1H68wsRom"
test=f"{test}".encode()



# Liste de mots de passe à tester (à remplacer par un dictionnaire plus grand pour les tests réels)
passwords_to_test = ["password", "123456", "monMotDePasse", "letmein", "admin", "bleh"]

# Fonction pour tester un mot de passe contre le hachage
def test_password(password):
    if bcrypt.checkpw(password.encode('utf-8'), test):
        print(f"Mot de passe trouvé : {password}")
        return True
    return False

# Fonction principale pour utiliser le multiprocessing
def decryptBcrypt():
    t1 = time.time()
    with Pool(cpu_count()) as pool:  # Utilise tous les cœurs disponibles
        results = pool.map(test_password, passwords_to_test)
        if any(results):
            print("Mot de passe cassé avec succès.")
        else:
            print("Aucun mot de passe trouvé.")
    t2 = time.time()
    print(t2 - t1)

print(decryptBcrypt())
