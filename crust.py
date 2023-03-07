from flask import *
from threading import Thread, Event

plan = Flask(__name__)


SPOTS = [
    {
    'id': 1,
    'Name': "Alexander Heritage And Rainforest Resort",
    'Info': "Among the facilities at this property are a 24-hour front desk and room service,along with free WiFi throughout the property.",
    'Rating ': "4.5/5",
    'Cost':'2000 per night',    
    },
    {
    'id': 2,
    'Name': "Dune Barr House - Verandah in the Forest",
    'Info': "Popular points of interest around the property include Charlotte Lake and Echo Point.offers are available all time",
    'Rating ': "4/5",
    'Cost':'1500 per night'    
    },
    {  
    'id': 3,
    'Name': "TY Cecil Hotel 2 stars",
    'Info': "13 km from Charlotte Lake and 13 km from Panorama Point.one time breakfast free offers are available only in mansoon",
    'Rating ': "3.5/5",
    'Cost':'1000 per night'   
    },
    
  ]

@plan.route('/')
def Main():
	return render_template('search.html')

@plan.route('/trip_page',methods =['POST'])
def getvalue():
    return render_template('trip.html')

@plan.route('/trip_page/start_page',methods =['POST'])
def setvalue():
    return render_template('start.html',spots = SPOTS)

@plan.route('/trip_page/start_page/route_page',methods =['POST'])
def putvalue():
    return render_template('route.html')

if __name__ == '__main__':
    plan.run()

 