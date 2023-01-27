import translator
text = translator.english_to_french("This is a sentence")["translations"][0]["translation"]

OriginalText = translator.french_to_english(text)["translations"][0]["translation"]
print(OriginalText, "->" ,text)

print(translator.english_to_french("Hello")["translations"][0]["translation"])
print(translator.french_to_english("Bonjour")["translations"][0]["translation"])

translator.english_to_french(None)
translator.french_to_english(None)
