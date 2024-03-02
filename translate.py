# All Functionality available at https://pypi.org/project/googletrans/
from googletrans import Translator
translator = Translator()
# You can use another google translate domain for translation. If multiple URLs are provided it then randomly chooses a domain.
# translator = Translator(service_urls=[
#       'translate.google.com',
#       'translate.google.co.kr',
#     ])
#! The maximum character limit on a single text is 15k.
# Default Language
# a = translator.translate('안녕하세요.')
a = translator.translate('안녕하세요.', dest='en')
# Showing  All available Info
print(a) #Translated(src=ko, dest=en, text=hello., pronunciation=None, extra_data="{'translat...")
# Showing Translated  Text Only
print(a.text)

#? Array can be used to translate a batch of strings in a single method call and 
#? a single HTTP session. The exact same method shown above work for arrays as well.
#! The maximum character limit on a single text is 15k.
translations = translator.translate(['The quick brown fox', 'jumps over', 'the lazy dog'], dest='ko')
for translation in translations:
    print(translation.origin, ' -> ', translation.text)
    
    
#todo Language detection
a = translator.detect('이 문장은 한글로 쓰여졌습니다.')
print(a) #Detected(lang=ko, confidence=1)



