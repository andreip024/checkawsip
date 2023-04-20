from flask import Flask, render_template, request
import requests
import json
import ipaddress
from ipaddress import IPv4Address, IPv4Network
import logging
from werkzeug.exceptions import BadRequest
import datetime

app = Flask(__name__)

logging.basicConfig(filename='/var/log/flask.log', level=logging.DEBUG, format=f'%(asctime)s %(levelname)s %('f'name)s %(threadName)s : %(message)s')

SITE_KEY = "your_rechapcha_key"
SECRET_KEY = "your_rechapcha_secret_key"
VERIFY_URL = "https://www.google.com/recaptcha/api/siteverify"
ANALYTICS_ID = "your_analytics_id"
AWS_URL = "https://ip-ranges.amazonaws.com/ip-ranges.json"

def aws_call(aws_url):
    
    r = requests.get(aws_url)
    global data
    data = r.json()

def rechapcha():
    secret_response = request.form['g-recaptcha-response']
    verify_response = requests.post(url=f'{VERIFY_URL}?secret={SECRET_KEY}&response={secret_response}').json()
    if verify_response["success"] == False:
        app.logger.warning('BOT detected by rechapcha')
        raise BadRequest("Chapcha error!")

aws_call(AWS_URL)

LAST_UPDATE = datetime.datetime.strptime(data["createDate"], '%Y-%m-%d-%H-%M-%S').strftime('%d-%b-%y %H:%M:%S')

@app.route('/')
def index():
    return render_template('index.html', site_key=SITE_KEY, analytics_id=ANALYTICS_ID, last_update=LAST_UPDATE)

@app.route('/', methods=['POST'])

def main():
    IP_HTML = request.form['ipform']
    try:
        rechapcha()
        MESSAGE_RESPONSE = "empty"
        if ipaddress.ip_address(IP_HTML):
            for cls in data['prefixes']:
                if IPv4Address(IP_HTML) in IPv4Network(cls["ip_prefix"]):
                    MESSAGE_RESPONSE="This IP is part of AWS infrastructure from region " + cls["region"]
                    app.logger.info("IP checked - " + IP_HTML + " - true")
        if MESSAGE_RESPONSE == "empty":
                MESSAGE_RESPONSE="This IP is NOT part of AWS infrastructure"
                app.logger.info("IP checked - " + IP_HTML + " - false")
        return render_template('index.html', message_response=MESSAGE_RESPONSE, site_key=SITE_KEY, analytics_id=ANALYTICS_ID, last_update=LAST_UPDATE)
    except ValueError:
        MESSAGE_RESPONSE="Please insert a valid IP address"
        app.logger.info("IP checked - " + IP_HTML + " - NA")
    return render_template('index.html', message_response=MESSAGE_RESPONSE, site_key=SITE_KEY, analytics_id=ANALYTICS_ID, last_update=LAST_UPDATE)

@app.route('/about/')
def about():
    return render_template('about.html', site_key=SITE_KEY, analytics_id=ANALYTICS_ID, last_update=LAST_UPDATE)

@app.route('/singin/')
def singin():
    return render_template('singin.html', site_key=SITE_KEY, analytics_id=ANALYTICS_ID, last_update=LAST_UPDATE)

if __name__ == '__main__':
    app.run(debug=False)
    