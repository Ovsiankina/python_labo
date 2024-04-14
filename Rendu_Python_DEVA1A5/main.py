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

    parsedKey = [characters for characters in cle]

    notEncryptedFile = open(fichierEntree, 'r')
    notEncryptedFileString = notEncryptedFile.read()

    encryptedFile = open(fichierSortie, 'w')

    for character in notEncryptedFileString:

        if j >= len(parsedKey):
            j = 0

        # Check if special character
        if character.isalpha():
            positionInput = a.index(character.lower())
            positionKey = a.index(parsedKey[j]) 
            
            # TexteChiffré[i] = (TexteClaire[i] + Clés[i]) modulo 26
            encryptedCharacter = (positionInput + positionKey)%26 # position of key 

            if args.verbose:
                # Prevent trailing whitespace when printing
                verbose = f"""
                                === VERBOSE ===
                                char:{character} + key:{parsedKey[j]} => {a[encryptedCharacter]}.
                                key index = {positionKey}
                        """
                print(verbose)

            ## Check if character is caps
            if not character.isupper():
                encryptedFile.write(a[encryptedCharacter])
            else:
                print(f"{character} is upper")
                print("")
                encryptedFile.write(a[encryptedCharacter].upper())

            # j is here to prevent the key from "moving" when special characters
            j += 1

        elif not character.isalpha():
            if args.verbose:

                print(f"""
                                '{character}' is not alpha
                                NO CHANGES
                """)
            encryptedFile.write(character)
        # Count loop 
        i += 1

def Dechiffrement(fichierEntree, cle, fichierSortie, alphabet):

    i = 0
    j = 0
    a = alphabet

    parsedKey = [characters for characters in cle]

    encryptedFile = open(fichierEntree, 'r')
    encryptedFileString = encryptedFile.read()

    notEncryptedFile = open(fichierSortie, 'w')

    for character in encryptedFileString:

        if j >= len(parsedKey):
            j = 0

        # Check if special character
        if character.isalpha():
            positionInput = a.index(character.lower())
            positionKey = a.index(parsedKey[j]) 
            
            # TexteClaire[i] = (TexteChiffré[i] - Clés[i]) modulo 26
            decryptedCharacter = (positionInput - positionKey)%26 # position of key 

            if args.verbose:
                # Prevent trailing whitespace when printing
                verbose = f"""
                                === VERBOSE ===
                                char:{character} + key:{parsedKey[j]} => {a[decryptedCharacter]}.
                                key index = {positionKey}
                        """
                print(verbose)

            ## Check if character is caps
            if not character.isupper():
                notEncryptedFile.write(a[decryptedCharacter])
            else:
                print(f"{character} is upper")
                print("")
                notEncryptedFile.write(a[decryptedCharacter].upper())

            # j is here to prevent the key from "moving" when special characters
            j += 1

        elif not character.isalpha():
            if args.verbose:

                print(f"""
                                '{character}' is not alpha
                                NO CHANGES
                """)
            notEncryptedFile.write(character)
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
