"""
import os
from flask import Flask, request, session, render_template, redirect, url_for
import requests
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

push_time = []

@app.route('/')
def index():
    url = "https://notify-api.line.me/api/notify"
    access_token = os.environ["LINE_TOKEN"]
    headers = {"Authorization": "Bearer " + access_token}
    message = "Hello,World!!"
    payload = {"message": message}
    r = requests.post(url,headers=headers,params=payload,)
    return render_template('home.html')

@app.route('/post', methods=["POST"])
def data_post():
    data = request.get_json()
    print(data)
    todo = data['todo']
    datetime = data['datetime']
    push_time.push(datetime)

    return datetime,todo

def push_todo():
    now = datetime.datetime.now()

app.run(port=8000, debug=True)
"""