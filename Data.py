import requests
import json
from functions import get_file_contents

class Data:
    #Dictionary mapping location to current lines
    lines = {}
    BUSINESS_ID = 'c6QaDLAu9T3ge_DZ7w4Sig'
    API_KEY = get_file_contents('api_key.txt')

    #Constructor method
    def __init__(self):
        pass

    @staticmethod
    #Getter method for lines
    def getLines(address):
        return Data.lines[address]

    @staticmethod
    #Setting method for lines
    def setLines(address, queue, eta):
        Data.lines[address] = [queue, eta]

    @staticmethod
    #Allows user to filter their search.
    def search(keywords, radius, location):
        ''' 
        Radius is defaulted to 10000 m
        Location is defaulted to current location (when None)
        '''
        ENDPOINT = 'https://api.yelp.com/v3/businesses/search'
        HEADERS = {'Authorization': 'bearer %s' % Data.API_KEY}
        if location == None:
            latitude = None
            longitude = None
            PARAMETERS = {'term': keywords,
              'limit': 20,
              'radius': radius,
              'latitude': latitude,
              'longitude': longitude}
        else:
            PARAMETERS = {'term':'grocery',
                'limit': 20,
                'radius': radius,
                'location': location}

        response = requests.get(url = ENDPOINT, params = PARAMETERS, headers = HEADERS)
        business_data = response.json()

        return business_data
        #for biz in business_data['businesses']:
        #    print(biz['name'])

    