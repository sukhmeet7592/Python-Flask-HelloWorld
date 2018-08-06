from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
  return 'Hey Vinod!This is Python Flask app on Azure!'

if __name__ == '__main__':
  app.run()
