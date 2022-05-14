"""Generate Markov text from text files."""

import sys
from random import choice


def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    contents = open(file_path).read()

    return contents


def make_chains(text_string):
    """Take input text as string; return dictionary of Markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> chains = make_chains('hi there mary hi there juanita')

    Each bigram (except the last) will be a key in chains:

        >>> sorted(chains.keys())
        [('hi', 'there'), ('mary', 'hi'), ('there', 'mary')]

    Each item in chains is a list of all possible following words:

        >>> chains[('hi', 'there')]
        ['mary', 'juanita']

        >>> chains[('there','juanita')]
        [None]
    """

    chains = {}

    words = text_string.split()

    for i in range(len(words) - 1):
        if (i + 2) < len(words):
            key_pair = (words[i],words[i + 1])
            word_value = words[i + 2]
            if key_pair not in chains:
                chains[key_pair] = [word_value]
            else:
                chains[key_pair].append(word_value)
        else:
            break

    return chains


def make_text(chains):
    """Return text from chains."""

    words = []
    #turns a key from the dicitonary into a list
    keys_list = list(chains.keys())
    #randomly chooses a tuple from the keys_list
    link = choice(keys_list)

    while True:
        if link in chains.keys():
            #randomly chooses a value from the chains dicitonary where the key == link
            dict_word = choice(chains[link])
            random_word_list = []
            #turning the tuples into a list
            link_list = list(link)
            
            #add the randomly chosen keys and associated value to list used to create new key
            random_word_list.append(link_list[0])
            random_word_list.append(link_list[1])
            random_word_list.append(dict_word)
            
            #add the randomly chosen words to the final string
            words.append(link_list[0])
            words.append(link_list[1])
            words.append(dict_word)
            
            #create a new key with the second value of the original key and the random word selected from that key value
            new_key = random_word_list[1], random_word_list[2]
            
            #update the link to the new key
            link = new_key
        else:
            break

    return ' '.join(words)


input_path = sys.argv[1]

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)
# Get a Markov chain
chains = make_chains(input_text)
# Produce random texts
random_text = make_text(chains)
print(random_text)
