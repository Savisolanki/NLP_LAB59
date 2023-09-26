import gensim
from gensim import corpora, models
from gensim.matutils import np
from gensim.utils import simple_preprocess

text1 = ["""ou probably already know that it is important to have a king-size breakfast every morning. 
         do you know why Your body is hungry in the morning because you haven’t eaten for about 8-10 hours? Breakfast is therefore the first meal of the day, and therefore, the most important. 
         Imagine driving without fuel; This is exactly how your body feels without fuel from a nutritious breakfast. Nowadays many people skip breakfast to lose weight. 
         Nutritionists are alarmed by this trend, as it is mandatory to eat breakfast within two hours of waking up. Depriving the body of energy can lead to serious health problems in the long run. 
         Forget silly celebrities and their absurd ways to lose weight. 
         Never miss breakfast!"""]

tokens1 = [[item for item in line.split()] for line in text1]
g_dict1 = corpora.Dictionary(tokens1)

print("The dictionary has: " +str(len(g_dict1)) + " tokens\n")
print(g_dict1.token2id)

text = ["The food is excellent but the service can be better",
        "The food is always delicious and loved the service",
        "The food was mediocre and the service was terrible"]

g_dict = corpora.Dictionary([simple_preprocess(line) for line in text])
g_bow = [g_dict.doc2bow(simple_preprocess(line)) for line in text]

print("Dictionary : ")
for item in g_bow:
    print([[g_dict[id], freq] for id, freq in item])

g_tfidf = models.TfidfModel(g_bow, smartirs='ntc')

print("TF-IDF Vector:")
for item in g_tfidf[g_bow]:
    print([[g_dict[id], np.around(freq, decimals=2)] for id, freq in item])