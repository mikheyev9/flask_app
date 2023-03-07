"""Run this file to launch website on your PC"""
from app import app, db
from app.models import User, Post

#flask shell
@app.shel_context_processor
def make_shell_context():
    return {'db':db, 'User':User, 'Post':Post}

app.run(debug=True)