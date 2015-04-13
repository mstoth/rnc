# RNC or Roman Numeral Calculator
# Written by Michael Toth

def add(augend, addend):
    if not isinstance(addend, basestring):
        raise ValueError
    if addend == 'V':
        raise ValueError
    return augend + addend
    
