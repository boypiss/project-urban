from flask import Flask, render_template

app = Flask(__name__)

# Route for the homepage
@app.route("/")
def home():
    return render_template("index.html")

# Route for the "More Information" page
@app.route("/info")
def info():
    return render_template("info.html")

if __name__ == "__main__":
    app.run(debug=True)

@app.route("/text")
def text_page():
    return render_template("text.html")
