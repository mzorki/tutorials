"""
Written by Mariana Zorkina 202011
"""
import re
import os.path

def open_vocab(vocabulary_file='default', longest_word=3):
    """
    Opens the vocabulary file and turns it into a list. Truncates the words longer than given value.
    
    Args:
        vocabulary_file: file with the vocabulary. Requires a .txt file with one word per line.
                            By default uses CDICT vocabulary. Else: give path to the file.
        longest_word: max length of a word to be saved. By default takes words of max length 3.
        
    Returns:
        vocab: words of the vocabulary in list format.
    """
    
    if vocabulary_file == 'default':
        vocabulary_file = os.path.join(os.path.dirname(__file__), '../CDICT(Stardict)_wordlist.txt')
        #vocabulary_file = 'CDICT(Stardict)_wordlist.txt'
    
    with open(vocabulary_file, 'r', encoding='utf8') as rf:
        vocab = list(set(rf.read().split("\n")))
        vocab = [v for v in vocab if len(v)<=longest_word and v != ""]
    
    return vocab




def tokenize(sentence, vocab, longest_word=3, verbose=False):
    """
    Takes a sentence and tokenizes it according to the given vocabulary file.
    Follows a simple window slide algorithm by trying to match the whole line 
    and reducing length until successful.
    If using this function, save vocabulary into memory with dict_tokenizer.open_vocab() first.
    
    Args:
        sentence: sentence to tokenize. Expects clean and split phrases (chunks of text between punctuation).
                    Will work if the text is dirty and contains punctuation, 
                    but will take very long with a long text.
        precise: match precision. 
                    False: Default. Will stop at the longest match. 
                    True: will try to split 3+ character words into smaller ones.
        vocab: list with words to use as a vocabulary for tokenizing
        longest_word: max length of a word to be saved. By default takes words of max length 3.
        verbose: set to True if want to get commentaries on 
    
    Returns:
        parsed: list of parsed words
                    
    """
    
    parsed = []
    beg = 0
    len_max = len(sentence)
    left = len_max
    shorten = 0


    while left>0:
        
        
        #Reduce the forward lookup to the longest word allowed to minimize search operations
        
        if verbose: print("Beginning of cycle, left: ", left)
            
        if left-shorten > longest_word:
            shorten = left - longest_word
            if verbose: print(f"New shorten: {shorten} = {left} - {longest_word}")

        #If the text chunk of the current length in vocabulary, remember it and move to new search position.     
        if sentence[beg:len_max-shorten] in vocab:
            
            parsed.append(sentence[beg:len_max-shorten])
            left -= len(sentence[beg:len_max-shorten])
            
            if verbose:
                print(f'Found: {sentence[beg:len_max-shorten]}\nLeft characters: {left}\n======================\n')
            
            beg +=len(sentence[beg:len_max-shorten])
            shorten = 0
            
        
        #If search is reduced to one character and it is still not found, add the current char and go on
        elif len(sentence[beg:len_max-shorten]) == 1 and sentence[beg:len_max-shorten] not in vocab:
            parsed.append(sentence[beg:len_max-shorten])
            
            if verbose: print(f'Not found and added: {sentence[beg:len_max-shorten]}')
            
            left -= 1
            beg +=len(sentence[beg:len_max-shorten])
            shorten = 0
            
            
            
        #If nothing is found in the vocabulary, reduce the length of the search term
        else:
            if verbose: print(f'Not found: {sentence[beg:len_max-shorten]}')
                
            shorten+=1
            

    parsed = [i for i in parsed if i != ' ']

    return parsed




# def tokenize_text(text, vocab, keep_punctuation=False, longest_word=2):
#     """
#     Takes a large multi-sentence text as a string, splits it into phrases by punctuation and tokenizes
#     it according to the given vocabulary file. Follows a simple window slide algorithm by trying to match 
#     the whole line and reducing length until successful. 
#     Will treat newlines as punctuation.
    
#     Args:
#         text: text to tokenize. Requires a re
#         vocab: list with words to use as a vocabulary for tokenizing
#         longest_word: max length of a word to be saved. By default takes words of max length 3. 
#                         In principle, for finer tokenization choose len=2; 
#                         otherwise many words with len=3 appear that can be interpreted as compounds.
#         keep_punctuation: 
#                             True: keep the punctuation, 
#                             False: delete all punctuation
    
#     Returns:
#         parsed: list with each sentence as a parsed list.
                    
#     """
    
    
    
#     #Parse the text into phrases/sentences
#     if keep_punctuation == True:
#         punctuation = re.compile("([。？！；：；、，「」『』《》 *  ()○\n\t])")#inspired by Paul Vierthaler's RegEx
#         sentences = [i for i in re.split(punctuation, text) if i != '' and i != " "] 
        
#     if keep_punctuation == False:
#         punctuation = re.compile("[。？！；：；、，「」『』《》 *  ()○\n\t]")
#         sentences = [i for i in re.split(punctuation, text) if i != '' and i != " "] 

    
#     #Tokenize each phrase
#     parsed = []
 
#     for sentence in sentences:
#         if re.match(punctuation, sentence):
#             parsed[-1].append(sentence)      
#         else:
#             parsed.append(tokenize(sentence, vocab=vocab, longest_word=longest_word))
    
#     return parsed

def tokenize_text(text, vocab, keep_punctuation=False, longest_word=2):
    """
    Takes a large multi-sentence text as a string, splits it into phrases by punctuation and tokenizes
    it according to the given vocabulary file. Follows a simple window slide algorithm by trying to match 
    the whole line and reducing length until successful. 
    Will treat newlines as punctuation.
    
    Args:
        text: text to tokenize. Requires a re
        vocab: list with words to use as a vocabulary for tokenizing
        longest_word: max length of a word to be saved. By default takes words of max length 3. 
                        In principle, for finer tokenization choose len=2; 
                        otherwise many words with len=3 appear that can be interpreted as compounds.
        keep_punctuation: 
                            True: keep the punctuation, 
                            False: delete all punctuation
    
    Returns:
        parsed: list with each sentence as a parsed list.
                    
    """
    
    vocabulary = open_vocab(vocab)
    
    #Parse the text into phrases/sentences
    if keep_punctuation == True:
        punctuation = re.compile("([。？！；：；、，「」『』《》 *  ()○\n\t])")#inspired by Paul Vierthaler's RegEx
        sentences = [i for i in re.split(punctuation, text) if i != '' and i != " "] 
        
    if keep_punctuation == False:
        punctuation = re.compile("[。？！；：；、，「」『』《》 *  ()○\n\t]")
        sentences = [i for i in re.split(punctuation, text) if i != '' and i != " "] 

    
    #Tokenize each phrase
    parsed = []
 
    for sentence in sentences:
        if re.match(punctuation, sentence):
            parsed[-1].append(sentence)      
        else:
            parsed.append(tokenize(sentence, vocab=vocabulary, longest_word=longest_word))
    
    return parsed