"""Generate Markov text from text files."""

from random import choice


def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    open_file = open(file_path)

    open_file = open_file.read()

    return open_file


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

    split_file = text_string.split()

    for i in range(len(split_file) -1):
        if i == len(split_file) - 2:
            break
        current_key = (split_file[i], split_file[i + 1])
        words = []
        if chains.get(current_key, 0) == 0:
            # print("hello!!!!")
            chains[(split_file[i], split_file[i + 1])] = []
            # print(current_key, chains[(split_file[i], split_file[i + 1])])
        chains[current_key].append(split_file[i + 2])
            # print(chains)
        # else: 
        #     chains[current_key].append(split_file[i + 2])
        # print("Words list: ", words)
        # if i == len(split_file) - 2:
        #     break
        # print(split_file[i], split_file[i + 1])
        # print(split_file[i + 2])
    
    return chains 


def make_text(chains):
    """Return text from chains."""

    words = []

    # your code goes here
    # STARTING THE LINK
    # get a random key
    link = choice(list(chains.keys()))
    for word in link:
        words.append(word)
    # get a random word from value of given key
    link = choice(chains.get(link))
    words.append(link)
    print(words)

    # REPEATING AND ADDING MORE LINKS
    # get second word from key and word from value to use as the new key
    # get random word from new key
    # add to words

    # words.append(link)

    # if link in chains.keys()

    # print(words)
    # return ' '.join(words)


input_path = 'green-eggs.txt'

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

print(random_text)
