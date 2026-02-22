"""
Temel veri temizleme adımları:
    -fazla boşlukların kaldırılması
    -büyük harflerin küçük harflere dönüştürülmesi
    -özel karakterlerin kaldırılması
    -yazım hatalarının düzeltilmesi
    -html etiketlerinin kaldırılması
pip install textblob beautifulsoup4    

"""
# Fazla boşlukların temizlenmesi
raw_text = "Python , Google    NLP     dersi."
print(raw_text.split())
normalized_text_1 = " ".join(raw_text.split())
print(f"Fazla boşluklari temizle : {normalized_text_1}")

# büyük küçük harf dönüşümü
raw_text = "PYTHON, Google NLP"
normalized_text_2 =raw_text.lower()
print(f"Harflari küçültülmüş veri : {normalized_text_2}")

# noktalama işaretlerinden kurtul
import string
raw_text = "AI ,Natural; Discover baby!!"
normalized_text_3 = raw_text.translate(str.maketrans("","",string.punctuation))
print(f"Noktalama işaretleri temizlenmiş veri : {normalized_text_3}")

# özel karakterlerden kurtul ^,%,& gibi
import re # regular expression (düzenli ifadeler)
raw_text = "Natural @ Language % Processing"
normalized_text_4 = re.sub(r"[^A-Za-z0-9\s]","", raw_text)
print(f"Ozel karakterlerden kurtulmus veri : {normalized_text_4}")

# Yazım hatalarından kurtul
from textblob import TextBlob
raw_text = "This is so nice devies"
normalized_text_5 = TextBlob(raw_text).correct() # yazım hatalarını düzelt
print(f"Yazim hatalari düzeltilmis veri : {normalized_text_5}")

# html etiketlerinden kurtul
from bs4 import BeautifulSoup
raw_html = "<div> 2045 Google </div>"
normalized_text_6 = BeautifulSoup(raw_html, "html.parser").get_text()
print(f"Html etiketlerinden kurtulmus veri : {normalized_text_6} ")
