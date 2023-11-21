import spacy
import nltk
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag

raw_text="""The Board of Control for Cricket in India (BCCI) is the governing body for cricket in 
India and is under the jurisdiction of Ministry of Youth Affairs and Sports, Government of India.[2] 
The board was formed in December 1928 as a society, registered under the Tamil Nadu Societies Registration Act. 
It is a consortium of state cricket associations and the state associations select their representatives 
who in turn elect the BCCI Chief. Its headquarters are in Wankhede Stadium, Mumbai. 
Grant Govan was its first president and Anthony De Mello its first secretary. """

NER = spacy.load("en_core_web_sm", disable=["tok2vec", "tagger", "parser", "attribute_ruler", "lemmatizer"])
text= NER(raw_text)
for w in text.ents:
    print(w.text,w.label_)

nltk.download('treebank')
sent = nltk.corpus.treebank.tagged_sents()
print(nltk.ne_chunk(sent[0]))
