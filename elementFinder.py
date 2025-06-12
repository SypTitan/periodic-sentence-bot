
elements = {'a':['Ac','Ag','Al','Am','Ar','As','At','Au'],
            'b':['B','Ba','Be','Bh','Bi','Bk','Br'],
            'c':['C','Ca','Cd','Ce','Cf','Cl','Cm','Cn','Co','Cr','Cs','Cu'],
            'd':['Db','Ds','Dy'],
            'e':['Er','Es','Eu'],
            'f':['F','Fe','Fl','Fm','Fr'],
            'g':['Ga','Gd','Ge'],
            'h':['H','He','Hg','Ho','Hs'],
            'i':['I','In','Ir'],
            'j':[],
            'k':['K','Kr'],
            'l':['La','Li','Lr','Lu','Lv'],
            'm':['Mc','Md','Mg','Mn','Mo','Mt'],
            'n':['N','Na','Nb','Nd','Ne','Nh','Ni','No','Np'],
            'o':['O','Og','Os'],
            'p':['P','Pa','Pb','Pd','Pm','Po','Pr','Pt','Pu'],
            'q':[],
            'r':['Ra','Rb','Re','Rf','Rg','Rh','Rn','Ru'],
            's':['S','Sb','Sc','Se','Sg','Si','Sm','Sn','Sr'],
            't':['Ta','Tb','Tc','Te','Th','Ti','Tl','Tm','Ts'],
            'u':['U'],
            'v':['V'],
            'w':['W'],
            'x':['Xe'],
            'y':['Y','Yb'],
            'z':['Zn','Zr'],
            }

MAX_REPEATS = 3
MIN_VARIETY = 3

def recreate_string(original: str, alphabet: dict = elements) -> str:
    """
    Recreate a string from the alphabet dictionary.
    Main function, wrapping preprocessing and processing.
    """
    # Pre-processing
    original = remove_emojis(original)
    toProcess = [char.lower() for char in original if char.isalpha()]
    toProcess = ''.join(toProcess)
    # Processing
    out = __add_to_string(toProcess, alphabet)
    # Post-processing
    if (len(set(out.split(' ')[:-1])) <= MIN_VARIETY and len(toProcess) >= 2*MIN_VARIETY):
        return '?'
    return out
    

def remove_emojis(original: str) -> str:
    """
    Removes discord emojis from a string.
    """
    original += ' '
    splits = original.split(':')
    # Loop over all spaces enclosed by :
    # Remove any that only consist of lowercase characters and are 2-32 characters long
    for i in range(1, len(splits), 2):
        if splits[i].isalpha() and splits[i].islower() and len(splits[i]) > 1 and len(splits[i]) < 33:
            splits[i] = ""
    return ''.join(splits)
    
def __add_to_string(original: str, alphabet: dict) -> str:
    """
    Add to a string from the alphabet dictionary.
    Uses recursive DFS to add single elements to the output.
    """
    # Handle edge cases
    if len(original) == 0:
        return ''
    if original[0] not in alphabet:
        raise ValueError("Invalid character in string.")
    
    # Limit options
    options = alphabet[original[0]]
    if len(options) == 0:
        return '?'
    
    # Find optimal option
    for option in reversed(options):
        output: str = option + ' '
        if (len(option) == 1):
            # Single-character element is guaranteed to fit
            output += __add_to_string(original[1:], alphabet)
        else:
            # Multi-character element might not fit with following chars
            if (len(option) > len(original)):
                continue
            # Check all characters, break if element doesn't fit
            for i in range(1,len(option)):
                if option[i] != original[i]:
                    output += '?'
                    break
            else:
                output += __add_to_string(original[len(option):], alphabet)
                
        # Return first fitting element        
        if '?' not in output:
            # Check for double elements
            output_split = output.split(' ')[:-1]
            print(output_split)
            if (len(output_split) < MAX_REPEATS):
                return output
            for i in range(MAX_REPEATS):
                if (output_split[i] != option):
                    return output
    # Give up
    return '?'
                

    

if __name__ == "__main__":
    while 1:
        print(recreate_string(input("Enter a string: \n")))
    