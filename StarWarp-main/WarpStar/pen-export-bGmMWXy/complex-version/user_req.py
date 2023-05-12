from flask import g, redirect, url_for
from functools import wraps

def user_required(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if not g.user:
            return redirect(url_for('login'))
        elif 'user' not in g.user.roles:
            return 'You are not authorized to perform this action'
        return func(*args, **kwargs)
    return wrapper
@app.route('/search')
@user_required
def search():
    # search logic here
