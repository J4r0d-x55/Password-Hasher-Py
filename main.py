from cryptography.fernet import Fernet

'''def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)'''

def load_key():
    file = open("key.key", "rb")
    key = file.read()
    file.close()
    return key

key = load_key()
fer = Fernet(key)

def view():
    with open("passwords.txt", 'r') as f:
        for line in f.readlines():
            data = line.rstrip()
            user, passw = data.split("|")
            print("Utilisateur:", user, "Mot de passe:", fer.decrypt(passw.encode()).decode())

def add():
    name = input("Nom de compte: ")
    pwd = input("Mot de passe: ")

    with open("passwords.txt", 'a') as f:
        f.write(name + "|" + fer.encrypt(pwd.encode()).decode() + "\n")

while True:
    mode = input("Voulez-vous ajouter un nouveau mot de passe ou voir ceux existant (voir, ajouter), appuyer sur q pour quitter? ").lower()
    if mode == "q":
        break
    if mode == "voir":
        view()
    elif mode == "ajouter":
        add()
    else:
        print("Choix invalide")
        continue


