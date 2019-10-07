from flask import Flask,render_template
import requests

"""
pip install flask
pip install requests
"""

URL = "https://geocoder.api.here.com/6.2/geocode.json"
location = input("Enter the location here: ")
app_ID = 'YOUR_APP_ID'
app_CODE = 'YOUR_APP_CODE'
PARAMS = {'app_id':app_ID,'app_code':app_CODE,'searchtext':location} 

# sending get request and saving the response as response object 
r = requests.get(url = URL, params = PARAMS) 
data = r.json()

latitude = data['Response']['View'][0]['Result'][0]['Location']['DisplayPosition']['Latitude']
longitude = data['Response']['View'][0]['Result'][0]['Location']['DisplayPosition']['Longitude']

app = Flask(__name__)

@app.route('/')

def map_func():
	return render_template('map.html',app_ID=app_ID,app_CODE=app_CODE,latitude=latitude,longitude=longitude)

if __name__ == '__main__':
    app.run(debug = False)
