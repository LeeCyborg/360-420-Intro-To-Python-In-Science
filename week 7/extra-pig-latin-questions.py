# by Bennet Axtell, 2025

# #######################
# # PART 1: pigLatinify #
# #######################
# '''
# The function pigLatinify takes one parameter, a word,
# and returns that word in Pig Latin
# To make a word into Pig Latin:
#     1. Find the first vowel in the word (a, e, i, o, u, or y)
#     2. Make a new string that is that first vowel to the end of the string
#     3. Add a hyphen (-) and then the word before the first vowel
#        to that new string
#     4. Finally add the letters 'ay' to the new string
#  Examples:
#   'Benett' becomes 'enett-Bay'
#   'scram' becomes 'am-scray'
#   'Python becomes 'ython-Pay'
# '''




# #Test your function pigLatinify by printing a call to it with a test word:

# #######################
# # PART 2: punctuation #
# #######################
# '''
# Update pigLatinify to keep punctuation after the word
# so 'Welcome!' becomes 'elcome-Way!' instead of 'elcome!-Way'
# You can consider anything that is not a letter to be punctuation for this
# HINT: word.isalpha() returns True if every letter is a-z or A-Z
# and False otherwise
# '''




# #######################
# # PART 2: Why Y?      #
# #######################
# '''
# Update pigLatinify to treat Y (or y) as a consonant when it's the first letter
# but as a vowel after that.
# so 'youth' becomes 'outh-yay' and 'Python' becomes 'ython-Pay'
# HINT: if Y is the first letter, you can assume the second letter is a vowel that
# is not Y
# '''


# ###########################
# # PART 3: Qu is a problem #
# ###########################
# '''
# Update pigLatinify to treat qu (or qu) as a consonant, meaning that the u right
# after a Q is skipped, so 'quiz' becomes 'iz-quay' instead of 'uiz-qay'
# HINT: You can assume the letter after qu is a vowel
# '''

# '''




# print(pigLatinPhrase('Sphinx of black quartz, judge my vow.'))


