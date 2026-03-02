"""
stop words çıkarma kelimeleri:
    -ingilizce stopwords çıkarma (nltk)
    -türkçe stopwords çıkarma (nltk)
    - manuel olarak stopwords çıkarma
pip install nltk     

"""
import nltk
from nltk.corpus import stopwords
nltk.download("stopwords") # stopwords veri setini indirir
stop_words_eng = set(stopwords.words("english")) # ingilizce stop words listesi

# örnek metin
eng_text = "This is just a simple example to show how stopwords can be removed from sentences"
eng_text_list = eng_text.split()
print(eng_text_list)

filtered_words_eng = [word for word in eng_text_list if word.lower() not in stop_words_eng]
print(f"Orijinal : {eng_text}")
print(f"Filtered : {filtered_words_eng}") # cümlenin stopwordslerden arındırılmış hali

# örnek metin 
stop_words_tr = set(stopwords.words("turkish"))
turkce_text = "Bu bir test metinidir ve bu metnin önemi basit bir olay ile kelime metin düzenleme için"
turkce_text_list = turkce_text.split()

filtered_words_tr = [word for word in turkce_text_list if word.lower() not in stop_words_tr]
print(f"Orijinal : {turkce_text}")
print(f"Filtered : {filtered_words_tr}")

# kütüphane kullanmadan stopword çıkarma işi
custom_tr_stopwords = ["bu","de","ile","ile","ki","da"]
custom_text = "Bu bir denemedir, bunun için amacımız metinde ki bazı kelimeleri çıkartmak."
custom_text_list = custom_text.split()

filtered_words_custom_text =[word for word in custom_text_list if word.lower() not in custom_tr_stopwords]
print(f"Orijinal hali gardass : {custom_text}")
print(f"Bu da filtrelenmiş hali gardass : {filtered_words_custom_text}")

