from flask import Flask, render_template, request, flash
from forms import ContactForm
from flask_mail import Mail, Message
import os

app = Flask(__name__)
mail = Mail(app)

app.secret_key = 'development key'

app.config["MAIL_SERVER"] = "smtp.gmail.com"
app.config["MAIL_PORT"] = 465
app.config["MAIL_USE_SSL"] = True
app.config["MAIL_USERNAME"] = 'jsalami60@gmail.com'
app.config["MAIL_PASSWORD"] = 'osalami20'

mail.init_app(app)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/areas")
def areas():
    return render_template("areas.html")


@app.route("/faqs")
def faqs():
    return render_template("faqs.html")
    
@app.route("/prices")
def prices():
    return render_template("prices.html")

@app.route("/testimonial")
def testimonial():
    return render_template("testimonial.html")
    
@app.route('/contact', methods=['GET', 'POST'])
def contact():
  form = ContactForm()

  if request.method == 'POST':
    if form.validate() == False:
      flash('All fields are required.')
      return render_template('contact.html', form=form)
    else:
      msg = Message(form.subject.data, sender='contact@example.com', recipients=['your_email@example.com'])
      msg.body = """
      From: %s <%s>
      %s
      """ % (form.name.data, form.email.data, form.message.data)
      mail.send(msg)

      return render_template('contact.html', success=True)

  elif request.method == 'GET':
    return render_template('contact.html', form=form)

if __name__ == '__main__':
    app.debug = True
    port = int(os.getenv('PORT', 8080))
    host = os.getenv('IP', '0.0.0.0')
    app.run(port=port, host=host)    