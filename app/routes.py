#Variable app import from the application package
from app import app, moc
#function render_template uses to display the html file
from flask import render_template, flash, redirect, url_for
#class LoginForm - form to login in web site
from app.forms import LoginForm


# processing inconing urls
@app.route('/') # https://your_website.com/
@app.route('/index') # https://your_website.com/index
def index():
    user = {'username': 'vasiliy'}
    return render_template('index.html',user=user, posts=moc.posts)

@app.route('/login', methods=['POST','GET'])
def login():
    form = LoginForm()
    # form.validate_on_submit react on 'POST' request
    if form.validate_on_submit():
        flash(f"""login requested for user {form.username.data} ,
              remember_me={form.remember_me.data}""")
        return redirect(url_for('index'))
    return render_template('login.html', title='log in', form=form)
