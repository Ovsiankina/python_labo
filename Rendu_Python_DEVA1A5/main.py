import sys, os, argparse

##############################################################################
# ARGPARSE
##############################################################################

parser = argparse.ArgumentParser(description='description : argparse test')

# Positional arguments 
parser.add_argument('fichierEntrée',
                    help="Definit le fichier d'entrée qui sera chiffré ou dechiffré")

parser.add_argument('Clé',
                    help="Definit la clé qui sera utilisée pour chiffrer ou déchiffrer")

parser.add_argument('fichierSortie',
                    help="Definit le fichier de sortie ou le resultat sera stocké")

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
                    help="Permet de specifier l'action de déchiffrement")

##############################################################################
# FUNCTIONS
##############################################################################

def checkInputFile():
    """ Check if input file is in the same directory as main.py """

    if not os.path.exists(args.fichierEntrée):
        print(f"Erreur: Le fichier {args.fichierEntrée} n'existe pas.")
        # Program cannot run without input file. End program execution now.
        sys.exit()

def getOptionnalArgument():
    """ Get the optionnal argument the user chose

    Displays an error if the user chose no optionnal argument
    """
    
    if args.chiffrement:
        return "chiffrement"

    elif args.dechiffrement:
        return "dechiffrement"

    # If no option was correctly chosen, return an error
    parser.error("Une option est requise. Utilisez l'option --help pour plus d'informations")

def main():
    """ Create an output string derived from an input string

    Get all characters in the input file. Modify each alphabetical character
    according to user's choice while maintaining the capitalization.
    Modify neither non-alphebatical characters nor accentuated letters.
    Then sends its output to the function writeOutputFile()

    """
    # Open input file in read mode and get content
    inputFile = open(args.fichierEntrée, 'r')
    # Get the key
    key = args.Clé

    # Generate a string that contains all the lowercased alphabet letters
    # getAlphabet a funciton to improve readability
    letters = getAlphabet()
    # count number of letters
    lettersCount = len(letters)

    # Get the content of the inputFile as a string
    inputString = inputFile.read()

    # Convert the key into an array
    keyList = [characters for characters in key]

    # Define the return value of the function
    outputString = ''

    # Translate every characters one by one
    # chosenOption tells this function if it need to encrypt or decrypt the characters
    j = 0 
    for character in inputString:
    
        # Check if we run out of key characters
        if j >= len(keyList):
            # If we ran out of character: set the key index we work with to 0
            j = 0
    
        # Check if character is a letter (checked as lowercased)
        if character.lower() in letters:
            # Modify the letter
            outputCharacterIndex = vigenereOperationOnLetter(
                letters,
                lettersCount,
                j,
                character,
                keyList
            )

            letter = revertBackToLetter(letters, character, outputCharacterIndex)
            # Insert the character into the outputString
            outputString = outputString + letter

            # j is here to prevent the key from "moving" when special characters
            j += 1
    
        # If character not a letter or is an accentuated letter we just insert it without modifications into the string
        else:
            outputString = outputString + character

    print(f"Le {chosenOption} s'est déroulé avec succès.")

    inputFile.close()
    print(f"Le fichier {args.fichierEntrée} été correctement fermé")

    writeOutputFile(outputString)
    
def getAlphabet():
    """ Produce and return an array of all the english letters

    Load all letters as unicode. For each letter as i, append it as to an
    empty string.

    Returns:
        str: An string containing all the english alphabet letters.
    """
    # Create a string of number rangin from letter 'a' to 'z'
    letters = ''.join(chr(i) for i in range(ord('a'), ord('z')+1))

    return letters

def vigenereOperationOnLetter(letters, lettersCount, j, character, keyList):
    """ Do the vigenere arithmetic operation on input file character indexes

    This function uses character indexes from the alphabet, input file and
    from the key to calculate a new index according to the user's option
    choice.

    Args:
        letters (str)       : The entire lowercapped english alphabet.
        lettersCount (int)  : The number of letters in the enligsh alphabet.
        j (int)             : The current loop count.
        character (str)     : The current letter to be modified.
        keyList (list)      : The entire key chosen by the user.

    Returns:
        int: The modified character index to be converted back into a letter.
    """

    characterIndex = letters.index(character.lower())
    keyIndex = letters.index(keyList[j]) 

    # Translate characters using array indexes
    if chosenOption == "chiffrement":
        outputCharacterIndex = (characterIndex + keyIndex) % lettersCount # position of key 

    elif chosenOption == "dechiffrement":
        outputCharacterIndex = (characterIndex - keyIndex) % lettersCount # position of key 

    else:
        parser.error("Une option est requise. Utilisez l'option --help pour plus d'informations")

    return outputCharacterIndex


# Revert back the indexe into a letter
def revertBackToLetter(letters, letter, newIndex):
    """ Revert the index back into a string letter

    Check letter capitalization to maintain then search the modified letter
    using the new index calculated by vigenereOperationOnLetter()

    Args:
        letters (str)       : The entire lowercapped english alphabet.
        letter (str)        : The current not yet modified letter.
        newIndex (int)      : The new calculated index.

    Returns:
        str: The new letter which will be written in the output file
    """
    # If letter is uppercased, insert it as an uppercased letter
    if letter.isupper():
        return letters[newIndex].upper()
    # Else insert the letter as it is
    else:
        return letters[newIndex]

def writeOutputFile(outputString):
    """ Write the result into the chosen output file

    Receive the output string from main() and write it into the chosen
    output file. Then ends the program proprely.

    Args:
        outputString (str)  : The entire encrypted or decrypted input file.

    Returns:
        str: An string containing all the english alphabet letters.
    """
    # Open output file in write mode
    outputFile = open(args.fichierSortie, 'w')
    # Write the output into the output file
    outputFile.write(outputString)
    print(f"Le fichier {args.fichierSortie} à été écrit.")

    outputFile.close()
    print(f"Le fichier {args.fichierSortie} à été correctement fermé")

    # Proprely end the program
    sys.exit()

##############################################################################
# MAIN
##############################################################################

# variable camel and fun too ?? no mistake correct this
if __name__ == '__main__':

    ### Global variable declaration ###

    # Get user input from argparse arguments
    args = parser.parse_args()
    
    # Check if input file is present before starting the main program
    checkInputFile()

    # Check what the user chose to do between "Chiffrement" and "Dechiffrement"
    # We get the optionnal argument here so that is error, no file were opened yet
    # also make the var accessible anywhere
    chosenOption = getOptionnalArgument()

    main()
