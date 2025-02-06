import numpy as np

class RailFenceCipher:
    def __init__(self, rail_size=3):
        self.rail_size = rail_size  

    def rail_fence_cipher_encrypt(self, plaintext, rail_size):
        ciphermatrix = np.array([[" " for _ in range(len(plaintext))] for _ in range(rail_size)])
        i, j = 0, 0
        direction = 1  
        for char in plaintext:
            ciphermatrix[j][i] = char  
            i += 1  
            j += direction  
            if j == rail_size:
                j = rail_size - 2
                direction = -1
            elif j == -1:
                j = 1
                direction = 1
        ciphertext = "".join("".join(row).replace(" ", "") for row in ciphermatrix)
        return ciphertext

    def rail_fence_cipher_decrypt(self, ciphertext, rail_size):
        plainmatrix = np.array([[" " for _ in range(len(ciphertext))] for _ in range(rail_size)])
        rows, columns = rail_size, len(ciphertext)
        i, j = 0, 0
        direction = 1
        for _ in range(columns):
            plainmatrix[j][i] = "*"  
            i += 1
            j += direction
            if j == rail_size:
                j = rail_size - 2
                direction = -1
            elif j == -1:
                j = 1
                direction = 1
        index = 0
        for row in range(rows):
            for column in range(columns):
                if plainmatrix[row][column] == "*" and index < len(ciphertext):
                    plainmatrix[row][column] = ciphertext[index]
                    index += 1
        i, j = 0, 0
        direction = 1
        plain_text = []
        while i < columns:
            plain_text.append(plainmatrix[j][i])
            i += 1
            j += direction
            if j == rail_size:
                j = rail_size - 2
                direction = -1
            elif j == -1:
                j = 1
                direction = 1
        return "".join(plain_text)
