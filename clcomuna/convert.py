import unicodedata
import csv
from fuzzywuzzy import process

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
    with open('data/comunas.csv', newline='') as csvfile:
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
