"""
Project goal 
Create a dictionary with words and word frequencies that can be passed to the generate_from_frequencies function of the WordCloud class.

Once you have the dictionary, use this code to generate the word cloud image:

123
cloud = wordcloud.WordCloud()
cloud.generate_from_frequencies(frequencies)
cloud.to_file("myfile.jpg")

Things to remember 
Before processing any text, you need to remove all the punctuation marks. To do this, you can go through each line of text, character-by-character, using the isalpha() method. This will check whether or not the character is a letter.

To split a line of text into words, you can use the split() method.

Before storing words in the frequency dictionary, check if they’re part of the "uninteresting" set of words (for example: "a", "the", "to", "if"). Make this set a parameter to your function so that you can change it if necessary.

Input file
For the input file, you need to provide a file that contains text only. For the text itself, you can copy and paste the contents of a website you like. Or you can use a site like Project Gutenberg to find books that are available online. You could see what word clouds you can get from famous books, like a Shakespeare play or a novel by Jane Austen.
"""

# Here are all the installs and imports you will need for your word cloud script and uploader widget

import sys
import io
import fileupload
from IPython.display import display
from matplotlib import pyplot as plt
import numpy as np
import wordcloud

# !pip install wordcloud
# !pip install fileupload
# !pip install ipywidgets
# !jupyter nbextension install - -py - -user fileupload
# !jupyter nbextension enable - -py fileupload

# This is the uploader widget

def _upload():

    _upload_widget = fileupload.FileUploadWidget()

    def _cb(change):
        global file_contents
        decoded = io.StringIO(change['owner'].data.decode('utf-8'))
        filename = change['owner'].filename
        print('Uploaded `{}` ({:.2f} kB)'.format(
            filename, len(decoded.read()) / 2 **10))
        file_contents = decoded.getvalue()

    _upload_widget.observe(_cb, names='data')
    display(_upload_widget)

_upload()

def calculate_frequencies(file_contents):
    # Here is a list of punctuations and uninteresting words you can use to process your text
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    uninteresting_words = ["the", "a", "to", "if", "is", "it", "of", "and", "or", "an", "as", "i", "me", "my", \
    "we", "our", "ours", "you", "your", "yours", "he", "she", "him", "his", "her", "hers", "its", "they", "them", \
    "their", "what", "which", "who", "whom", "this", "that", "am", "are", "was", "were", "be", "been", "being", \
    "have", "has", "had", "do", "does", "did", "but", "at", "by", "with", "from", "here", "when", "where", "how", \
    "all", "any", "both", "each", "few", "more", "some", "such", "no", "nor", "too", "very", "can", "will", "just"]
    
    # LEARNER CODE START HERE
    #dictionary for keeping track of word count
    word_counter={}
    words_in_file=file_contents.split(" ")
    for word in words_in_file:
        #getting a word in list
        for letter in word:
            #getting each letter of word to see if punctuation
            if letter in punctuations:
                #if word is punctuation,removing it
                word=word.replace(letter,"")
    #print(len(words_in_file)) #length before removing uninterested words   
    
    #Removing ininteresting words from list
    for word in words_in_file:
        if word in uninteresting_words:
            words_in_file.remove(word)
     
    #Making a dictionasry of word and it's count
    for word in words_in_file:
        if word not in word_counter.keys():
            word_counter[word]=0
        if word in word_counter.keys():
            word_counter[word]+=1
        
    #print(len(words_in_file)) #counter after removing uninteredted words
    
    #print(word_counter)
    #return words_in_file            
    #wordcloud
    cloud = wordcloud.WordCloud()
    cloud.generate_from_frequencies(word_counter)
    return cloud.to_array()

    # Display your wordcloud image

myimage = calculate_frequencies(file_contents)
plt.imshow(myimage, interpolation = 'nearest')
plt.axis('off')
plt.show()