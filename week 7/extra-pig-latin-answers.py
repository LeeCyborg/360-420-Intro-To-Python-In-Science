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

# def pigLatinify(word):
#     '''
#     Returns word translated into Pig Latin
#     (all letters before first vowel moved to the end plus 'ay'
#     :param word: string of a single word to make into Pig Latin
#     :return: a new string of the Pig Latin version of word
#     '''
#     first_vowel = 0
#     for ch in word:
#         if ch.lower() in 'aeiouy':
#             return word[first_vowel:] + '-' + word[:first_vowel] + 'ay'
#         first_vowel = first_vowel + 1
#     return word + '-ay' #handle no vowel case


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

# def pigLatinifyPunc(word):
#     '''
#     Returns word translated into Pig Latin keeping a single
#     punctuation mark at the end
#     (all letters before first vowel moved to the end plus 'ay'
#     :param word: string of a single word to make into Pig Latin
#     :return: a new string of the Pig Latin version of word
#     '''
#     first_vowel = 0
#     for ch in word:
#         if ch.lower() in 'aeiouy':
#             if first_vowel == 0 and ch.lower() == 'y':
#                 first_vowel = 1
#             elif first_vowel > 0 and word[first_vowel-1:first_vowel+1].lower() == 'qu':
#                 first_vowel += 1
#             if word[-1].isalpha():
#                 return word[first_vowel:] + '-' + word[:first_vowel] + 'ay'
#             else:
#                 return word[first_vowel:-1] + '-' + word[:first_vowel] + 'ay' + word[-1]
#         first_vowel = first_vowel + 1 #can also do this with find
#     return word + '-ay' #handle no vowel case


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
# def pigLatinifyPunc(word):
#     '''
#     Returns word translated into Pig Latin keeping a single
#     punctuation mark at the end
#     (all letters before first vowel moved to the end plus 'ay'
#     :param word: string of a single word to make into Pig Latin
#     :return: a new string of the Pig Latin version of word
#     '''
#     first_vowel = 0
#     for ch in word:
#         if ch.lower() in 'aeiouy':
#             if first_vowel == 0 and ch.lower() == 'y':
#                 first_vowel = 1
#             elif first_vowel > 0 and word[first_vowel-1:first_vowel+1].lower() == 'qu':
#                 first_vowel += 1
#             if word[-1].isalpha():
#                 return word[first_vowel:] + '-' + word[:first_vowel] + 'ay'
#             else:
#                 return word[first_vowel:-1] + '-' + word[:first_vowel] + 'ay' + word[-1]
#         first_vowel = first_vowel + 1 #can also do this with find
#     return word + '-ay' #handle no vowel case
# ###########################
# # PART 3: Qu is a problem #
# ###########################
# '''
# Update pigLatinify to treat qu (or qu) as a consonant, meaning that the u right
# after a Q is skipped, so 'quiz' becomes 'iz-quay' instead of 'uiz-qay'
# HINT: You can assume the letter after qu is a vowel
# '''

# '''
# word_in = input('Word to translate: ')
# while word_in != '':
#     print(f"{word_in} in Pig Latin is {pigLatinifyPunc(word_in)}")
#     word_in = input('Word to translate: ')
# '''

# def pigLatinPhrase(phrase):
# 	'''
# 	Return phrase with each word translated into Pig Latin
# 	:param phrase: string phrase to be translated
# 	:return: phrase translated into Pig Latin
# 	'''
# 	pig_latin = ''
# 	for word in phrase.split():
# 		pig_latin = pig_latin + ' ' + pigLatinifyPunc(word)
# 	return pig_latin[1:] #cut the first space off

# print(pigLatinPhrase('Sphinx of black quartz, judge my vow.'))


