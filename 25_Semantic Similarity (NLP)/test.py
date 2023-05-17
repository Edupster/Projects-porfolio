import spacy
nlp = spacy.load('en_core_web_md')

f = open("movies.txt" , "r")
descriptions = []
movie_names = []
for line in f:
    descriptions.append(line[9:].strip("\n"))
    movie_names.append(line[0:9])
f.close


def watch_next(description_input):
    description_input_nlp = nlp(description_input)
    similarity = []

    for description in descriptions:
        similarity.append(nlp(description).similarity(description_input_nlp))
    print (similarity)


description_in = """Will he save their world or destroy it? When the Hulk becomes too dangerous for the 
Earth, the Illuminati trick Hulk into a shuttle and launch him into space to a planet where the Hulk can 
live in peace. Unfortunately, Hulk land on the planet Sakaar where he is sold into slavery and trained as 
a gladiator."""

watch_next(description_in)