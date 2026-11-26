from flask import Flask

app = Flask(__name__)
VERSION = "1.0.0"

@app.route("/")
def index():
    return f"devops-ci-app version {VERSION}\n"

@app.route("/health")
def health():
    return "ok\n"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
