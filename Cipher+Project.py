
# coding: utf-8

# # Cipher Project:
# 
# ### The first steps were to load the files into the program. Once they were inserted, I took each line and put them into arrays. I then took the encrypted text and made all of the letters lowercase, while the regular english text was uppercase. Once that was done, I looked for the index of both arrays to see where the letter A and Z were, and then took all the letters in-between to know where the alphabet was. I also did similar things to find the punctuation and other characters to look for in the the text to try and avoid. The last part of the first section was to create a dictionary that had all lowercase letters, with the items to be null, which would then be replaced by the correct letter that corresponds to that encrypted lowercase letter, along with arrays that solved encrypted letters would be assigned to.
# 
# ### The next step was to keep all the punctuation as is, so we could start looking for certain words. The first word that I looked for was I. Since I and A are really the only real one letter words, and I is the only word that can end in a sentence correctly, I looked for the letter that was most commonly followed by a period. That was then assigned I. The next most popular one letter word would then be A in english, so that letter was then assigned to A. The last specific letter to look for would be to have letters that came before " ' ", because that is also typical of an english, specifically O. So that letter that was most common to start off a word followed by an apostrophe was assigned O.
# 
# 
# ### Now that I didn't really need punctuation any longer, I re-did the arrays to make all of them have no punctuation, but left in the other characters in the end because words that had "-" or other specific characters to them would be very minimal in frequency. Once I got rid of the punctuation for both the encrypted letters, and regular letters, I replaced the letters that I solved for with the uppercase true english letter. Then I took the frequencies of both arrays so I could see the most popular words formed on both sides. 
# 
# ### My next decision was to try and find words that had a length greater than 2 (because two letter words started to screw up my algorithm), that only had one lowercase letter (which meant that all of the letters in the word had been solved for, besides that one letter). I took the word that was most frequent with that condition, and then compared it to words that were in the regular English text file that had the same placement of known letters.
# 
# ### For example, if I knew that TxE was the next most commonly used word, I would look in the English file to see where the length of the word was 3, the first letter was T and the third letter was E. That would correspond to THE, so we would then make x to H. 
# 
# ### Once I solved for that letter, I would add it to the dictionary (dict_1) that had all the solved letters, and also append the solved encrypted letter and solved real letter to their solved arrays. The while loop would then refresh the known letters, and start the process over again until all of the letters had been solved for. 
# 
# ### Once all of the letters had been solved for, I took the encrypted file, and swapped out all of the encrypted letters for the new ones, and then output a file called "cipher_output.txt" with the decoded language.

# In[4]:

#Load the files
import numpy as np

encrypted_txt = "encrypted.txt"
plain_txt = "plain.txt"
plain_good = "plain_without_copyright.txt"

#Put each file in its own array
encrypted = open(encrypted_txt, 'rU').readlines()
plain = open(plain_good, 'rU').readlines()



#Get each line into an array called base. 
encrypted_base = []
i = 0
for x in range(len(encrypted)):
    k = encrypted[x].split('\n')
    encrypted_base.append("".join(k))
    i = i + 1

#Gets all letters and punctuation in the encrypted message.
#This will be so we can get rid of all puncation and just focus on letters and words
letters_and_chars_enc = []
for x in encrypted_base:
    for y in x.split():
        for z in y:
            if z.lower() not in letters_and_chars_enc:
                letters_and_chars_enc.append(z.lower())
                
                
digits_enc = []
for x in letters_and_chars_enc:
    if x.isdigit() == True:
        digits_enc.append(x)
digits_enc


letters_and_chars_enc.sort()
dict_1 = {}
a = letters_and_chars_enc.index('a')
z = letters_and_chars_enc.index('z')
alphabet = letters_and_chars_enc[a:z+1]
alphabet

for x in alphabet:
    dict_1[x] = np.nan
    
# All words in the encrypted message transformed to lowercase
encrypted_base_2 = []
for x in range(len(encrypted_base)):
    for y in encrypted_base[x].split():
        if y.isdigit() == False: #This will get rid of all page numbers
            encrypted_base_2.append(y.lower())
            
#Get each line into an array called base. 
plain_base = []
i = 0
for x in range(len(plain)):
    k = plain[x].split('\n')
    plain_base.append("".join(k))
    i = i + 1
plain_base


plain_base_2 = []
for x in range(len(plain_base)):
    for y in plain_base[x].split():
        if y.isdigit() == False: #This will get rid of all page numbers
            plain_base_2.append(y.upper())
            
#Gets all letters and punctuation in the encrypted message.
#This will be so we can get rid of all puncation and just focus on letters and words
letters_and_chars_plain = []
for x in plain_base:
    for y in x.split():
        for z in y:
            if z.upper() not in letters_and_chars_plain:
                letters_and_chars_plain.append(z.upper())


#Find the index for A and Z, and everything between will be the alphabet locations
letters_and_chars_plain.sort()
a = letters_and_chars_plain.index('A')
z = letters_and_chars_plain.index('Z')
alphabet_plain = letters_and_chars_plain[a:z+1]


punctuation = ['.',',','!','?',':', ';']
solved_letters_encrypted = []
solved_letters_english = []


