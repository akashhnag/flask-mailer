from flask import Flask,jsonify,request
from flask_mail import Mail,Message

app=Flask(__name__)

app.config['MAIL_SERVER']='email provider'
app.config['MAIL_PORT']=587
app.config['MAIL_USE_TLS'] = True,
app.config['MAIL_USERNAME']="username"
app.config['MAIL_PASSWORD']="password"
app.config['MAIL_DEFAULT_SENDER']="sender email"

mail = Mail(app)

@app.route('/mail')
def send_mail():
    print('sending mail')
    msg = Message("Hello",
                  recipients=["recipient email"])
    mail.send(msg)
    return 'Done'

app.run(port=4000,debug=True)
