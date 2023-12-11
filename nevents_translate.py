#!/usr/bin/env python3
import os
import time
import requests


class NeventsTranslate():

  def _init_(self):
    self.__url = "https://google-translate113.p.rapidapi.com/api/v1/translator/text"
    self.__headers = {
        "content-type": "application/x-www-form-urlencoded",
        "X-RapidAPI-Key": "11afcd18e2msh70d16f51cfb8189p1e4487jsnb40b06717259",
        "X-RapidAPI-Host": "google-translate113.p.rapidapi.com",
        "user-agent": "google_translate_app/1.0"
    }
    self.__language = {
        "Afrikaans": "af",
        "Akan": "ak",
        "Albanian": "sq",
        "Amharic": "am",
        "Arabic": "ar",
        "Armenian": "hy",
        "Assamese": "as",
        "Aymara": "ay",
        "Azerbaijani": "az",
        "Bambara": "bm",
        "Bangla": "bn",
        "Basque": "eu",
        "Belarusian": "be",
        "Bhojpuri": "bh",
        "Bosnian": "bs",
        "Bulgarian": "bg",
        "Burmese": "my",
        "Catalan": "ca",
        "Cebuano": "ceb",
        "Central Kurdish": "ku",
        "Chinese (Simplified)": "zh-CN",
        "Chinese (Traditional)": "zh-TW",
        "Corsican": "co",
        "Croatian": "hr",
        "Czech": "cs",
        "Danish": "da",
        "Divehi": "dv",
        "Dogri": "doi",
        "Dutch": "nl",
        "English": "en",
        "Esperanto": "eo",
        "Estonian": "et",
        "Ewe": "ee",
        "Filipino": "tl",
        "Finnish": "fi",
        "French": "fr",
        "Galician": "gl",
        "Ganda": "lg",
        "Georgian": "ka",
        "German": "de",
        "Goan Konkani": "gom",
        "Greek": "el",
        "Guarani": "gn",
        "Gujarati": "gu",
        "Haitian Creole": "ht",
        "Hausa": "ha",
        "Hawaiian": "haw",
        "Hebrew": "he",
        "Hindi": "hi",
        "Hmong": "hmn",
        "Hungarian": "hu",
        "Icelandic": "is",
        "Igbo": "ig",
        "Iloko": "ilo",
        "Indonesian": "id",
        "Irish": "ga",
        "Italian": "it",
        "Japanese": "ja",
        "Javanese": "jv",
        "Kannada": "kn",
        "Kazakh": "kk",
        "Khmer": "km",
        "Kinyarwanda": "rw",
        "Korean": "ko",
        "Krio": "kri",
        "Kurdish": "ku",
        "Kyrgyz": "ky",
        "Lao": "lo",
        "Latin": "la",
        "Latvian": "lv",
        "Lingala": "ln",
        "Lithuanian": "lt",
        "Luxembourgish": "lb",
        "Macedonian": "mk",
        "Maithili": "mai",
        "Malagasy": "mg",
        "Malay": "ms",
        "Malayalam": "ml",
        "Maltese": "mt",
        "Manipuri": "mni",
        "Māori": "mi",
        "Marathi": "mr",
        "Mizo": "lus",
        "Mongolian": "mn",
        "Nepali": "ne",
        "Northern Sotho": "nso",
        "Norwegian": "no",
        "Nyanja": "ny",
        "Odia": "or",
        "Oromo": "om",
        "Pashto": "ps",
        "Persian": "fa",
        "Polish": "pl",
        "Portuguese": "pt",
        "Punjabi": "pa",
        "Quechua": "qu",
        "Romanian": "ro",
        "Russian": "ru",
        "Samoan": "sm",
        "Sanskrit": "sa",
        "Scottish Gaelic": "gd",
        "Serbian": "sr",
        "Shona": "sn",
        "Sindhi": "sd",
        "Sinhala": "si",
        "Slovak": "sk",
        "Slovenian": "sl",
        "Somali": "so",
        "Southern Sotho": "st",
        "Spanish": "es",
        "Sundanese": "su",
        "Swahili": "sw",
        "Swedish": "sv",
        "Tajik": "tg",
        "Tamil": "ta",
        "Tatar": "tt",
        "Telugu": "te",
        "Thai": "th",
        "Tigrinya": "ti",
        "Tsonga": "ts",
        "Turkish": "tr",
        "Turkmen": "tk",
        "Ukrainian": "uk",
        "Urdu": "ur",
        "Uyghur": "ug",
        "Uzbek": "uz",
        "Vietnamese": "vi",
        "Welsh": "cy",
        "Western Frisian": "fy",
        "Xhosa": "xh",
        "Yiddish": "yi",
        "Yoruba": "yo",
        "Zulu": "zu"
    }

  def __main_translate(self, f_language, s_language, t_text):
    payload = {"from": f_language, "to": s_language, "text": t_text}
    try:
      response = requests.post(self.__url,
                               data=payload,
                               headers=self.__headers)
    except requests.exceptions.RequestException as req_error:
      return req_error, 1
    else:
      response = response.json()["trans"]
      return response, 0

  def translate(self,
                from_lang="auto",
                to_lang="auto",
                from_lang_text="I auto detect the text if you don't specify"):
    count = 1
    if (from_lang == "auto"
        and to_lang == "auto") or (from_lang in self.__language
                                   and to_lang in self.__language):
      f_language = from_lang
      s_language = to_lang
      t_text = from_lang_text
      translation, status = self.__main_translate(f_language, s_language, t_text)
      if status == 0:
        print(translation)
        return status
      print(translation)
      return status
    while True:
      if isinstance(from_lang, str):
        if count % 4 == 0:
          print("Here is a list of languages available:")
          time.sleep(5)
          os.system('clear')
          print(list(self.__language.keys()), "\n")
          from_lang = input(
              "Enter The correct spelling of the first language: ")
          count += 1
        elif from_lang.capitalize() == "Chinese":
          ask = int(input("Enter 0 for simplified or 1 for traditional: "))
          f_language = "zh-CN" if ask == 0 else "zh-TW"
          break
        elif from_lang.capitalize() in self.__language:
          f_language = self.__language[from_lang.capitalize()]
          break
        else:
          from_lang = input(
              "Enter The correct spelling of the first language: ")
          count += 1
      else:
        from_lang = input(
            "Enter language must be a text, enter the language first again: ")
        count += 1
    os.system("clear")
    count = 1
    while True:
      if isinstance(to_lang, str):
        if count % 4 == 0:
          print("Here is a list of languages available:")
          time.sleep(5)
          os.system('clear')
          print(list(self.__language.keys()), "\n")
          to_lang = input(
              "Enter The correct spelling of the second language: ")
          count += 1
        elif to_lang.capitalize() == "Chinese":
          ask = int(input("Enter 0 for simplified or 1 for traditional: "))
          s_language = "zh-CN" if ask == 0 else "zh-TW"
          break
        elif to_lang.capitalize() in self.__language:
          s_language = self.__language[to_lang.capitalize()]
          break
        else:
          to_lang = input(
              "Enter The correct spelling of the second language: ")
          count += 1
      else:
        to_lang = input(
            "Enter language must be a text, enter the language second again: ")
        count += 1
    os.system("clear")
    t_text = from_lang_text
    translation, status = self.__main_translate(f_language, s_language, t_text)
    if status == 0:
      print(translation)
      return status
    print(translation)
    return status


if __name__ == "__main__":
  test = NeventsTranslate()
  test.translate(
      from_lang="german",
      to_lang="french",
      from_lang_text="Meine Freunden sind Abiodun, Excel, und Michael")


