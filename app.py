from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

#https://testingautomation.onrender.com/

@app.get('/')
def home_page():
    return {"message":"Welcome to Testing Automation site"}

@app.get('/create-user')
def create_user():
    return {"message":"still in progress"}

if __name__=='__main__':
    app.run(host='0.0.0.0',port=5000)