"""
Kök ve gövde (lemma) bulma işlemini yapıcaz
    -stemming: porter stemmer
    -lemmatization : word net lemmaziter
pip install nltk      
"""
import nltk 
nltk.download("wordnet") # lemma yani gövde bulmak için gerekli veri tabanı
nltk.download("omw-1.4") # wordnet için gerekli ek dil desteği 

# stemming
from nltk.stem import PorterStemmer # ingilizce için popüler stemming uygulaması
stemmer = PorterStemmer() # porter stemmer nesnesi oluşturuyoruz gavdass
word_stem = ["playing","played","plays","happier","happily","studying","studies"]
stems = [stemmer.stem(w) for w in word_stem]
print(f"Orijinal : {word_stem}")
print(f"Koklerine ayrilmis hali : {stems}")

# lemmatization
from nltk.stem import WordNetLemmatizer
lematizer = WordNetLemmatizer()
lemma = ["running","ran","gone","better","children"]
lemmas = [lematizer.lemmatize(w) for w in lemma]
print(f"orijinal : {lemma}")
print(f"Govdelenmis hali : {lemmas}")
