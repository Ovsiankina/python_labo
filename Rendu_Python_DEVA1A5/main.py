import sys, os, argparse

parser = argparse.ArgumentParser(description='description : argparse test')

# Positional arguments 
parser.add_argument('fichierEntree',
                    help="Definit le fichier d'entree qui sera chiffre ou dechiffre")

parser.add_argument('cle',
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

def Chiffrement(fichierEntree, cle, fichierSortie, alphabet):

    i = 0
    j = 0
    a = alphabet

    keyString = [characters for characters in cle]

    inputFile = open(fichierEntree, 'r')
    inputString = inputFile.read()
    outputFile = open(fichierSortie, 'w')

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
            
            # TexteChiffré[i] = (TexteClaire[i] + Clés[i]) modulo 26
            outputCharacter = (characterIndex + keyIndex)%26 # position of key 

            if args.verbose:
                # Prevent trailing whitespace when printing
                verbose = f"""
                                === VERBOSE ===
                                char:{character} + key:{keyString[j]} => {a[outputCharacter]}.
                                key index = {keyIndex}
                        """
                print(verbose)

            ## Check if character is caps
            if not character.isupper():
                outputFile.write(a[outputCharacter])
            else:
                print(f"{character} is upper")
                print("")
                outputFile.write(a[outputCharacter].upper())

            # j is here to prevent the key from "moving" when special characters
            j += 1

        elif not character.isalpha():
            if args.verbose:
                print(f"""
                                '{character}' is not alpha
                                NO CHANGES
                """)
            outputFile.write(character)
        # Count loop 
        i += 1

def Dechiffrement(fichierEntree, cle, fichierSortie, alphabet):

    i = 0
    j = 0
    a = alphabet

    keyString = [characters for characters in cle]

    inputFile = open(fichierEntree, 'r')
    inputString = inputFile.read()
    outputFile = open(fichierSortie, 'w')

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
            
            # TexteChiffré[i] = (TexteClaire[i] + Clés[i]) modulo 26
            outputCharacter = (characterIndex - keyIndex)%26 # position of key 
            # TexteClaire[i] = (TexteChiffré[i] - Clés[i]) modulo 26

            if args.verbose:
                # Prevent trailing whitespace when printing
                verbose = f"""
                                === VERBOSE ===
                                char:{character} + key:{keyString[j]} => {a[outputCharacter]}.
                                key index = {keyIndex}
                        """
                print(verbose)

            ## Check if character is caps
            if not character.isupper():
                outputFile.write(a[outputCharacter])
            else:
                print(f"{character} is upper")
                print("")
                outputFile.write(a[outputCharacter].upper())

            # j is here to prevent the key from "moving" when special characters
            j += 1

        elif not character.isalpha():
            if args.verbose:
                print(f"""
                                '{character}' is not alpha
                                NO CHANGES
                """)
            outputFile.write(character)
        # Count loop 
        i += 1

if __name__ == "__main__":
    print("""
    -------------
    Test argparse
    -------------
    """)

    alphabet = [
        'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
        'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
    ]

    args = parser.parse_args()
    print(args)

    # What happens is created but then empty and try decrypt?
    if not os.path.exists(args.fichierEntree):
        create = open(args.fichierEntree, 'x')
        create.close()

    if args.chiffrement:
        Chiffrement(args.fichierEntree,args.cle,args.fichierSortie,alphabet)

    elif args.dechiffrement:
        Dechiffrement(args.fichierEntree,args.cle,args.fichierSortie,alphabet)
    else:
        print("Choisissez -c ou -d")
        # force le -h pour expliquer comment utiliser la commande
