from flask import Flask
from threading import Thread

app = Flask(__name__)
port = 8000

def setport(newport: int):
  global port
  port = newport

@app.route('/')
def home():
    return "<h1>Periodic Sentence Bot</h1><p>This website keeps the bot alive on most free hosting sites, as it will present itself as a webservice needing constant uptime. For even more security, use cron jobs or a similar feature to ping it every few minutes</p>"

def run():
  global port
  print("Running on port ", port)
  app.run(host='0.0.0.0',port=port)

def keep_alive(port: int = 8000):
    setport(port)
    t = Thread(target=run)
    t.start()