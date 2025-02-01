from encoderdecoder import VignereCipher
from vocabulary import vocab
def match_length(plain_text,key):
    if len(plain_text) > len(key):
        size=(len(plain_text)//len(key))+1
        matched_key=(key * size)[:len(plain_text)]
        return plain_text,matched_key
    elif len(plain_text) < len(key):
        key=key[:len(plain_text)]
        matched_key=key
        return plain_text,matched_key
    else:
        return plain_text,key
    
def get_vignere_cipher(plain_text,key):
        plain_text,matched_key=match_length(plain_text,key)
        create_vocab=VignereCipher(vocab)
        plain_id,key_id=create_vocab.encoder(plain_text,matched_key)
        text=create_vocab.decoder(plain_id,key_id)
        return text.upper()



    