#First look at single letter words that end in some type of punctuation in the encrypted message
possible_one_word_vowels_encrypted = {}
for x in encrypted_base_2:
    if len(x) == 2 and x[-1] in ['.','!','?'] and x[0] not in digits_enc:
        if x[0] not in possible_one_word_vowels_encrypted:
            possible_one_word_vowels_encrypted[x[0]] = 1
        else:
            possible_one_word_vowels_encrypted[x[0]] +=1  

#Looking for 2 letter "words" that end in sentence ending punctuation and not numbers that could be I.
possible_one_word_vowels_english = {}
for x in plain_base_2:
    if len(x) == 2 and x[-1] in ['.','!','?'] and x[0] not in digits_enc:
        if x[0] not in possible_one_word_vowels_english:
            possible_one_word_vowels_english[x[0]] = 1
        else:
            possible_one_word_vowels_english[x[0]] +=1 
            

most_popular_single_letter_english = max(possible_one_word_vowels_english, key=possible_one_word_vowels_english.get)

most_popular_single_letter_encrypted = max(possible_one_word_vowels_encrypted, key = possible_one_word_vowels_encrypted.get)

# So now, most_popular_single_letter_encrypted in dict_1 will be come most_popular_single_letter_english
# Also add it to the solved letters list
solved_letters_encrypted.append(most_popular_single_letter_encrypted)
solved_letters_english.append(most_popular_single_letter_english)
dict_1[most_popular_single_letter_encrypted] = most_popular_single_letter_english
dict_1

#Look for letters that started a word, and were followed by an apostrophie. Usually I or O, but we already solved for I
possible_letter_before_apost_encrypted = {}
for x in encrypted_base_2:
    if len(x) > 1 and x[1] == "'" and x[0] in alphabet and x[0] not in solved_letters_encrypted:
        if x[0] not in possible_letter_before_apost_encrypted:
            possible_letter_before_apost_encrypted[x[0]] = 1
        else:
            possible_letter_before_apost_encrypted[x[0]] +=1 

max_letter_before_apost_enc = max(possible_letter_before_apost_encrypted, key=possible_letter_before_apost_encrypted.get)

possible_letter_before_apost_english = {}
for x in plain_base_2:
    if len(x) > 1 and x[1] == "'" and x[0] in alphabet_plain and x[0] not in solved_letters_english:
        if x[0] not in possible_letter_before_apost_english:
            possible_letter_before_apost_english[x[0]] = 1
        else:
            possible_letter_before_apost_english[x[0]] +=1 
possible_letter_before_apost_english


max_letter_before_apost_english = max(possible_letter_before_apost_english, key=possible_letter_before_apost_english.get)


# Looks like the english letter that is most common before an apostrophie is q for encrypted, and O in english
dict_1[max_letter_before_apost_enc] = max_letter_before_apost_english
solved_letters_encrypted.append(max_letter_before_apost_enc)
solved_letters_english.append(max_letter_before_apost_english)

# Now looking for the next easiest one letter word, which would be A
possible_single_letter_words_enc = {}
for x in encrypted_base_2:
    if len(x) == 1 and x[0] in alphabet and x[0] not in solved_letters_encrypted:
        if x[0] not in possible_single_letter_words_enc:
            possible_single_letter_words_enc[x[0]] = 1
        else:
            possible_single_letter_words_enc[x[0]] +=1 
possible_single_letter_words_enc


max_single_letter_word_enc = max(possible_single_letter_words_enc, key=possible_single_letter_words_enc.get)


possible_single_letter_words_english = {}
for x in plain_base_2:
    if len(x) == 1 and x[0] in alphabet_plain and x[0] not in solved_letters_english:
        if x[0] not in possible_single_letter_words_english:
            possible_single_letter_words_english[x[0]] = 1
        else:
            possible_single_letter_words_english[x[0]] +=1 
possible_single_letter_words_english

max_single_letter_word_english = max(possible_single_letter_words_english, key=possible_single_letter_words_english.get)

#Appending all of the letters that we have solved for
dict_1[max_single_letter_word_enc] = max_single_letter_word_english
solved_letters_encrypted.append(max_single_letter_word_enc)
solved_letters_english.append(max_single_letter_word_english)

# Making testing data of the plain english texts just in case of future screw ups
plain_test = plain_base_2

# Making testing data of the encrytped text just in case of future screw ups
encrypted_test = encrypted_base_2

# Looking for weird characters that are not in puctuation or the alphabet to look out for
encrypted_other_chars = []
for x in letters_and_chars_enc:
    if x not in punctuation:
        if x not in alphabet and x not in "'" and x not in "-":
            encrypted_other_chars.append(x)

            
#Getting rid of weird characters that we dont care about at the beginning or end of words.
i = 0

for word in encrypted_test:
    if len(word) > 1 and (word[-1] in punctuation or word[-1] in encrypted_other_chars):
        new_word = "" + word[:-1]
        encrypted_test[i] = new_word

    if len(word) > 1 and (word[0] in punctuation or word[0] in encrypted_other_chars):
        new_word = "" + word[1:]
        encrypted_test[i] = new_word    

    i +=1
    

