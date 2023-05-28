import urllib.parse
import urllib.request


def run(request: dict, secret: str):
    token = request['h-captcha-response']
    url = 'https://hcaptcha.com/siteverify'
    data = {
        'secret': secret,
        'response': token
    }
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    encoded_data = urllib.parse.urlencode(data).encode('utf-8')
    req = urllib.request.Request(url, encoded_data, headers)
    with urllib.request.urlopen(req) as res:
        body = res.read()
        return body
