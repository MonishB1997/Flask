from flask import Flask , request , render_template
from dotenv import load_dotenv
import os
import pymongo

MONGO_URI= os.getenv('MONGO_URI')

client=pymongo.MongoClient(MONGO_URI)

db=client.Monish

collection=db['Assignment']


app=Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    name=request.form.get('Name')
    age=request.form.get('Age')
    if name == '' or age =='':
        return " Name or age is empty fill both and submit"
    else :
      form_data=dict(request.form)
      print(form_data)
      data=collection.insert_one(form_data)
      data={
          'data':data
      }
      return 'data submitted successfully'
@app.route('/view')
def view():
    data=collection.find()
    data=list(data)
    for item in data:
        del item['_id']
    return data
   

if __name__== '__main__':
    app.run(debug=True)