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

def Chiffrement(characterIndex, keyIndex, vigenereCharactersLength):
    # TexteChiffré[i] = (TexteClaire[i] + Clés[i]) modulo 26
    return (characterIndex + keyIndex)%vigenereCharactersLength # position of key 

def Dechiffrement(characterIndex, keyIndex, vigenereCharactersLength):
    # TexteClaire[i] = (TexteChiffré[i] - Clés[i]) modulo 26
    return (characterIndex - keyIndex)%vigenereCharactersLength # position of key 

def endProgram():
    # Close files
    inputFile.close()
    outputFile.close()

    # Exit the programm
    sys.exit

if __name__ == "__main__":

    # Characters used for the vigenere encryption
    vigenereCharacters = [
        'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
        'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
    ]
    vigenereCharactersLength = len(vigenereCharacters)

    args = parser.parse_args()
    
    # Check if input file exists
    if not os.path.exists(args.fichierEntree):
        print(f"Erreur: Le fichier {args.fichierEntree} n'existe pas")
        endProgram()

    # Open input file in read mode and get content
    inputFile = open(args.fichierEntree, 'r')
    inputString = inputFile.read()

    # Tranform the key into an array
    key = args.Cle
    keyString = [characters for characters in key]

    # Open output file in write mode
    outputFile = open(args.fichierSortie, 'w')
    outputString = ''
    outputCharacterIndex = 0

    i = 0
    j = 0

    for character in inputString:

        if j >= len(keyString):
            j = 0

        """
            Check if the current character is alphabetic

            If yes, it'll convert both the current key and character into
            the correct alphabet[indexes] and do calculations with these indexes.

            Then converts back the alphabet[index] into a letter which can be
            written into the output file.
        """
        if character.isalpha() and (character.lower() in vigenereCharacters):
            print(character)
            characterIndex = vigenereCharacters.index(character.lower())
            keyIndex = vigenereCharacters.index(keyString[j]) 

            if args.chiffrement:
                outputCharacterIndex = int(Chiffrement(characterIndex, keyIndex, vigenereCharactersLength))
            elif args.dechiffrement:
                outputCharacterIndex = int(Dechiffrement(characterIndex, keyIndex, vigenereCharactersLength))
            else:
                parser.error("Une option est requise. Utilisez l'option --help pour plus d'informations")

            ## Check if character is caps
            if not character.isupper():
                outputString = outputString + vigenereCharacters[outputCharacterIndex]
            else:
                outputString = outputString + vigenereCharacters[outputCharacterIndex].upper()

            # j is here to prevent the key from "moving" when special characters
            j += 1

        # If character not alpha or is an accentuated letter we just insert it without modifications into the array
        else:
            outputString = outputString + character

        # Count loop 
        i += 1

    # Write the output into the output file
    outputFile.write(outputString)
    # End of program. Closing files
    endProgram()
