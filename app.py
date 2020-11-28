from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_openshift ():
    return 'Python no Openshift!'
  
app.run(host='0.0.0.0 ', port =8080)