plain_other_chars = []
for x in letters_and_chars_plain:
    if x not in punctuation:
        if x not in alphabet_plain and x not in "'" and x not in "-":
            plain_other_chars.append(x)
plain_other_chars



i = 0
for word in plain_test:
    if len(word) > 1 and (word[-1] in punctuation or word[-1] in plain_other_chars):
        new_word = "" + word[:-1]
        plain_test[i] = new_word
    
    if len(word) > 1 and (word[0] in punctuation or word[0] in plain_other_chars):
        new_word = "" + word[1:]
        plain_test[i] = new_word    
    
    i +=1
    

#Creating the most popualar words that were in the plain english language
plain_test_popular = {}
for x in plain_test:
    if x not in plain_test_popular:
        plain_test_popular[x] = 1
    else:
        plain_test_popular[x] += 1
    i += 1


# In[5]:

# The while will keep going until all of the letters have been solved for
while len(solved_letters_encrypted) < 26:
    
    #This refreshes the encrytped words for letters that we have already solved for
    encrypted_test_deciphered = []
    for x in encrypted_test:
        word = []
        for y in x:
            if y in alphabet:
                if dict_1[y] is not np.nan:
                    word.append(dict_1[y])
                else:
                    word.append(y)
            else:
                word.append(y)
        word = "".join(word)
        encrypted_test_deciphered.append(word)
    
    #Refreshes the frequency of each encrypted word with each letter that was solved for
    encrypted_test_popular = {}
    for x in encrypted_test_deciphered:
        if x not in encrypted_test_popular:
            encrypted_test_popular[x] = 1
        else:
            encrypted_test_popular[x] += 1
        i += 1
    
    
    #Looking for words that are longer than 2 letters long and only have 1 unknown letter
    partially_decrypted_words = {}
    for x in encrypted_test_popular:
        if len(x) > 2:
            if sum(1 for c in x if c.islower()) == 1: #This shows all of the letters with one lowercase letter. 
                #print(x, encrypted_test_popular[x])
                partially_decrypted_words[x] = encrypted_test_popular[x]
    
    #The most frequently used word that has only 1 unknown letter in the word
    max_word = max(partially_decrypted_words, key= partially_decrypted_words.get)
    
    i = 0

    word_dict = {}

    #This looks for the letters that are known, and puts their index in a dictionary
    #It also looks for the lowercase letter (unknown) and finds its index
    for y in max_word:
        if y.isupper() == True and y in alphabet_plain:
            word_dict[i] = y
        if y.islower() == True and y in alphabet:
            max_word_encrypted_index = i
            max_word_encrypted_letter = y
        i +=1
        
        
      
    english_comparison_array = []
    english_comparison = {}
    exclude_list = []

    i = 0

    #Looks for regular english words that are the same length as the encrytped word
    #Then looks to see if the first solved letter is in the same index spot as the English word
    for x in word_dict:
        if len(english_comparison_array) == 0:
            for y in plain_test_popular:
                if len(y) == len(max_word) and y[x] == word_dict[x]:
                    english_comparison_array.append(y)

        else : #If it wasn't matched, it was added to the exclude array
            for y in english_comparison_array:
                if y[x] is not word_dict[x]:
                    exclude_list.append(y)

    #Looks at all words that met the criteria, and excludes all words that did not to get list of possible matches
    #Then takes the english word that was most frequently used
    for word in english_comparison_array:
        if word not in exclude_list and word[max_word_encrypted_index] not in solved_letters_english:
            english_comparison[word] =  plain_test_popular[word]

    #Looks at the best choice of the word, and finds the letter that we are solving for, and its true encrypted value
    i = 0
    for y in max_word:
        if y.isupper() == True and y in alphabet_plain:
            max_word_index = i
            max_word_letter = y
        if y.islower() == True and y in alphabet:
            max_word_encrypted_index = i
            max_word_encrypted_letter = y
        i +=1  
        
    #If all of the above has been solved for, we add them to the dictionary of solved indexes, and then start over  
    if len(english_comparison) > 0:
        english_max_comparison = max(english_comparison, key = english_comparison.get)

        #Place in the new decrypted letter into dict_1
        dict_1[max_word_encrypted_letter] = english_max_comparison[max_word_encrypted_index]
        solved_letters_encrypted.append(max_word_encrypted_letter)
        solved_letters_english.append(english_max_comparison[max_word_encrypted_index])
        dict_1
    #If no possible matches were found, we get rid of that popular encrypted word, and try again
    else:
        plain_test_popular.pop(english_max_comparison)


# In[6]:

encrypted_lower = [words.lower() for words in encrypted_base]

#Decipher the whole code and make it to the way it should look in normal english
cipher_text = []
for x in encrypted_lower:
    words = []
    for y in x:
        if y in dict_1:
            words.append(dict_1[y])
        else:
            words.append(y)
    cipher_text.append("".join(words))

#Write it to a file called cipher_output 
f = open("cipher_output", "w")
f.write(" ".join(cipher_text))
f.close()


# In[ ]:



