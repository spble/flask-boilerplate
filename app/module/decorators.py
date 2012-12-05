from functools import wraps
from flask import g, flash, redirect, url_for, request

def example_wrapper(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        return f(*args, **kwargs)
    return decorated_function
