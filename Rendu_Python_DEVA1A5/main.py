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

def Chiffrement(fichierEntree, cle, fichierSortie, alphabet):

    i = 0
    j = 0
    a = alphabet

    parsedKey = [characters for characters in cle]

    notEncryptedFile = open(fichierEntree, 'r')
    notEncryptedFileString = notEncryptedFile.read()

    encryptedFile = open(fichierSortie, 'a')

    for character in notEncryptedFileString:

        if j >= len(parsedKey):
            j = 0

        positionInput = a.index(character) 
        positionKey = a.index(parsedKey[j]) 
        
        # TexteChiffré[i] = (TexteClaire[i] + Clés[i]) modulo 26
        encryptedCharacter = (positionInput + positionKey)%26 # position of key 

        print(f"""
                {character} + {parsedKey[j]} => {a[encryptedCharacter]}
                key index = {positionKey}
            """)

        encryptedFile.write(a[encryptedCharacter])
        
        i += 1
        j += 1


def Dechiffrement(fichierEntree, cle, fichierSortie, alphabet):
    print(f"{fichierEntree}, {cle}, {fichierSortie}, {alphabet}")

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
