def rail_fence_cipher(plaintext, rail_size=4):  
    ciphermatrix = [[" " for _ in range(len(plaintext))] for _ in range(rail_size)]
    
    i = 0
    j = 0
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

    ciphertext = "".join("".join(row).strip() for row in ciphermatrix)
    return ciphertext
