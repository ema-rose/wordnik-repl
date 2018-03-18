"""This module is going to accept json from wordnik and return a python dictionary"""

import json

raw_data = """[
  {
    "userId": 1166212,
    "username": "edna.adele",
    "numberCommentsOnWord": 12,
    "numberLists": 262,
    "createdAt": "2017-12-29T18:27:50.414+0000",
    "id": 3063031,
    "word": "petrichor"
  }
]"""


acrid_defs = """[
  {
    "textProns": [],
    "sourceDictionary": "ahd-legacy",
    "exampleUses": [],
    "relatedWords": [],
    "labels": [],
    "citations": [],
    "word": "acrid",
    "partOfSpeech": "adjective",
    "attributionText": "from The American Heritage® Dictionary of the English Language, 4th Edition",
    "sequence": "0",
    "text": "Unpleasantly sharp, pungent, or bitter to the taste or smell. See Synonyms at bitter.",
    "score": 0
  },
  {
    "textProns": [],
    "sourceDictionary": "ahd-legacy",
    "exampleUses": [],
    "relatedWords": [],
    "labels": [],
    "citations": [],
    "word": "acrid",
    "partOfSpeech": "adjective",
    "attributionText": "from The American Heritage® Dictionary of the English Language, 4th Edition",
    "sequence": "1",
    "text": "Caustic in language or tone.",
    "score": 0
  }
]"""


words_data = json.loads(raw_data)

acrid_definitions = json.loads(acrid_defs)

def words_only(word_dict):
    """this function will take a list of dictionary words and return a list of words only"""
    words_list = []
    for i in range(len(words_data)):
        words_list.append(words_data[i]['word'])
    return words_list


print(words_only(words_data))

def pick_definition(word):
    """this function will return a dict of a word and the chosen definition if avalible"""
    # get definitions for a word
    definitions = get_definitions(word.lower())
    # if no definitions are given, discard the word -- return an empty dictionary (please pick another)
    if definitions == {}:
        return {}
    # else, return a dictionary with 1 word key, and 1 definition value
    if len(definitions) == 1:
        return { word:  definitions[0]["text"] }   
    if len(definitions) >= 2:
        i = 0
        the_def = ""
        while i < len(definitions):
            if len(definitions[i]["text"]) > len(the_def):
                the_def = definitions[i]["text"]
            i += 1
        # { "word_of_interest": "Definition of that word" }
        return { word: the_def }

def get_definitions(word):
    """this functions will return the definitions from Wordnik"""
    if word == "acrid":
        return acrid_definitions
    else:
        return {}


# print(acrid_definitions)

print(pick_definition("Acrid"))
