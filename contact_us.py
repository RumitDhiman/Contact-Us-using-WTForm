from flask import Flask, request, redirect, url_for, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, validators, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email
import email_validator

app=Flask(__name__)
app.secret_key='any-string-you-want-just-keep-it-secret'
class contactForm(FlaskForm):
    name=StringField(label='Name', validators=[DataRequired()])
    email=StringField(label='Email',validators=[DataRequired(), Email(granular_message=True)])
    message=StringField(label='Message')
    submit=SubmitField(label='Log In')

@app.route('/',methods=['GET','POST'])
def home():
    a=contactForm()
    if a.validate_on_submit():
        print(f'Name:{a.name.data}, Email:{a.email.data},Message:{a.message.data}')
    else:
        print('Someting want wrong')
    return render_template('contact_us.html',form=a)

if __name__=='__main__':
    app.run(debug=True)
    