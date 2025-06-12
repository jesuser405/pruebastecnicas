#Traslate text from Spanish to English using Google Translate API

from translate import Translator

translator = Translator(from_lang='es', to_lang='en')

txt = input("Introduce lo que quieres tarducir: ")
# Example: txt = "Hola, ¿cómo estás?"

res = translator.translate(txt)

print(f"Traducción: {res}")
