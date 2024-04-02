from flask import Flask, render_template, request, flash
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired
import secrets

secret_key = secrets.token_hex(16)

app = Flask(__name__)
app.secret_key = secret_key

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[InputRequired()])
    password = PasswordField('Password', validators=[InputRequired()])
    submit = SubmitField('Submit')

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        # Process the form data
        username = form.username.data
        password = form.password.data
        
        # Check if either username or password is missing
        if not username:
            flash('Username is required.', 'error')
        elif not password:
            flash('Password is required.', 'error')
        else:
            # You can add further processing or validation here
            flash('Login successful!', 'success')
            return render_template('success.html', username=username)
    
    return render_template('login.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)
