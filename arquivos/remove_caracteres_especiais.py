import unicodedata

def remove_caracteres_especiais(palavra):
    return unicodedata.normalize('NFKD', palavra).encode('ASCII', 'ignore').decode('ASCII')