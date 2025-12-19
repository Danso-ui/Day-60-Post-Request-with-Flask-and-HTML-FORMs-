from flask import Flask, render_template, request
from work import data
from datetime import datetime
import smtplib

app = Flask(__name__)


@app.route('/')
def home_page():
    return render_template("index.html", data=data, year=datetime.now().year)

@app.route('/about')
def about_page():
    return render_template("about.html", year=datetime.now().year)

@app.route('/contact', methods=["GET", "POST"])
def contact_page():
    if request.method == "POST":
        dat = request.form
        name_entry = request.form.get("username")
        email_entry = request.form.get("email")
        phone_entry = request.form.get('number')
        message_entry = request.form.get('text')
        send_email(name_entry, email_entry, phone_entry, message_entry)
        # to_addrs="owusuaaafriyie276@gmail.com",
        return render_template("contact.html", year=datetime.now().year, msg_sent=True)
    return render_template("contact.html", year=datetime.now().year, msg_sent=False)

@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    for blog_post in data:
        if blog_post["id"] == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post, year=datetime.now().year)


def send_email(name, email, phone, message):
    email_message = f"Subject:New Message\n\nName: {name}\nEmail: {email}\nPhone: {phone}\nMessage:{message}"
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.ehlo()
        connection.login("abeam7117@gmail.com", "sjjwlsdcbtzkhcdy")
        connection.sendmail("abeam7117@gmail.com", "davnyame1233@gmail.com", email_message)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5500)
