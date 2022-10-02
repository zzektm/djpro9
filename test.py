import googletrans
from googletrans import Translator

# print(googletrans.LANGUAGES)

text1 = "안녕하세요"


# nd = googletrans.LANGUAGES
translator = Translator()

print(translator.detect(text1))

# for i in nd:
trans1 = translator.translate(text1, src=translator.detect(text1).lang, dest='en')
print(trans1.text)

#     print(f"{nd[i]}의 인사말: ", trans1.text)