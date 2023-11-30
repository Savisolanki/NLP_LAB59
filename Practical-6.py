import spacy
nlp = spacy.load("en_core_web_sm")
from spacy import displacy
text = "Hello Im Savi.Im final year Student.I like to explore new places and try new food."
doc = nlp(text)
for token in doc:
    print(
        f"""
TOKEN: {token.text}
=====
{token.tag_ = }
{token.head.text = }
{token.dep_ = }"""
    )

displacy.serve(doc,style="dep")


"""
TOKEN: Hello
=====
token.tag_ = 'UH'        
token.head.text = 'Hello'
token.dep_ = 'ROOT'      

TOKEN: I
=====
token.tag_ = 'PRP'       
token.head.text = 'Hello'
token.dep_ = 'npadvmod'

TOKEN: m
=====
token.tag_ = 'NNP'
token.head.text = 'Hello'
token.dep_ = 'npadvmod'

TOKEN: Savi
=====
token.tag_ = 'NNP'
token.head.text = 'Hello'
token.dep_ = 'npadvmod'

TOKEN: .
=====
token.tag_ = '.'
token.head.text = 'Hello'
token.dep_ = 'punct'

TOKEN: Im
=====
token.tag_ = 'NNP'
token.head.text = 'Student'
token.dep_ = 'nmod'

TOKEN: final
=====
token.tag_ = 'JJ'
token.head.text = 'year'
token.dep_ = 'amod'

TOKEN: year
=====
token.tag_ = 'NN'
token.head.text = 'Student'
token.dep_ = 'compound'

TOKEN: Student
=====
token.tag_ = 'NN'
token.head.text = 'Student'
token.dep_ = 'ROOT'

TOKEN: .
=====
token.tag_ = '.'
token.head.text = 'Student'
token.dep_ = 'punct'

TOKEN: I
=====
token.tag_ = 'PRP'
token.head.text = 'like'
token.dep_ = 'nsubj'

TOKEN: like
=====
token.tag_ = 'VBP'
token.head.text = 'like'
token.dep_ = 'ROOT'

TOKEN: to
=====
token.tag_ = 'TO'
token.head.text = 'explore'
token.dep_ = 'aux'

TOKEN: explore
=====
token.tag_ = 'VB'
token.head.text = 'like'
token.dep_ = 'xcomp'

TOKEN: new
=====
token.tag_ = 'JJ'
token.head.text = 'places'
token.dep_ = 'amod'

TOKEN: places
=====
token.tag_ = 'NNS'
token.head.text = 'explore'
token.dep_ = 'dobj'

TOKEN: and
=====
token.tag_ = 'CC'
token.head.text = 'explore'
token.dep_ = 'cc'

TOKEN: try
=====
token.tag_ = 'VB'
token.head.text = 'explore'
token.dep_ = 'conj'

TOKEN: new
=====
token.tag_ = 'JJ'
token.head.text = 'food'
token.dep_ = 'amod'

TOKEN: food
=====
token.tag_ = 'NN'
token.head.text = 'try'
token.dep_ = 'dobj'

TOKEN: .
=====
token.tag_ = '.'
token.head.text = 'like'
token.dep_ = 'punct'

"""
