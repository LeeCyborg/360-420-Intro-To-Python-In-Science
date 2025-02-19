def insertAtIndex(str, i, substring):
    '''
    insert substring into str at index i and return updated string
    :param str: string with family, genus, species triples separated by commas and space
    :param i: integer index where substring should be inserted
    :param substring: the substring insterted into str
    :return: str, the updated string after the insertion of substring at index i
    '''
    updated_str = str[:i] + substring + str[i:]
    return updated_str


def lastSpecies(str, species):
    '''
    determine if species is the last word in str
    :param str: string with family, genus, species triples separated by commas and space
    :param species: name of a specific species
    :return : True if species is the last word in str.  Otherwise, return False
    '''
    index = str.find(species)
    num_char_species = len(species)

    if (index + num_char_species) == len(str):
        return True
    return False



my_string = "cats"
string_length = len(my_string)
# I can test if my outcome is as expected: 
print(string_length)

# Or, my_string = input("what is the animal?")
if my_string == "cats":
    print("its cats!")

if my_string == "CATS":
    print("is it cats?")

my_string = my_string.upper()

if my_string == "CATS":
    print("is it cats?")

def numSpecies(str, species):
    '''
    if species appears in str only once, insert species in capital letters 3 times in str 
    after the first occurrence
    :param str: string of family, genus, species triples separated by comma and a space
    :param species: name of specific species
    :return : updated_str that may include species repeated 3 times in capital letters
    '''
    count = str.count(species)          # count number of times species appears in str
    index = str.find(species)           # starting index of first occurrance of species in str
    insertion_index = index + len(species) + 2    # index after comma/space of first occurrence of species in str 
   
    if species not in str:
        return str
    elif count > 1:
        return str
    elif not lastSpecies(str, species): 
        repeated_species = f'{species.upper()}, '*3
    else:
        repeated_species = f', {species.upper()}'*3

    str_updated = insertAtIndex(str, insertion_index, repeated_species)
    return str_updated


def numGenus(str):
    '''
    compute the number of genus in the given string str
    :param str: string of family, genus, species triples separated by comma and a space
    :return : the number of genus in str
    '''
    num_genus = str.count(', ') + 1
    num_triples = num_genus//3   
    return num_triples



s = 'Canidae, Canis, CanisLupus, Felidae, Felis, FelisCatus'
updated_str = numSpecies(s, 'CanisLupus')

print(numSpecies(s, "Felis"))
print(f'Original set of triples: {s}')
print(f'Updated set of triples: {updated_str}')
print(f'The number of genus is: {numGenus(s)}')

