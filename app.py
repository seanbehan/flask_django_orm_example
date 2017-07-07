import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
from data.models import *
from flask import Flask, render_template as template

app = Flask('app')

@app.route("/")
def home():
    user = User(name="someone", email="someone@example.com")
    user.save()

    return template('users.html', users=User.objects.all())

if __name__ == '__main__':
    app.run(debug=True)
