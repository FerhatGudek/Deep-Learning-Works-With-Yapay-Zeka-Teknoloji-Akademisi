"""
Doğal dil işlemenin ön adımlarından olan tokenizasyon uygulamaları yapacağız
tokenizasyon aslında parçalama işlemidir diyebiliriz belli başlı parçalara ayırma işlemidir.

- kelime tokenizasyonu
- cümle tokenizasyonu
pip install nltk

"""
import nltk # natural language tool kit
nltk.download("punkt_tab") # kelime ve cümle tokenizasyonu için gerekli veri
# örnek text tanımlayalım gardass
raw_text = "Merhaba Google! Bu bir NLP eğitimidir. NLP den sonra firaririyiz arkadaslar."
# kelime tokenizasyonu yapıyoruz arkadaşlar
word_tokens = nltk.word_tokenize(raw_text)
print(f"Kelime tokenizasyonu aha da bu gardas : {word_tokens}")
#cümle tokenizasyonu yapıyoruz gavdaslav sentence de denir
sentence_tokens = nltk.sent_tokenize(raw_text)
print(f"Cümle tokenizasyonu da aha bu gardas : {sentence_tokens}")

