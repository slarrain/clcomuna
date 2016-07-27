import unicodedata
import csv
from fuzzywuzzy import process
from pkg_resources import resource_filename # For the right filename

def remove_accents(input_str):
    '''
    Removes accents and special characters
    Input:  string
    Output: Modified string
    '''

    nfkd_form = unicodedata.normalize('NFKD', input_str)
    return u"".join([c for c in nfkd_form if not unicodedata.combining(c)])

def comunas_dict():
    '''
    Returns a dictionary with Comuna_name : code
    Reads it from a file comunas.csv on the 'data' directory
    '''
    comunas = {}

    # This is so it gets the correct path+filename and
    # it actually works
    filename = resource_filename(__name__, '../data/comunas.csv')

    with open(filename, newline='') as csvfile:
        data = csv.reader(csvfile, delimiter=',')
        for row in data:
            comunas[row[0]] = row[1]
    return comunas

def get_code(name):
    '''
    Given the name of a comuna, returns the code of that comuna
    Input:  string
    Output: string
    '''

    comuna = remove_accents(name).upper()
    comunas = comunas_dict()

    try:
        return comunas[comuna]
    except Exception as e:
        print ("Could not find code for: ", comuna)

def get_fuzzy(name, show=False, threshold=False):
    '''
    Returns the most similar comuna name.
    Uses the fuzzywuzzy package
    Returns the name (string)
    '''

    comuna = remove_accents(name).upper()
    comunas = comunas_dict()

    comunas_names = list(comunas.keys())    # List of comunas names (choioces)

    best_match = process.extractOne(comuna, comunas_names)

    if show:    #prints the name of the comuna and the score it got
        print (best_match)
    if threshold:   #if the user specifies a threshold
        if best_match[1]<threshold:
            print ("Score lower than minimum threshold for comuna: {0} - {1}".format(comuna, best_match[0]))
            return None
    return best_match[0]    # The name

def get_steps(name, show=False, threshold=False):
    '''
    A wrapper mtehod that uses the 'get_code' function first
    and if it fails, it tries the 'get_fuzzy method'
    Returns the code
    '''

    comuna = get_code(name)
    if comuna==None:
        comuna = get_fuzzy(name, show, threshold)
        if comuna:
            comuna = get_code(comuna)
    return comuna
