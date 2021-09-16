from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    html = "<h1>Hello,devops capstone done by mohamed osama</h1>"
    return html.format(format)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, debug=True)
