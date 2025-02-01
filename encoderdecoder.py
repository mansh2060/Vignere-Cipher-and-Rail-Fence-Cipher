class VignereCipher:
    def __init__(self,vocab):
        self.chr_to_int={token:idx for token,idx in vocab.items()}
        self.int_to_chr={idx:token for token,idx in vocab.items()}

    def encoder(self,plain_text,key):
        plain_id=[self.chr_to_int[character.lower()] for character in plain_text]
        key_id=[self.chr_to_int[character.lower()] for character in key]
        return plain_id,key_id

    def decoder(self,plain_id,key_id):
        combined_id=[plain_id[i]+key_id[i] for i in range(len(plain_id))]
        combined_id=[idx % 26 for idx in combined_id]
        text=[self.int_to_chr[idx] for idx in combined_id]
        vignerecipher="".join(text)
        return vignerecipher
