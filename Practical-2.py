#Name : Savi Hemant Solanki
#Roll No: 59
#Assignment : 2-2.py

import gensim
from gensim import corpora, models
from gensim.matutils import np
from gensim.utils import simple_preprocess

text1 = ["""You are probably already know that it is important to have a king-size breakfast every morning. 
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

    
#OUTPUT :-
#{'8-10': 0, 'Breakfast': 1, 'Depriving': 2, 'Forget': 3, 'Imagine': 4, 'Never': 5, 'Nowadays': 6, 'Nutritionists': 7, 'This': 8, 'You': 9, 'Your': 10, 'a': 11, 'about': 12, 'absurd': 13, 'alarmed': 14, 'already': 15, 'and': 16, 'are': 17, 'as': 18, 'because': 19, 'body': 20, 'breakfast': 21, 'breakfast!': 22, 'breakfast.': 23, 'by': 24, 'can': 25, 'celebrities': 26, 'day,': 27, 'do': 28, 'driving': 29, 'eat': 30, 'eaten': 31, 'energy': 32, 'every': 33, 'exactly': 34, 'feels': 35, 'first': 36, 'for': 37, 'from': 38, 'fuel': 39, 'fuel;': 40, 'have': 41, 'haven’t': 42, 'health': 43, 'hours': 44, 'hours?': 45, 'how': 46, 'hungry': 47, 'important': 48, 'important.': 49, 'in': 50, 'is': 51, 'it': 52, 'king-size': 53, 'know': 54, 'lead': 55, 'long': 56, 'lose': 57, 'mandatory': 58, 'many': 59, 'meal': 60, 'miss': 61, 'morning': 62, 'morning.': 63, 'most': 64, 'nutritious': 65, 'of': 66, 'people': 67, 'probably': 68, 'problems': 69, 'run.': 70, 'serious': 71, 'silly': 72, 'skip': 73, 'that': 74, 'the': 75, 'their': #76, 'therefore': 77, 'therefore,': 78, 'this': 79, 'to': 80, 'trend,': 81, 'two': 82, 'up.': 83, 'waking': 84, 'ways': 85, 'weight.': 86, 'why': 87, 'within': 88, 'without': 89, 'you': 90, 'your': 91}

#Dictionary :
#[['be', 1], ['better', 1], ['but', 1], ['can', 1], ['excellent', 1], ['food', 1], ['is', 1], ['service', 1], ['the', 2]]
#[['food', 1], ['is', 1], ['service', 1], ['the', 2], ['always', 1], ['and', 1], ['delicious', 1], ['loved', 1]]
#[['food', 1], ['service', 1], ['the', 2], ['and', 1], ['mediocre', 1], ['terrible', 1], ['was', 2]]


#TF-IDF Vector:
#[['be', 0.43], ['better', 0.43], ['but', 0.43], ['can', 0.43], ['excellent', 0.43], ['food', 0.09], ['is', 0.21], ['service', 0.09], ['the', 0.18]]       
#[['food', 0.11], ['is', 0.26], ['service', 0.11], ['the', 0.21], ['always', 0.52], ['and', 0.26], ['delicious', 0.52], ['loved', 0.52]]
#[['food', 0.08], ['service', 0.08], ['the', 0.16], ['and', 0.2], ['mediocre', 0.39], ['terrible', 0.39], ['was', 0.78]]