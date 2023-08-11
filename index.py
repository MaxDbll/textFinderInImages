
import sys
import os
import pytesseract # Tesseract OCR needs to be installed
from PIL import Image
from typing import List
from rich.progress import track

# Get first param of the script if exists
param: str = ""
if len(sys.argv) > 1:
    param = sys.argv[1]

# if param is empty, ask the user for a directory path
if param == "":
    param = input("Entrez un chemin de répertoire : ")

# Check if param is a directory path
if not os.path.isdir(param):
    print("Le répertoire n'existe pas")
    exit()

# Ask the user for words to search separated by ;
wordsList: str = input("Entrez les mots à rechercher séparés par un point-virgule : ")
# words string to list
words: List[str] = wordsList.split(";")

if (len(words) == 0):
    print("Vous devez entrer un mot")
    exit()

# Get all files in the directory
files: List[str] = os.listdir(param)

# List of files that contains required words
res: List[str] = []

# Loop through all files
for file in track(files, description="Traitement des fichiers"):
    # Check if file is an image
    if not (file.endswith(".jpg") or file.endswith(".png") or file.endswith(".jpeg")):
        continue

    # Open the image
    img = Image.open(param + "/" + file)

    # Convert image to text
    text: str = pytesseract.image_to_string(img)

    # Check if word is in the text
    for word in words:
        if word.lower().strip() in text.lower():
            print("Le mot '" + word + "' est dans le fichier " + file)
            res.append(file)

# Check if there is any result
if len(res) == 0:
    print("Aucune correspondance trouvée")
    exit()

# Ask the user to press enter
input("Appuyez sur entrée pour terminer...")