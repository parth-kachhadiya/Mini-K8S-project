from flask import Flask, request, render_template
import socket

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    greeting = None
    if request.method == "POST":
        name = request.form.get("name", "").strip()
        greeting = f"Hello, {name}! 👋" if name else "Please enter a name."
    return render_template("index.html", greeting=greeting, host=socket.gethostname())

@app.route("/health")
def health():
    return {"status": "ok"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)