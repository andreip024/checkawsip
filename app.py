from flask import Flask, render_template, request
import requests
import json
import ipaddress
from ipaddress import IPv4Address, IPv4Network


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def uppercase():
    iphtml = request.form['ipform']
    try:
        if ipaddress.ip_address(iphtml):
            url = "https://ip-ranges.amazonaws.com/ip-ranges.json"
            r = requests.get(url)
            message_response = "empty"
            data = r.json()
            for cls in data['prefixes']:
                if IPv4Address(iphtml) in IPv4Network(cls["ip_prefix"]):
                    message_response="This IP is part of AWS infrastructure"
        if message_response == "empty":
                message_response="This IP is NOT part of AWS infrastructure"
        return render_template('index.html', script_response=message_response)
    except ValueError:
        message_response="Please insert a valid IP address."
    return render_template('index.html', script_response=message_response)

if __name__ == '__main__':
    app.run(debug=True)