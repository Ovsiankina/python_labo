import sys, os, argparse

parser = argparse.ArgumentParser(description='description : argparse test')

# Positional arguments 
parser.add_argument('fichierEntree',
                    help="Definit le fichier d'entree qui sera chiffre ou dechiffre")

parser.add_argument('Cle',
                    help="Definit la cle qui sera utilisee pour chiffrer ou dechiffrer")

parser.add_argument('fichierSortie',
                    help="Definit le fichier de sortie ou le resultat sera stocke")

# Optional arguments
# group prevent the use of both 'chiffrement' and 'dechiffrement' at the same time
group = parser.add_mutually_exclusive_group()

group.add_argument('-c',
                    '--chiffrement',
                    action="store_true",
                    help="Permet de specifier l'action de chiffrement")

group.add_argument('-d',
                    '--dechiffrement',
                    action="store_true",
                    help="Permet de specifier l'action de dechiffrement")

##############################################################################
# FUNCTIONS
##############################################################################

def checkInputFile():
    if not os.path.exists(args.fichierEntree):
        print(f"Erreur: Le fichier {args.fichierEntree} n'existe pas.")
        # Program cannot run without input file. End program execution now.
        sys.exit()

def getOptionnalArgument():
    if args.chiffrement:
        return "chiffrement"

    elif args.dechiffrement:
        return "dechiffrement"

    # If no option was correctly chosen, return an error
    parser.error("Une option est requise. Utilisez l'option --help pour plus d'informations")

def translateFile(inputFile,key):

    # Get the content of the inputFile as a string
    inputString = inputFile.read()

    # Convert the key into an array
    keyString = [characters for characters in key]

    # Define the return value of the function
    outputString = ''

    i = 0
    j = 0
    
    # Translate every characters one by one
    # chosenOption tells this function if it need to encrypt or decrypt the characters
    for character in inputString:
    
        # Check if we run out of key characters
        if j >= len(keyString):
            # If we ran out of character: set the key index we work with to 0
            j = 0
    
        # Check if character is a letter (checked as lowercased)
        if character.lower() in letters:

            # Insert the character into the outputString
            outputString = outputString + vigenereOperationOnLetter(j,character, keyString)

            # j is here to prevent the key from "moving" when special characters
            j += 1
    
        # If character not a letter or is an accentuated letter we just insert it without modifications into the array
        else:
            outputString = outputString + character
    
        # Count loop 
        i += 1

    return outputString

def vigenereOperationOnLetter(j,character, keyString):

    characterIndex = letters.index(character.lower())
    keyIndex = letters.index(keyString[j]) 

    # Translate characters using array indexes
    if chosenOption == "chiffrement":
        outputCharacterIndex = (characterIndex + keyIndex) % lettersNumber # position of key 

    elif chosenOption == "dechiffrement":
        outputCharacterIndex = (characterIndex - keyIndex) % lettersNumber # position of key 

    else:
        parser.error("Une option est requise. Utilisez l'option --help pour plus d'informations")

    # Revert back the indexes into a letter

    # If character is uppercased, insert it as an uppercased letter
    if character.isupper():
        letter = letters[outputCharacterIndex].upper()
    # Else insert the character normally
    else:
        letter = letters[outputCharacterIndex]

    return letter


def endProgram():
    # Close files
    print(f"Les fichiers correctement été fermés/n")
    inputFile.close()
    outputFile.close()

    # Exit the programm
    print(f"Fin du programme")
    sys.exit()

##############################################################################
# MAIN
##############################################################################

### Variable declaration ###

# Create a string of number rangin from letter 'a' to 'z'
letters = ''.join(chr(i) for i in range(ord('a'), ord('z')+1))

# Count the number of letters
lettersNumber = len(letters)

# Get user input from argparse arguments
args = parser.parse_args()

# Check if input file is present
checkInputFile()

# Check what the user chose to do between "Chiffrement" and "Dechiffrement"
chosenOption = getOptionnalArgument()

# Open input file in read mode and get content
inputFile = open(args.fichierEntree, 'r')

# Get the key
key = args.Cle

# Open output file in write mode
outputFile = open(args.fichierSortie, 'w')

# Translate the file using vigenere encryption or decryption
outputString = translateFile(inputFile,key)

# Write the output into the output file
outputFile.write(outputString)

# Close all files and exit the program
endProgram()
