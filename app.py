from flask import Flask, render_template, request
import gifapi
import whats2

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/send', methods=["POST"])
def sending():
    number = request.form["number"]
    gif_type = request.form["gif_type"]
    gif_link = gifapi.gif_request(gif_type)
    whats2.whatsapp(number, gif_link)
    return render_template("index.html")



if __name__ == "__main__":
    app.run(debug=True)
