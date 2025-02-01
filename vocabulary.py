import string
alphabet_list=[]

for characters in string.ascii_lowercase: 
    alphabet_list.append(characters)

vocab={tokens:idx for idx,tokens in enumerate(alphabet_list)}
