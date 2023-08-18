
import requests
import random
import string
import time

print("""
█▀▀ █░░█ █▀▀█ █▀▀█ █▀▀ █▀▀ ▄▀▀▄
█▀▀ █░░█ █▄▄▀ █▄▄█ █░░ █▀▀ ▀▄▄█
▀░░ ░▀▀▀ ▀░▀▀ ▀░░▀ ▀▀▀ ▀▀▀ ░▄▄▀""")
time.sleep(2)
print("Génération de liens Nitro")
time.sleep(0.3)
print("Envoyer une demande d'ami à furace#7474 en cas de bugs\n")
time.sleep(0.2)

num = int(input('Entrez le nombre de codes à générer et à vérifier: '))

with open("Nitro Codes.txt", "w", encoding='utf-8') as file:
    print("Vos codes nitro sont en cours de génération, soyez patient si vous avez saisi le chiffre élevé !")

    start = time.time()

    for i in range(num):
        code = "".join(random.choices(
            string.ascii_uppercase + string.digits + string.ascii_lowercase,
            k = 16
        ))

        file.write(f"https://discord.gift/{code}\n")

    print(f"Generated {num} codes | Time taken: {time.time() - start}\n")

with open("Nitro Codes.txt") as file:
    for line in file.readlines():
        nitro = line.strip("\n")

        url = "https://discordapp.com/api/v6/entitlements/gift-codes/" + nitro + "?with_application=false&with_subscription_plan=true"

        r = requests.get(url)

        if r.status_code == 200:
            print(f" Valid | {nitro} ")
            break
        else:
            print(f" Invalid | {nitro} ")

input("\nVous avez généré, maintenant appuyez sur Entrée pour fermer ceci, vous obtiendrez des codes valides dans Valid Codes.txt si vous voyez qu'il est vide, alors vous n'avez pas de chance, générez 20 millions de codes pour la chance ou autre.")
