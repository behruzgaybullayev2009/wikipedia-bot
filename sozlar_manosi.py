import wikipedia

def wikipedia_soz(soz):
    wikipedia.set_lang("uz")
    try:
      result = wikipedia.summary(soz)
    except:
      result = "Topilmadi😔"
    return result

