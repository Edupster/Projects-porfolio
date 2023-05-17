"""Functions for creating, transforming, and adding prefixes to strings."""


def add_prefix_un(word):
    """Take the given word and add the 'un' prefix.
    :param word: str - containing the root word.
    :return: str - of root word prepended with 'un'.
    """
    word="un"+word
    print(word)
    return word

add_prefix_un ( "happy" )


def make_word_groups(vocab_words):
    """Transform a list containing a prefix and words into a string with the prefix followed by the words with prefix prepended.
    :param vocab_words: list - of vocabulary words with prefix in first index.
    :return: str - of prefix followed by vocabulary words with
            prefix applied.
    This function takes a `vocab_words` list and returns a string
    with the prefix and the words with prefix applied, separated
     by ' :: '.
    For example: list('en', 'close', 'joy', 'lighten'),
    produces the following string: 'en :: enclose :: enjoy :: enlighten'.
    """
    prefix = vocab_words [ 0 ]
    output = prefix + " :: "
    for i in range ( 1, len ( vocab_words )):
        vocab_words [ i ] = prefix + vocab_words [ i ]
        if i != len(vocab_words)-1:
            output = output + vocab_words [ i ] + " :: "
        else:
            output = output + vocab_words [ i ]
    print(output)
    return output

make_word_groups(['pre', 'serve', 'dispose', 'position', 'order'])


def remove_suffix_ness(word):
    """Remove the suffix from the word while keeping spelling in mind.
    :param word: str - of word to remove suffix from.
    :return: str - of word with suffix removed & spelling adjusted.
    For example: "heaviness" becomes "heavy", but "sadness" becomes "sad".
    """

    if word [len(word)-4 : len(word)] == "ness":
        word = word[0 : len(word)-4]
        
    print(word)
    return(word)

remove_suffix_ness("sadness")



def adjective_to_verb(sentence, index):
    """Change the adjective within the sentence to a verb.
    :param sentence: str - that uses the word in sentence.
    :param index: int - index of the word to remove and transform.
    :return: str - word that changes the extracted adjective to a verb.
    For example, ("It got dark as the sun set", 2) becomes "darken".
    """
    sentence_list = sentence.strip(". ! ? ,").split(" ")
    adj_to_verb = sentence_list[index] + "ten"
    print(adj_to_verb)
    return(adj_to_verb)

adjective_to_verb('It got dark as the sun set.', 2)