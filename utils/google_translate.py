from googletrans import Translator

def translate_srt(srt_data: list) -> list:
    translator = Translator()
    translated = []

    for item in srt_data:
        translated_text = translator.translate(item["text"], src='en', dest='pt').text
        translated.append({
            "index": item["index"],
            "start": item["start"],
            "end": item["end"],
            "text": translated_text
        })

    return translated
