"""
Written by Mariana Zorkina 202102
"""

import os.path

def open_vocab(dictionary='default'):
    """
    Opens the dictionary file and turns it into a tree data structure for fast retrieval.
    Truncates the words longer than given value.
    Solution taken from here:
    https://stackoverflow.com/questions/16547643/convert-a-list-of-delimited-strings-to-a-tree-nested-dict-using-python
    
    Args:
        dictionary: a path to a .txt file with one word per line. 
                    By default set to CDICT (http://download.huzheng.org/zh_TW/)   
    Returns:
        tree: a list of words as a dict structure
    """
    
    #Load the dictionary
    if dictionary == 'default':
        dictionary = os.path.join(os.path.dirname(__file__), 'CDICT(Stardict)_wordlist.txt')
    
    with open(dictionary, 'r', encoding='utf8') as rf:
        vocabulary = [word for word in list(set(rf.read().split("\n")))]

    #Turn the list into a tree structure
    vocabulary_tree = {}

    for item in vocabulary:
        t = vocabulary_tree
        for part in list(item):
            t = t.setdefault(part, {})
    
    return vocabulary_tree

    
def remove_prefix(text, prefix):
    """
    A short algorithm to remove the defined word from the text 
    and move forward with tokenization.
    Args:
        text: text that to tokenize
        prefix: a part of the text (= the word found in dictionary to remove)
    Returns:
        truncated text that doesn't contain the tokenized word in the beginning
    """
    return text[text.startswith(prefix) and len(prefix):]


def pop_token_tree(text, tree, longest_word):
    """
    Checks the vocabulary tree for the longest allowed match.
    When found, returns the match and removes it from the text.
    Args:
        text: text to tokenize
        tree: a list of words as a dict structure prepared by open_vocab() function
        longest_word: max number of characters allowed per word. Recommended 2 or 3. 
    Returns:
        frag: the longest of allowed matches that was found in the dictionary
        text: the tokenized text with the previous match removed
    """

    frag = text[:longest_word]
    count = 0
    
    while count<longest_word:

        try:
            tree = tree[frag[count]]
            
        except:
            if count == 0:
                return frag[0], text[1:]
            else:
                return frag[:count], text[count:]
        
        count +=1
        
    
    return frag, text[longest_word:]


def tokenize(text, tree, longest_word=2):
    """
    Takes a sentence or text and crawls through it trying to find matches in a dictionary.
    Only two functions in this module need to be run: 
    First, the open_vocab(), then this one.
    Args:
        text: text to tokenize
        tree: a dictionary created by open_vocab()
    Returns:
        tokens: a tokenized sentence in a list format.
    
    """
    tokens = []
    while len(text)>0:
        t, text = pop_token_tree(text, tree, longest_word)
        tokens.append(t)
    
    return tokens
