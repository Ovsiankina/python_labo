import sys, os, argparse

##############################################################################
# ARGPARSE
##############################################################################

parser = argparse.ArgumentParser()

# Positional arguments 
parser.add_argument('fichierEntrée',
                    help="Definit le fichier d'entrée qui sera chiffré ou déchiffré")

parser.add_argument('Clé',
                    help="Definit la clé qui sera utilisée pour chiffrer ou déchiffrer")

parser.add_argument('fichierSortie',
                    help="Definit le fichier de sortie ou le resultat sera stocké")

# Optional arguments
# group prevent the use of both 'chiffrement' and 'déchiffrement' at the same time
group = parser.add_mutually_exclusive_group()

group.add_argument('-c',
                    '--chiffrement',
                    action="store_true",
                    help="Permet de specifier l'action de chiffrement")

group.add_argument('-d',
                    '--déchiffrement',
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

    elif args.déchiffrement:
        return "déchiffrement"

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
    input_file = open(args.fichierEntrée, 'r')
    # Get the key
    key = args.Clé

    # Generate a string that contains all the lowercased alphabet letters
    # getAlphabet a funciton to improve readability
    letters = getAlphabet()
    # count number of letters
    letter_count = len(letters)

    # Get the content of the input_file as a string
    input_string = input_file.read()

    # Convert the key into an array
    key_list = [characters for characters in key]

    # Define the return value of the function
    output_string = ''

    # Translate every characters one by one
    # chosen_option tells this function if it need to encrypt or decrypt the characters
    j = 0 
    for character in input_string:
    
        # Check if we run out of key characters
        if j >= len(key_list):
            # If we ran out of character: set the key index we work with to 0
            j = 0
    
        # Check if character is a letter (checked as lowercased)
        if character.lower() in letters:
            # Modify the letter
            output_character_index = vigenereOperationOnLetter(
                letters,
                letter_count,
                j,
                character,
                key_list
            )

            letter = revertBackToLetter(letters, character, output_character_index)
            # Insert the character into the output_string
            output_string = output_string + letter

            # j is here to prevent the key from "moving" when special characters
            j += 1
    
        # If character not a letter or is an accentuated letter we just insert it without modifications into the string
        else:
            output_string = output_string + character

    print(f"Le {chosen_option} s'est déroulé avec succès.")

    input_file.close()
    print(f"Le fichier {args.fichierEntrée} été correctement fermé")

    writeOutputFile(output_string)
    
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

def vigenereOperationOnLetter(letters, letter_count, j, character, key_list):
    """ Do the vigenere arithmetic operation on input file character indexes

    This function uses character indexes from the alphabet, input file and
    from the key to calculate a new index according to the user's option
    choice.

    Args:
        letters (str)       : The entire lowercapped english alphabet.
        letter_count (int)  : The number of letters in the enligsh alphabet.
        j (int)             : The current loop count.
        character (str)     : The current letter to be modified.
        key_list (list)     : The entire key chosen by the user.

    Returns:
        int: The modified character index to be converted back into a letter.
    """

    character_index = letters.index(character.lower())
    key_index = letters.index(key_list[j]) 

    # Translate characters using array indexes
    if chosen_option == "chiffrement":
        output_character_index = (character_index + key_index) % letter_count # position of key 

    elif chosen_option == "déchiffrement":
        output_character_index = (character_index - key_index) % letter_count # position of key 

    else:
        parser.error("Une option est requise. Utilisez l'option --help pour plus d'informations")

    return output_character_index


# Revert back the indexe into a letter
def revertBackToLetter(letters, letter, new_index):
    """ Revert the index back into a string letter

    Check letter capitalization to maintain then search the modified letter
    using the new index calculated by vigenereOperationOnLetter()

    Args:
        letters (str)       : The entire lowercapped english alphabet.
        letter (str)        : The current not yet modified letter.
        new_index (int)     : The new calculated index.

    Returns:
        str: The new letter which will be written in the output file
    """
    # If letter is uppercased, insert it as an uppercased letter
    if letter.isupper():
        return letters[new_index].upper()
    # Else insert the letter as it is
    else:
        return letters[new_index]

def writeOutputFile(output_string):
    """ Write the result into the chosen output file

    Receive the output string from main() and write it into the chosen
    output file. Then ends the program proprely.

    Args:
        output_string (str)  : The entire encrypted or decrypted input file.

    Returns:
        str: An string containing all the english alphabet letters.
    """
    # Open output file in write mode
    output_file = open(args.fichierSortie, 'w')
    # Write the output into the output file
    output_file.write(output_string)
    print(f"Le fichier {args.fichierSortie} à été écrit.")

    output_file.close()
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
    chosen_option = getOptionnalArgument()

    main()
