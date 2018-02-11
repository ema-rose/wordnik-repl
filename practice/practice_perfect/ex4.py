def censor(text, word):
  phrase = text.split(word)
  return ("*" * len(word)).join(phrase)
