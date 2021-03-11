


###Tokenization du vocabulaire :

vocabulary = open("dictionnaire.txt","r",encoding="utf-8").read()


### on va creer une liste de mots:
tokenization_vocabulary = vocabulary.split(" ")


###tokenize
f = open("text.txt","r",encoding="utf-8")
text_string = f.read()


def tokenize(string,special_character,replacement_string):
  cleaned_text = text_string

  for string in special_character:
    cleaned_text = cleaned_text.replace(string,replacement_string)
  cleaned_text = cleaned_text.lower()
  text_tokens = cleaned_text.split(" ")
  return(text_tokens) 

clean_characters = [".",",","'","\n"]
replacement =""
tokenize_text= tokenize(text_string,clean_characters,replacement)

print(tokenize_text[0:10])

###Trouver les mot mal orthographier.

misspelled_words = []

for words in tokenize_text:
  if words not in tokenization_vocabulary:
    misspelled_words.append(words)

print(misspelled_words)