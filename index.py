
import sys
import os
import pytesseract # Tesseract OCR needs to be installed
from PIL import Image
from typing import List
from rich.progress import track


def get_data_file_path(relative_path):
    # Obtient le chemin absolu du répertoire du script en cours d'exécution
    script_dir = os.path.dirname(os.path.abspath(__file__))

    # Construit le chemin complet du fichier de données en utilisant le chemin du script et le chemin relatif
    data_file_path = os.path.join(script_dir, relative_path)

    return data_file_path

# Get first param of the script if exists
testMode: bool = False

if len(sys.argv) > 1:
    param = sys.argv[1]
    if param == "-test":
        testMode = True

# Set tesseract path
if testMode:
    # Here you need to set the path to tesseract.exe if it's not in the PATH environment variable
    pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
else:
    # Find the path to tesseract.exe in the data directory
    pytesseract.pytesseract.tesseract_cmd = get_data_file_path('tesseract.exe') # Path to tesseract.exe

# if param is empty, ask the user for a directory path
param: str = input("Entrez un chemin de répertoire : ")

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

# Ask the user to press enter
input("Appuyez sur entrée pour terminer...")