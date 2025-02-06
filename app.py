from flask import Flask, render_template, request
from vignerecipher import get_vignere_cipher_encrypt, get_vignere_cipher_decrypt
from railfencecipher import RailFenceCipher

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    encrypted_text = None
    decrypted_text = None
    error = None
    plaintext = ""
    key = ""
    rail_size = ""

    if request.method == "POST":
        cipher_type = request.form.get("cipher_type")
        
        if "encrypt" in request.form:
            plaintext = request.form.get("plaintext", "").upper()
            key = request.form.get("key", "").upper()
            
            if cipher_type == "vigenere":
                if not plaintext or not key:
                    error = "Plaintext and key are required for encryption."
                else:
                    encrypted_text = get_vignere_cipher_encrypt(plaintext, key)
            
            elif cipher_type == "rail_fence":
                rail_size = request.form.get("rail_size", "")
                if not rail_size.isdigit() or int(rail_size) < 2:
                    error = "Rail size must be a number greater than or equal to 2."
                else:
                    rail_fence = RailFenceCipher(int(rail_size))
                    encrypted_text = rail_fence.rail_fence_cipher_encrypt(plaintext, int(rail_size))

        elif "decrypt" in request.form:
            ciphertext = request.form.get("ciphertext", "").upper()
            key = request.form.get("key", "").upper()
            
            if cipher_type == "vigenere":
                if not ciphertext or not key:
                    error = "Ciphertext and key are required for decryption."
                else:
                    decrypted_text = get_vignere_cipher_decrypt(ciphertext, key)
            
            elif cipher_type == "rail_fence":
                rail_size = request.form.get("rail_size", "")
                if not rail_size.isdigit() or int(rail_size) < 2:
                    error = "Rail size must be a number greater than or equal to 2."
                else:
                    rail_fence = RailFenceCipher(int(rail_size))
                    decrypted_text = rail_fence.rail_fence_cipher_decrypt(ciphertext, int(rail_size))
    
    return render_template("index.html", result=encrypted_text, decrypted=decrypted_text, error=error, plaintext=plaintext, key=key, rail_size=rail_size)

if __name__ == "__main__":
    app.run(debug=True)
