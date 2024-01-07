import subprocess
import os


result = subprocess.run("dir", shell=True, capture_output=True, text=True)

repertoire_media = r"C:\Users\Florian\Desktop\projets_random\ytdownload\media"

os.chdir(repertoire_media)

# Exécuter la commande "dir" via l'interpréteur de commandes
result = subprocess.run("dir", shell=True, capture_output=True, text=True)

# Afficher la sortie
print("Sortie de la commande dir:")
print(result.stdout)

# Afficher le code de retour
print("Code de retour:", result.returncode)
