'''Language Translator, French&English'''
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator(apikey=apikey)

translator = LanguageTranslatorV3(
    version="2018-05-01",
    authenticator=authenticator
)

translator.set_service_url(url)

def english_to_french(english_text):
    if english_text:
        french_text = translator.translate(
            text=english_text,
            model_id="en-fr"
            ).get_result()["translations"][0]["translation"]
        return french_text
    else:
        return "English text required"

def french_to_english(french_text):
    if french_text:
        english_text = translator.translate(
            text=french_text
            ,model_id="fr-en"
            ).get_result()["translations"][0]["translation"]
        return english_text
    else:
        return "French text required"
