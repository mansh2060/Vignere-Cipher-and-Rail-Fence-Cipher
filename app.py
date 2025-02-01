from flask import Flask, render_template, request
from cipher import get_vignere_cipher 

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        plaintext = request.form.get("plaintext").lower()
        key = request.form.get("key").lower()
        if not plaintext or not key:
            return render_template("index.html", error="Both fields are required.")

        try:
            encrypted_text = get_vignere_cipher(plaintext, key)
            return render_template("index.html", result=encrypted_text, plaintext=plaintext, key=key)
        except KeyError:
            return render_template("index.html", error="Invalid characters in input. Use only lowercase alphabets.")

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)