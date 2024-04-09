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
parser.add_argument('-c',
                    '--chiffrement',
                    action="store_true",
                    required=False,
                    help="Permet de specifier l'action de chiffrement")

parser.add_argument('-d',
                    '--dechiffrement',
                    type=str,
                    required=False,
                    help="Permet de specifier l'action de dechiffrement")

def Vigenere (args.fichierEntree,args.Cle,args.fichierSortie)
    

if __name__ == "__main__":
    print("""
    -------------
    Test argparse
    -------------
    """)

    args = parser.parse_args()

    if args.chiffrement:
        print(f'cle: {args.Cle}')

        inputText = open(args.fichierEntree)
        print(inputText.read())

    if args.dechiffrement:
        print(f'Dechiffrement value: {args.dechiffrement}')
