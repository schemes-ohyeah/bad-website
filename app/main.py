from flask import Flask, render_template, jsonify
from Mailgun import Mailgun

app = Flask(__name__)


@app.route("/")
def main():
    return render_template("index.html")


@app.route("/send-mail", methods=["POST"])
def send_mail():
    sender = request.form.get("from")
    receiver = request.form.get("to")
    subject = request.form.get("subject")
    message = request.form.get("message")

    result = Mailgun.send(
        sender, receiver, subject, message
    )

    return jsonify(result)



if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True, port=80)
