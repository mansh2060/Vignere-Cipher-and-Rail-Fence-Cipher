from flask import Flask, render_template, request
from railfencecipher import rail_fence_cipher
from vignerecipher import get_vignere_cipher 

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    encrypted_text = None
    error = None
    plaintext=""
    if request.method == "POST":
        plaintext = request.form.get("plaintext").lower()
        cipher_type = request.form.get("cipher_type")

        if not plaintext:
            error = "Plaintext field is required."
        else:
            if cipher_type == "vigenere":
                key = request.form.get("key").lower()
                if not key:
                    error = "Key is required for Vigenère Cipher."
                else:
                    try:
                        encrypted_text = get_vignere_cipher(plaintext, key)
                    except KeyError:
                        error = "Invalid characters in input. Use only lowercase alphabets."
            elif cipher_type == "rail_fence":
                encrypted_text = rail_fence_cipher(plaintext)

    return render_template("index.html", result=encrypted_text, error=error, plaintext=plaintext)

if __name__ == "__main__":
    app.run(debug=True)
