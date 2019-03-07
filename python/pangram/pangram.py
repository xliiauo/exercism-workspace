def is_pangram(sentence):
  if len(sentence) == 0:
    return False

  s = set()
  for i in sentence:
    if i.isalpha():
      s.add(i.lower())

  return len(s) == 26
