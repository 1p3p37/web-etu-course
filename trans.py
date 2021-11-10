"""translations = translator.translate(['see if this helps', 'tarun'], dest='hi')  # translate two phrases to Hindi
  for translation in translations:  # print every translation
      print(translation.text)"""

#from google.cloud import translate
"""def trans11(meme):
    translator = translate(to_lang="en")  # initalize the Translator object
    translation = translator.translate(meme)
    return translation
meme1 = "— Writing a coursework is more painful than having a baby. \n" \
        "— <Have you ever had a baby?>\n" \
            "— No, but women sometimes say <Let's have another one>, but no student will say\n" \
        "<I'll write another coursework>!"
meme2 = "car\n" \
        "shitting on floor\n" \
        "i'm so angry!"
translator = translate(to_lang="ru")  # initalize the Translator object
translation = translator.translate(meme2)
print(translation)""""""
meme2 = "car\n" \
        "shitting on floor\n" \
        "i'm so angry!"
meme3 = "car"
def translate_text(text=meme3, project_id="YOUR_PROJECT_ID"):"""
    #Translating Text.
"""
    client = translate.TranslationServiceClient()

    location = "global"

    parent = f"projects/{project_id}/locations/{location}"

    # Detail on supported types can be found here:
    # https://cloud.google.com/translate/docs/supported-formats
    response = client.translate_text(
        request={
            "parent": parent,
            "contents": [text],
            "mime_type": "text/plain",  # mime types: text/plain, text/html
            "source_language_code": "en-US",
            "target_language_code": "ru",
        }
    )

    # Display the translation for each input text provided
    for translation in response.translations:
        print("Translated text: {}".format(translation.translated_text))"""