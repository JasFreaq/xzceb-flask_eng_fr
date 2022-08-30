'''
Translator file to manage translation between English to French
and vice versa using IBM Watson Language Translator.
'''

import json
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator(f"{apikey}")
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url(f"{url}")

def english_to_french(english_text):
    '''Translates English string to French.'''

    if english_text != "":
        result = language_translator.translate(english_text, model_id='en-fr').get_result()
        french_text = result["translations"][0]["translation"]
        return french_text

    return ""

def french_to_english(french_text):
    '''Translates French string to English.'''

    if french_text != "":
        result = language_translator.translate(french_text, model_id='fr-en').get_result()
        english_text = result["translations"][0]["translation"]
        return english_text

    return ""
