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
group = parser.add_mutually_exclusive_group()

group.add_argument('-c',
                    '--chiffrement',
                    action="store_true",
                    help="Permet de specifier l'action de chiffrement")

group.add_argument('-d',
                    '--dechiffrement',
                    action="store_true",
                    help="Permet de specifier l'action de dechiffrement")

parser.add_argument('-v',
                    '--verbose',
                    action="store_true",
                    help="Description de ce qu'il ce passe")

def Chiffrement(characterIndex, keyIndex):
    # TexteChiffré[i] = (TexteClaire[i] + Clés[i]) modulo 26
   return (characterIndex + keyIndex)%26 # position of key 

def Dechiffrement(characterIndex, keyIndex):
    # TexteClaire[i] = (TexteChiffré[i] - Clés[i]) modulo 26
    return (characterIndex - keyIndex)%26 # position of key 

if __name__ == "__main__":
    print("""
    -------------
    Test argparse
    -------------
    """)

    # Alphabet used in the code
    a = [
        'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
        'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
    ]

    args = parser.parse_args()
    
    # What happens is created but then empty and try decrypt?

    # Check if input file exists
    if not os.path.exists(args.fichierEntree):
        create = open(args.fichierEntree, 'x')
        create.close()
    # Open files and get content
    inputFile = open(args.fichierEntree, 'r')
    inputString = inputFile.read()

    key = args.Cle
    keyString = [characters for characters in key]

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
        if character.isalpha():
            characterIndex = a.index(character.lower())
            keyIndex = a.index(keyString[j]) 

            if args.chiffrement:
                outputCharacterIndex = int(Chiffrement(characterIndex, keyIndex))
            elif args.dechiffrement:
                outputCharacterIndex = int(Dechiffrement(characterIndex, keyIndex))
            else:
                print("Choisissez -c ou -d")
                # force le -h pour expliquer comment utiliser la commande

            if args.verbose:
                # Prevent trailing whitespace when printing
                verbose = f"""
                                === VERBOSE ===
                                char:{character} + key:{keyString[j]} => {a[outputCharacterIndex]}.
                                key index = {keyIndex}
                        """
                print(verbose)

            ## Check if character is caps
            if not character.isupper():
                print(outputString)
                outputString = outputString + a[outputCharacterIndex]
                print(outputString)
            else:
                outputString = outputString + a[outputCharacterIndex].upper()
                print(outputString)

            # j is here to prevent the key from "moving" when special characters
            j += 1

        elif not character.isalpha():
            if args.verbose:
                print(f"""
                                '{character}' is not alpha
                                NO CHANGES
                """)

            outputString = outputString + character
        # Count loop 
        i += 1

    # Write the output into the output file
    print(outputString)
    outputFile.write(outputString)
    # End of program. Closing files
    inputFile.close()
    outputFile.close()
