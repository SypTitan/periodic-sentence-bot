
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

def recreate_string(original: str, alphabet: dict = elements) -> str:
    """
    Recreate a string from the alphabet dictionary.
    """
    toProcess = [char.lower() for char in original if char.isalpha()]
    toProcess = ''.join(toProcess)
    return __add_to_string(toProcess, alphabet)
    
def __add_to_string(original: str, alphabet: dict) -> str:
    """
    Add to a string from the alphabet dictionary.
    """
    if len(original) == 0:
        return ''
    if original[0] not in alphabet:
        raise ValueError("Invalid character in string.")
    
    options = alphabet[original[0]]
    if len(options) == 0:
        return '?'
    for option in options:
        output = option + ' '
        if (len(option) == 1):
            output += __add_to_string(original[1:], alphabet)
        else:
            if (len(option) > len(original)):
                continue
            optionFits = True
            for i in range(1,len(option)):
                if option[i] != original[i]:
                    optionFits = False
            if optionFits:
                output += __add_to_string(original[len(option):], alphabet)
            else:
                output += '?'
        if '?' not in output:
            return output
    return '?'
                

    

if __name__ == "__main__":
    while 1:
        print(recreate_string(input("Enter a string: \n")))
    