import unicodedata
import re
from unicodedata import normalize

def limpiarTexto(texto):
    texto = re.sub(
        r"([^n\u0300-\u036f]|n(?!\u0303(?![\u0300-\u036f])))[\u0300-\u036f]+", r"\1", 
        normalize( "NFD", texto), 0, re.I
    )
    
    cat_filter = ["Cn", "Sc", "Sk", "Sm", "So"]  # categorías a filtrar

    texto = "".join(c for c in texto if unicodedata.category(c) not in cat_filter)
        
    texto = re.sub(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', '', texto)
    texto = re.sub(r"  +", ' ', texto)
    texto = re.sub(r"\n", ' ', texto)
    emoji_pattern = re.compile("["
        u"\U0001F600-\U0001F64F"  # emoticons
        u"\U0001F300-\U0001F5FF"  # symbols & pictographs
        u"\U0001F680-\U0001F6FF"  # transport & map symbols
        u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
        u"\U0001F900-\U0001F9FF"
                           "]+", flags=re.UNICODE)
    
    texto = emoji_pattern.sub(r'', texto)
    texto = re.sub(r'[^\s][...]+', '',texto)
    return texto