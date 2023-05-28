import awsgi
import os
from flask import Flask, request, render_template
import validate_hcaptcha

HCAPTCHA_SITE_KEY = os.environ['HCAPTCHA_SITE_KEY']
HCAPTCHA_SECRET = os.environ['HCAPTCHA_SECRET']

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html', HCAPTCHA_SITE_KEY=HCAPTCHA_SITE_KEY)


@app.route('/', methods=['POST'])
def index_post():
    return validate_hcaptcha.run(request.form, secret=HCAPTCHA_SECRET)


def lambda_handler(event, context):
    return awsgi.response(app, event, context)


if __name__ == '__main__':
    app.run(debug=True)