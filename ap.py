from flask import Flask ,render_template ,request

from datetime import date

from dotenv import load_dotenv

import os

import pymongo

MONGO_URI= os.getenv('MONGO_URI')

client= pymongo.MongoClient(MONGO_URI)

db=client.MK

collection=db['new collection']

app=Flask(__name__)

@app.route('/')
def home():
    today = str(date.today())
    

    return render_template('ap.html',today=today)

@app.route('/submit',methods=['POST'])
def submit():
    data=dict(request.form)   #best way to get all data in 1 shot
    collection.insert_one(data)

    return "data submitted"

@app.route('/view')
def view():
    data=collection.find()
    data=list(data)
    for item in data:
        
        del item['_id']
        print(data)
        
    return data



if __name__ == '__main__':
    app.run(debug=True)