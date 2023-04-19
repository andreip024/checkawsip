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

SITE_KEY = "6LdMQJglAAAAALZosA7_89pMLpHI9K4md8Yy7RCo"
SECRET_KEY = "6LdMQJglAAAAAF5ZuO9jGobazMp2GQhSUUBxPb9N"
VERIFY_URL = "https://www.google.com/recaptcha/api/siteverify"
ANALYTICS_ID = "G-QPW0Q5L2KY"
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
        message_response = "empty"
        if ipaddress.ip_address(IP_HTML):
            for cls in data['prefixes']:
                if IPv4Address(IP_HTML) in IPv4Network(cls["ip_prefix"]):
                    message_response="This IP is part of AWS infrastructure from region " + cls["region"]
                    app.logger.info("IP checked - " + IP_HTML + " - true")
        if message_response == "empty":
                message_response="This IP is NOT part of AWS infrastructure"
                app.logger.info("IP checked - " + IP_HTML + " - false")
        return render_template('index.html', script_response=message_response, site_key=SITE_KEY, analytics_id=ANALYTICS_ID, last_update=LAST_UPDATE)
    except ValueError:
        message_response="Please insert a valid IP address"
        app.logger.info("IP checked - " + IP_HTML + " - NA")
    return render_template('index.html', script_response=message_response, site_key=SITE_KEY, analytics_id=ANALYTICS_ID, last_update=LAST_UPDATE)

if __name__ == '__main__':
    app.run(debug=False)
    