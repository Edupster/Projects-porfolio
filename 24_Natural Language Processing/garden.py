# === Your task ==============================================================
# Let's have some 'fun'.
# Go to http://en.wikipedia.org/wiki/Garden_path_sentence and have a brief read 
# at what a 'Garden Path sentence' is (at the top) and look at the 'Examples'

# Create the file garden.py for this task.
# 1. Use some Garden Path sentences or think up your own (at least 5).
# 2. Tokenise and perform Entity recognition for each of the sentences 
#    after you have stored them in a list called gardenpathSentences.
# 3. See how spaCy has categorised these sentences and look up the entities you
#    don't understand
# 4. At the bottom of your file, write a comment about two unusual entities 
# you found that spaCy gave one of the words of your sentences - did you expect this?

import spacy
nlp = spacy.load('en_core_web_sm')

gardenpathSentences = [
    """The old man the boat.""",

    """The complex houses married and single soldiers and their families.""",

    """The horse raced past the barn fell.""",
    
    """ As with other examples, one explanation for the initial misunderstanding
     by the reader is that a sequence of words or phrases tends to be analyzed in terms of a frequent pattern""",
     
    """ In A Dictionary of Modern English Usage (1926), Fowler describes such sentences as unwittingly laying a "false scent"."""
    ]

for sentence in gardenpathSentences:

    nlp_sentence = nlp(sentence)
    print("Tokens:")
    print([token.orth_ for token in nlp_sentence if not token.is_punct | token.is_space])
    print("\n")
    print("Entities:")
    print([(i, i.label_, i.label) for i in nlp_sentence.ents])
    print("\n")
    print("Part Of Speach Tagging:")
    print([(w.text, w.pos_) for w in nlp_sentence])
    print("\n")

#in the sentence: "In A Dictionary of Modern English Usage (1926), Fowler describes such sentences as unwittingly laying a "false scent".
#The entity “English" is not recognised as nationality entity type


# In the sentence: As with other examples, one explanation...., the entity one is detected as cardinal entity when the function on 
# the sentence is to give an example 


